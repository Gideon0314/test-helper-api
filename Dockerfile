FROM python:3.8.5

WORKDIR /usr/src/app
COPY ./test_helper_api /usr/src/app
RUN rm -f /etc/localtime \
&& ln -sv /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& echo "Asia/Shanghai" > /etc/timezone
RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
ENV FLASK_APP test_helper.py
EXPOSE 5000
CMD ["gunicorn", "test_helper:app", "-c", "./gunicorn.conf.py"]
