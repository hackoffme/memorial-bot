FROM python:3.10
RUN useradd --create-home app
WORKDIR /home/app
USER app

COPY --chown=app:app api/requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY --chown=app:app .env .
COPY --chown=app:app ./api/ ./api/
CMD uvicorn api.main:app 