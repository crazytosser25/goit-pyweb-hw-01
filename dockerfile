FROM python:3.12-bookworm

WORKDIR /assist
COPY . .

RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install

ENTRYPOINT ["poetry", "run", "python", "bot.py"]