FROM python:alpine

RUN pip install fastapi uvicorn python-dotenv httpx

EXPOSE 80

COPY ./ .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
