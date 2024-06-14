FROM python:3.12-bookworm

COPY . .

RUN pip install poetry
RUN poetry install

ENTRYPOINT ["python", "bot.py"]