<h1>Education Platform</h1>

<h2>Overview</h2>

<p>The Education Platform is a comprehensive web application designed for educational purposes. It provides functionality for users to register, log in, manage their profiles, and browse courses. Administrators and teachers can add, edit, and delete courses. This platform is built using Django for the backend and React for the frontend.</p>

<h2>Features</h2>

<ul>
  <li>User Registration and Authentication
    <ul>
      <li>Users can register using their email.</li>
      <li>Login using username or email.</li>
      <li>Profile management: users can update their profile information.</li>
    </ul>
  </li>
  <li>Course Management
    <ul>
      <li>Users can view available courses.</li>
      <li>Admins and teachers can add new courses.</li>
      <li>Edit existing courses.</li>
      <li>Delete courses.</li>
    </ul>
  </li>
  <li>Dashboard
    <ul>
      <li>Personalized dashboard for users with a profile picture.</li>
      <li>Access to user-specific courses and functionalities.</li>
    </ul>
  </li>
</ul>

<h2>Technologies Used</h2>

<ul>
  <li><strong>Backend</strong>: Django, Django REST framework</li>
  <li><strong>Frontend</strong>: React</li>
  <li><strong>Database</strong>: PostgreSQL</li>
  <li><strong>Authentication</strong>: Django's built-in authentication system</li>
  <li><strong>Styling</strong>: Bootstrap, custom CSS</li>
</ul>

<h2>Installation</h2>

<h3>Prerequisites</h3>

<ul>
  <li>Python 3.8+</li>
  <li>Node.js 14+</li>
  <li>PostgreSQL</li>
</ul>

<h3>Backend Setup</h3>

<ol>
  <li>
    <strong>Clone the repository</strong>
    <pre><code>git clone https://github.com/yourusername/education-platform.git
cd education-platform/myplatform-backend
</code></pre>
  </li>
  <li>
    <strong>Create and activate a virtual environment</strong>
    <pre><code>python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
</code></pre>
  </li>
  <li>
    <strong>Install the required packages</strong>
    <pre><code>pip install -r requirements.txt
</code></pre>
  </li>
  <li>
    <strong>Configure the database</strong>
    <p>Create a PostgreSQL database and update the <code>DATABASES</code> settings in <code>myplatform/settings.py</code> with your database credentials.</p>
  </li>
  <li>
    <strong>Run migrations</strong>
    <pre><code>python manage.py migrate
</code></pre>
  </li>
  <li>
    <strong>Create a superuser</strong>
    <pre><code>python manage.py createsuperuser
</code></pre>
  </li>
  <li>
    <strong>Run the development server</strong>
    <pre><code>python manage.py runserver
</code></pre>
  </li>
</ol>

<h3>Frontend Setup</h3>

<ol>
  <li>
    <strong>Navigate to the frontend directory</strong>
    <pre><code>cd ../myplatform-frontend
</code></pre>
  </li>
  <li>
    <strong>Install the required packages</strong>
    <pre><code>npm install
</code></pre>
  </li>
  <li>
    <strong>Start the development server</strong>
    <pre><code>npm start
</code></pre>
    <p>The frontend development server will start at <code>http://localhost:3000</code>.</p>
  </li>
</ol>

<h2>Usage</h2>

<ol>
  <li>Open your browser and navigate to the frontend URL: <code>http://localhost:3000</code></li>
  <li>Register a new user: Go to the registration page and fill out the form. After registration, you will be redirected to the login page.</li>
  <li>Log in: Enter your username or email and password to log in.</li>
  <li>Dashboard: After logging in, you will be redirected to the user dashboard. The dashboard displays user information and available functionalities.</li>
  <li>Course Management: Users can browse courses. Admins and teachers can add, edit, or delete courses.</li>
</ol>

![Знімок екрана 2024-07-30 145303](https://github.com/user-attachments/assets/0b8e3568-3f9e-4273-8aea-ad78cdf1c4ac)

<h2>Curent API Endpoints</h2> 

<ul>
  <li>User Registration: <code>POST /api/users/register/</code></li>
  <li>User Login: <code>POST /api/users/login/</code></li>
  <li>Update Profile: <code>PUT /api/users/update-profile/<int:user_id>/</code></li>
  <li>Course List: <code>GET /api/courses/</code></li>
  <li>Course Detail: <code>GET /api/courses/<int:course_id>/</code></li>
  <li>Add Course: <code>POST /api/courses/</code></li>
  <li>Update Course: <code>PUT /api/courses/<int:course_id>/</code></li>
  <li>Delete Course: <code>DELETE /api/courses/<int:course_id>/</code></li>
</ul>

<h2>Project Structure</h2>

<pre><code>
EducationPlatform/
│
├── myplatform-backend/
│   ├── myplatform/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── apps/
│   │   ├── users/
│   │   ├── courses/
│   │   ├── assignments/
│   │   ├── payments/
│   │   └── notifications/
│   ├── manage.py
│   ├── requirements.txt
│   └── .env
│
├── myplatform-frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   └── .env
│
├── .gitignore
└── README.md
</code></pre>

<h2>Contributing</h2>

<ul>
  <li>Fork the repository</li>
  <li>Create a new branch for your feature or bugfix</li>
  <li>Commit your changes</li>
  <li>Push to your branch</li>
  <li>Create a pull request</li>
</ul>
