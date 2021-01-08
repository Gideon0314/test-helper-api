FROM python:3.8.5

COPY ./test_helper_api /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt && pip install gunicorn gevent
ENV FLASK_APP test_helper.py
EXPOSE 5000
#ENTRYPOINT ["./boot.sh"]
CMD ["gunicorn", "test_helper:app", "-c", "./gunicorn.conf.py"]