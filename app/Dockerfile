FROM python:3.8.10

COPY image_service /app

WORKDIR app

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "Rest.py", "--port", "5000"]