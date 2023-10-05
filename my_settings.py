from pathlib import Path
from django.core.exceptions import ImproperlyConfigured
import os
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# JSON 파일에 Secret key두고 -> 그 파일에서 SECRET_KEY를 가져와서 여기서 사용 -> JSON 파일은 .gitignore
secret_file = os.path.join(BASE_DIR, 'secrets.json')
with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    """Get SECRET_KEY Value or Error"""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = f"Set the {setting} environment variable."
        raise ImproperlyConfigured(error_msg)


#my_settings.py
DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME':'Local instance MySQL',
        'USER':'root',
        'PASSWORD':'0000',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

SECRET_KEY = get_secret("SECRET_KEY")
