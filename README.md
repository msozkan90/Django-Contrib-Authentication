# Django-Contrib-Authentication


Django is a Python library for create web applications.

In this project you can login, logout, register and reset your account password with mail

## Tech
- Python - Django

- HTML 

- CSS - Bootstrap

## Installation
Instal Python to your device

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install library.

Activate the virtual environment for use this project easily.

- Download project files 

- Unzip project files

- Open project in your IDE

- Run the code given below for activate virtual environment
```bash
& write-here-your-project-path/DjangoAuth/authentication-env/Scripts/Activate.ps1
```

## Usage
- Migrate and create given  tables in django
```bash
python manage.py migrate
```
- Create super user to manage your admin panel
```bash
python manage.py createsuperuser
```
- You have to configure email settings in settings.py 
```python

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = "" # Enter your email address example: youremail@mail.com
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = "" #Enter your email's password

```

- After these, you can run your project
```bash
python manage.py runserver
```


