FROM python:3.9.0

WORKDIR /home/
# Root Directory로 접근
RUN echo "testing"
#git에 들어가는 source code가 바뀌었는데 docker가 cashe된 이미지를 계속 써서 앞에 변경 사항이 있어야 합니다.
RUN git clone https://github.com/airhac/reportDjango.git
# Root Directory 밑에 github에 저장한 reportDjango를 저장 해줍니다.
WORKDIR /home/reportDjango/
#Root Directory 아래에 있는 reportDjango에 접근 해줍니다.
RUN pip install - r requirements.txt
#requirements.txt에 있는 모든 명령어를 실행 시켜 설치 시켜주겠다.
RUN pip install gunicorn
#RUN echo "시크릿 키" > .env
RUN pip install mysqlclient

RUN python manage.py collectstatic

EXPOSE 9000

#Docker에 적용이 되지 않습니다.
#이 명령어를 가지고 db와 연동해 줍니다.
#Command에 넣어주어야하는 명령어가 두개가 생깁니다.
CMD ["bash","-c","python manage.py migrate --settings=reportDjango.deploy && gunicorn reportDjango.wsgi --env DJANGO_SETTINGS_MODULE=reportDjango.settings.deploy --bind 0.0.0.0:9000"]
#git 저장소에 secret KEY가 없어서 위의 명령어가 제대로 실행 되지 않습니다.
#그래서 SECRET KEY를 임의로 지정해 줍니다.
# 현재 manage.py의 설정 경로를 local로 해둔 상태 입니다.
#local 환경 기반으로 migrate를 하게 되어있습니다.
#gunicorn 환경 세팅에 deploy로 사용하도록 해줍니다.