from .base import *
env_list = dict()

local_env = open(os.path.join(BASE_DIR, '.env'))

while True:
    line = local_env.readline()
    if not line:
        break
    line = line.replace('\n', '')
    start = line.find('=')
    key = line[:start]
    value = line[start+1:]
    env_list[key] = value

SECRET_KEY = env_list['SECRET_KEY']
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
#개발중인 상태를 위한 것
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #mariadb자체가 mysql에서 분기된 것입니다.
        'NAME': 'django',
        #mariadb안에서 만드는 db의 이름
        'USER': 'django',
        'PASSWORD': 'password1234',
        'HOST': 'mariadb',
        #네트워크를 사용하여 django와 mariadb를 연결 시켜줄것인데
        #container이름으로 통신을 하기 때문에 mariadb의 container 이름을 적어 줍니다.
        'PORT': '3306',
    }
}