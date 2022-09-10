FROM python:3

WORKDIR /dex-pysmtplib

COPY src/dex.py .

CMD ["python", "./dex.py"]