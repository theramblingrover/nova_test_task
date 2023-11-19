FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /app

# Copy the dependencies
COPY requirements.txt .

# Install the dependencies
RUN pip3 install -r /app/requirements.txt \
 && rm -rf /root/.cache/pip

COPY . .

# Use SIGINT To stop django process
STOPSIGNAL SIGINT