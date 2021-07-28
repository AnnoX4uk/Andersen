FROM python:3.7-alpine as base
FROM base as builder-stage1
RUN mkdir /install
WORKDIR /install
RUN pip install --prefix=/install flask
FROM base as builder-stage2
RUN mkdir /install
WORKDIR /install-app
ADD helloworld.py /install-app/
FROM base
RUN mkdir /app
COPY --from=builder-stage1 /install /usr/local
COPY --from=builder-stage2 /install-app /app
WORKDIR /app
EXPOSE 8080
CMD ["python3", "/app/helloworld.py"]
