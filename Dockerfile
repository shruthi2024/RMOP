#         # Use a base Python image (choose a specific version based on your needs)
# FROM python:3.9
#
# # Create a working directory inside the container
# WORKDIR /app
#
# # Install required libraries using pip
# RUN pip install <library_name>  # Replace with your library names
#
# # Copy your Python script to the working directory
# COPY script.py .
#
# # Set the command to execute your script when the container starts
# CMD ["python", "script.py"]


FROM python:3.9-slim
WORKDIR /app
RUN pip install paramiko
RUN apt-get update && apt-get install -y iputils-ping
COPY login.py .
COPY ec2_in2.pem .
CMD ["python","login.py"]

