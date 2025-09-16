FROM python:3.11-slim AS builder

RUN apt-get update && \
    apt-get install -y python3-pip python3-dev build-essential && \
    ln -s /usr/bin/python3 /usr/bin/python

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

FROM python:3.11-slim
RUN useradd -m -r appuser && \
    mkdir /app && \
    chown appuser /app
# Copy the python dependencies from the builder stage    
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
WORKDIR /app
COPY --chown=appuser:appuser . . 
# this is copying all the application code into this app folder with this user and giving permission to it
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
USER appuser
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "mysite.wsgi:application"]