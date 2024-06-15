FROM python:3.12-slim-bookworm

WORKDIR /assistant
COPY . .

RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install

ENTRYPOINT ["poetry", "run", "python", "bot.py"]