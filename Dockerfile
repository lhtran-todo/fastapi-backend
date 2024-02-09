FROM python:3.11-slim-bookworm
ENV PORT=8000
WORKDIR /src
COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt
COPY ./app /src/app
CMD ["bash", "-c", "uvicorn app.main:app --proxy-headers --forwarded-allow-ips=* --host 0.0.0.0 --port $PORT"]