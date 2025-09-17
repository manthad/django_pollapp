services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: ${DATABASE_NAME}
      POSTGRES_USER: ${DATABASE_USERNAME}
      POSTGRES_PASSWORD: ${DATABASE_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5433:5432"

  web:
    build: .
    # container name: postgress-container-compose
    ports:
     - "8000:8000"
    depends_on:
     - db
    environment:
     DJANGO_SECRET_KEY: ${DJANGO_SECRET_KEY}
     DEBUG: ${DEBUG}
     DJANGO_LOGLEVEL: ${DJANGO_LOGLEVEL}
     DJANGO_ALLOWED_HOSTS: ${DJANGO_ALLOWED_HOSTS}
     DATABASE_ENGINE: ${DATABASE_ENGINE}
     DATABASE_NAME: ${DATABASE_NAME}
     DATABASE_USERNAME: ${DATABASE_USERNAME}
 
     DATABASE_PASSWORD: ${DATABASE_PASSWORD}
     DATABASE_HOST: ${DATABASE_HOST}
     DATABASE_PORT: ${DATABASE_PORT}
    env_file:
     - .env
volumes:
  postgres_data: