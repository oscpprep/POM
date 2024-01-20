# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Copy the project files
COPY . /POM
WORKDIR /POM

# Upgrade pip and install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

ENTRYPOINT ["pytest"]

CMD []
