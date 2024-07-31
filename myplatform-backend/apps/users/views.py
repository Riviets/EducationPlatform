from .forms import CustomUserCreationForm
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import CustomUserUpdateForm
import logging
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator

logger = logging.getLogger(__name__)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        logger.debug(f'Request POST data: {request.POST}')
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'student'  # Встановлюємо роль за замовчуванням
            user.save()
            logger.info(f'New user created: {user.username}')
            login(request, user)
            return JsonResponse({'message': 'User registered successfully'})
        else:
            logger.error(f'Error in form: {form.errors}')
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        logger.debug(f'Login - Request POST data: {request.POST}')
        logger.debug(f'Login - Request body: {request.body}')
        
        try:
            data = json.loads(request.body)
            username_or_email = data.get('username')  # Це поле може містити або username, або email
            password = data.get('password')
        except json.JSONDecodeError:
            logger.error('Invalid JSON in request body')
            return JsonResponse({'errors': 'Invalid JSON'}, status=400)
        
        logger.debug(f'Login attempt for username or email: {username_or_email}')
        
        UserModel = get_user_model()
        try:
            # Шукаємо користувача за username або email
            user = UserModel.objects.get(Q(username=username_or_email) | Q(email=username_or_email))
            # Перевіряємо пароль
            if user.check_password(password):
                login(request, user)
                request.session['userName'] = user.username
                request.session['userEmail'] = user.email
                request.session['profileImageUrl'] = user.profile_image_url if user.profile_image_url else 'https://via.placeholder.com/40'
                
                logger.info(f'User logged in successfully: {user.username}')
                logger.info(f"Session data set: {request.session['userName']}, {request.session['userEmail']}, {request.session['profileImageUrl']}")
                
                return JsonResponse({
                    'message': 'User logged in successfully',
                    'userName': user.username,
                    'userEmail': user.email,
                    'profileImageUrl': user.profile_image_url if user.profile_image_url else 'https://via.placeholder.com/40',
                    'role': user.role,
                    'phone_number': user.phone_number,
                    'id': user.id
                })
            else:
                logger.warning(f'Failed login attempt for username or email: {username_or_email}')
                return JsonResponse({'errors': 'Invalid credentials'}, status=400)
        except UserModel.DoesNotExist:
            logger.warning(f'User not found for username or email: {username_or_email}')
            return JsonResponse({'errors': 'User not found'}, status=400)
    
    return render(request, 'users/login.html')

@csrf_exempt
@login_required
def update_profile(request, user_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = get_object_or_404(CustomUser, id=user_id)
        
        form = CustomUserUpdateForm(data, instance=user)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'Profile updated successfully',
                'userName': user.username,
                'userEmail': user.email,
                'profileImageUrl': user.profile_image_url,
                'role': user.role,
                'phone_number': user.phone_number,
                'id': user.id
            })
        else:
            logger.error(f'Error in form: {form.errors}')
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'message': 'Invalid request method'}, status=400)

@csrf_exempt
@login_required
def delete_user(request, user_id):
    if request.method == 'DELETE':
        user = get_object_or_404(CustomUser, id=user_id)
        user.delete()
        return JsonResponse({'message': 'User deleted successfully'})
    return JsonResponse({'message': 'Invalid request method'}, status=400)

@csrf_exempt
def list_teachers(request):
    if request.method == 'GET':
        teachers = CustomUser.objects.filter(role='teacher')
        teachers_list = [{
            'id': teacher.id,
            'username': teacher.username,
            'email': teacher.email,
            'first_name': teacher.first_name,
            'last_name': teacher.last_name,
            'phone_number': teacher.phone_number,
            'profile_image_url': teacher.profile_image_url
        } for teacher in teachers]
        return JsonResponse(teachers_list, safe=False)
    return JsonResponse({'message': 'Invalid request method'}, status=400)


@csrf_exempt
def list_students(request):
    if request.method == 'GET':
        students = CustomUser.objects.filter(role='student')
        students_list = [{
            'id': student.id,
            'username': student.username,
            'email': student.email,
            'first_name': student.first_name,
            'last_name': student.last_name,
            'phone_number': student.phone_number,
            'profile_image_url': student.profile_image_url
        } for student in students]
        return JsonResponse(students_list, safe=False)
    return JsonResponse({'message': 'Invalid request method'}, status=400)


# Password Reset (Forgot Password)

@csrf_exempt
def reset_password_request(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        
        try:
            user = CustomUser.objects.get(email=email)
            token = default_token_generator.make_token(user)
            reset_url = f"http://localhost:3000/reset-password?uid={user.pk}&token={token}"
            send_mail(
                'Password Reset Request',
                f'Click the link below to reset your password:\n{reset_url}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            return JsonResponse({'message': 'Password reset link has been sent to your email.'})
        except CustomUser.DoesNotExist:
            return JsonResponse({'errors': 'Email not found'}, status=404)
    return JsonResponse({'message': 'Invalid request method'}, status=400)

@csrf_exempt
def reset_password_confirm(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        uid = data.get('uid')
        token = data.get('token')
        new_password = data.get('new_password')
        new_password_confirm = data.get('new_password_confirm')

        if new_password != new_password_confirm:
            return JsonResponse({'errors': 'Passwords do not match'}, status=400)

        try:
            user = CustomUser.objects.get(pk=uid)
            if default_token_generator.check_token(user, token):
                user.set_password(new_password)
                user.save()
                return JsonResponse({'message': 'Password has been reset successfully'})
            else:
                return JsonResponse({'errors': 'Invalid token'}, status=400)
        except CustomUser.DoesNotExist:
            return JsonResponse({'errors': 'Invalid user'}, status=404)
    return JsonResponse({'message': 'Invalid request method'}, status=400)


@csrf_exempt
def test_email(request):
    send_mail(
        'Test Email',
        'This is a test email from Django.',
        settings.DEFAULT_FROM_EMAIL,
        ['boghtml@gmail.com'],
        fail_silently=False,
    )
    return JsonResponse({'message': 'Email sent successfully'})



# change th password with a old one
@csrf_exempt
@login_required
def change_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        old_password = data.get('old_password')
        new_password = data.get('new_password')
        new_password_confirm = data.get('new_password_confirm')

        if new_password != new_password_confirm:
            return JsonResponse({'errors': 'New passwords do not match'}, status=400)

        user = request.user

        if not user.check_password(old_password):
            return JsonResponse({'errors': 'Old password is incorrect'}, status=400)

        user.set_password(new_password)
        user.save()
        return JsonResponse({'message': 'Password has been changed successfully'})
    return JsonResponse({'message': 'Invalid request method'}, status=400)
