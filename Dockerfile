FROM python:3.7-alpine

ENV PYTHONPATH=venv:.:/venv
ADD . /
RUN pip install -r requirements.txt

EXPOSE 5005

ENTRYPOINT ["python"]
CMD ["-m", "make.server"]

