from pathlib import Path
from decouple import config

# Caminho base do projeto (raiz do repositório)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Segurança
SECRET_KEY = 'django-insecure-d%+is^+ijz%vy6@5s%stz&n#8-x=j@^7+!xteo5(x0(10ds@m6'
DEBUG = True
ALLOWED_HOSTS = []

# Aplicações instaladas
INSTALLED_APPS = [
    'widget_tweaks',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps do projeto
    'apps.alimentacao',
    'apps.ordenha',
    'apps.reproducao',
    'apps.saude',
    'apps.usuarios',
]

# Middlewares padrão do Django
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuração de rotas
ROOT_URLCONF = 'sistemarural.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'backend' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = 'sistemarural.wsgi.application'

# Banco de dados sqlite3
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'backend' / 'db.sqlite3',
#     }
# }

# Banco de dados PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY')

# Validação de senha
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internacionalização
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Arquivos estáticos
STATIC_URL = 'static/'
STATICFILES_DIRS = [ BASE_DIR / 'backend' / 'static' ]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Configuração padrão para chaves primárias
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuração de arquivos de mídia
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
