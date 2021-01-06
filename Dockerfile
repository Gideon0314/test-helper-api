FROM python:3.8.5

COPY ./back-end /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt && pip install pymysql gunicorn
ENV FLASK_APP test_helper.py
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
