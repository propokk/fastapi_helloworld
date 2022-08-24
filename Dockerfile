FROM python:3.10

WORKDIR /hw_code

COPY ./requirements.txt /hw_code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /hw_code/requirements.txt

COPY ./backend /hw_code

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]