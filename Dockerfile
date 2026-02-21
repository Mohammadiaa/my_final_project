FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip cache purge && \
    pip install --no-cache-dir -r requirements.txt


COPY . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
