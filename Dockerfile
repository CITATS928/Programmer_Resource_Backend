# set base image
FROM python:3.10-slim

# work directory
WORKDIR /app

COPY . /app

# install
RUN pip install --no-cache-dir -r requirement.txt

EXPOSE 5000

CMD ["python", "app.py"]
