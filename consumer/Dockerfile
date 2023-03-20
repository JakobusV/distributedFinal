FROM python:3.9.6
WORKDIR /code
ENV DATABASE_URL=postgresql://postgres:admin@host.docker.internal:6543/dockerDB
COPY ./requirements.txt /code/requirements.txt
RUN apt-get update && apt-get install -y iputils-ping
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["python3", "-u", "/code/app/startup.py"]