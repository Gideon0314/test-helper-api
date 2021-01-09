FROM python:3.8.5

WORKDIR /usr/src/app
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
ENV FLASK_APP test_helper.py
EXPOSE 5000
COPY . .
CMD ["gunicorn", "test_helper:app", "-c", "./gunicorn.conf.py"]