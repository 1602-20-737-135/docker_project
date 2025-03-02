# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /home/data

# Copy necessary files into the container
COPY scripts/script.py .
COPY data/IF-1.txt .
COPY data/AlwaysRememberUsThisWay-1.txt .

# Ensure the output directory exists
RUN mkdir -p /home/data/output

# Run the Python script when the container starts
CMD ["python", "script.py"]
