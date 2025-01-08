# set base image
FROM python:3.10-slim

# work directory
WORKDIR /app

COPY . /app

# install
RUN pip install --no-cache-dir -r requirement.txt

RUN apt-get update && apt-get install -y \
    chromium-driver \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 5001

CMD ["python", "app.py"]
