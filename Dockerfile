# Use a base image
FROM ubuntu:20.04

# Install Python and necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Set the working directory
WORKDIR /src

# Copy the application code into the container
COPY src/ /src/

# Install dependencies
# RUN pip3 install -r /src/requirements.txt

# Expose the FastAPI port
EXPOSE 8000

# Run the application
CMD ["python3", "src/api_start.py"]
