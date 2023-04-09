FROM python:3.11-alpine3.16

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN  apk update \
	&& apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
	&& pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY  ./ ./

CMD ["gunicorn", "-c", "config/gunicorn/config.py", "--bind", "8000", "--chdir", "MartFarming", "MartFarming.wsgi:application"]