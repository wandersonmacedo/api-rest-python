FROM python:3.8

RUN pip install fastapi uvicorn python-dotenv httpx psycopg2 alembic

EXPOSE 80

COPY ./ .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
