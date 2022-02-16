FROM python:3.8

ENV TZ=Europe/Zurich

RUN mkdir /app
COPY .. /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["bash"]
