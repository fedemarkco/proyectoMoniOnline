FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /app && cd /app
WORKDIR /app
COPY . /app
RUN pip install -r /app/requirements.txt
RUN chmod +x /app/run.sh