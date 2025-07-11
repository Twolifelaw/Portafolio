# backend/settings.py

from pathlib import Path
from decouple import config
import sys
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ===================================================================
# ▼ CORRECCIÓN 1: Mueve estas líneas aquí arriba y borra las del final ▼
# ===================================================================
SECRET_KEY = config('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Ya no necesitas las líneas originales que tenían la clave quemada
# SECRET_KEY = 'django-insecure-...'
# DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', os.environ.get('RENDER_EXTERNAL_HOSTNAME')]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # --- Librerías de terceros ---
    'rest_framework',
    'corsheaders',
    # --- Tu app ---
    'api',
]

# ===================================================================
# ▼ CORRECCIÓN 2: Orden correcto del Middleware (y sin duplicados)  ▼
# ===================================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # <-- Ponerlo aquí
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Portafolio.urls' # Asegúrate que el nombre sea 'backend.urls' si así llamaste al proyecto

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Portafolio.wsgi.application' # Asegúrate que sea 'backend.wsgi.application'

# Database
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}

# Use SQLite in-memory for tests
if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    # ... (esto está bien como estaba)
]

# Internationalization
LANGUAGE_CODE = 'es-co' # <-- ¡Cambiado a español de Colombia!
TIME_ZONE = 'America/Bogota' # <-- ¡Cambiado a tu zona horaria!
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS Configuration
CORS_ALLOWED_ORIGINS = [
    "https://portfolio-front-gold-phi.vercel.app",
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
]

# Configuración de Correo Electrónico
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Para Gmail
EMAIL_PORT = 587
EMAIL_USE_TLS = True  # Usar TLS para seguridad
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
SERVER_EMAIL = config('SERVER_EMAIL')

# Opcional: Para depuración, puedes usar el backend de consola
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'