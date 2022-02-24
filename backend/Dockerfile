FROM python:3.9

RUN pip install --upgrade pip
RUN pip install poetry

WORKDIR /backend

COPY poetry.lock pyproject.toml /backend/

RUN poetry config virtualenvs.create false && poetry install

COPY . /backend/
