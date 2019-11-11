FROM python:3.7-alpine

ADD . /
RUN pip install -r requirements.txt

EXPOSE 5005

ENTRYPOINT ["python"]
CMD ["-m", "server"]

