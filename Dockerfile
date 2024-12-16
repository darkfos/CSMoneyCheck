FROM python:3.12

WORKDIR /backend

COPY . .

RUN pip3 install  --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]