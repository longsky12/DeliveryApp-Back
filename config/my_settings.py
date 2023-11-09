from pathlib import Path
from django.core.exceptions import ImproperlyConfigured
import os
import json

BASE_DIR = Path(__file__).resolve().parent.parent
# print(BASE_DIR)
# C:\Users\Jeong\Desktop\capstone\DeliveryApp-Back

# SECRET_KEY는 외부로 알려지면 보안상 문제가 생김 -> 아래는 이를 해결해주는 함수
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


# mySQL 잘 저장 되는것 확인 ORM 연동도 잘 수행됨
# NAME 부분만 우리가 저장할 데이터베이스 만들어서 바꿔주기
# 보안상 USER랑 비번도 바꿔주는게 좋을듯 하다
# my_settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Local instance MySQL',
        'USER': 'root',
        'PASSWORD': '0000',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

SECRET_KEY = get_secret("SECRET_KEY")

payment_secret_file = os.path.join(BASE_DIR, 'payment_secrets.json')
with open(payment_secret_file) as f:
    admin_key = json.loads(f.read())


def get_payment_secrets(setting, secrets=admin_key):
    """Get SECRET_KEY Value or Error"""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = f"Set the {setting} environment variable."
        raise ImproperlyConfigured(error_msg)


ADMIN_KEY = get_payment_secrets("ADMIN_KEY")
