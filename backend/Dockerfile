FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/
COPY ML-model/fetch_latest_model.py /app/ML-model/
COPY backend/ /app/

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

ENV DAGSHUB_TOKEN=${DAGSHUB_TOKEN}
RUN python /app/ML-model/fetch_latest_model.py

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
