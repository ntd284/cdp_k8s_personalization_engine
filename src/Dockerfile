FROM python:3.8

WORKDIR /src

COPY requirements.txt /src/

RUN pip3 install --no-cache-dir -r requirements.txt



COPY api_start.py /src/
COPY personalization_router.py /src/
COPY personalization.py /src/
CMD ["python3", "/src/api_start.py"]
