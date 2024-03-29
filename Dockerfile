FROM python:3.10

WORKDIR /

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY ./ ./

CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "80"]