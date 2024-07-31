# apps/users/urls.py

from django.urls import path
from .views import register, login_view, update_profile, delete_user, list_teachers, list_students, reset_password_request, reset_password_confirm, test_email, change_password

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('update-profile/<int:user_id>/', update_profile, name='update_profile'),
    path('delete-user/<int:user_id>/', delete_user, name='delete_user'),  # New URL pattern for deleting a user
    path('teachers/', list_teachers, name='list_teachers'),  # New URL pattern for listing teachers
    path('students/', list_students, name='list_students'),  # New URL pattern for listing students
    path('reset-password-request/', reset_password_request, name='reset_password_request'),
    path('reset-password-confirm/', reset_password_confirm, name='reset_password_confirm'),
    path('test-email/', test_email, name='test_email'),
    
    path('change-password/', change_password, name='change_password'),
]
