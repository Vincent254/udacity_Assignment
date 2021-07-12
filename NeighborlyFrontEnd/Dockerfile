FROM python:3.7
#FROM mcr.microsoft.com/azure-functions/python:3.0-python3.7
ENV host:logger:consoleLoggingMode=always

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt

EXPOSE 5000


CMD ["python", "/code/app.py"]
# Base the image on the built-in Azure Functions Python image
#FROM mcr.microsoft.com/azure-functions/python:3.0-python3.7

#ENV host:logger:consoleLoggingMode=always

# Add files from this repo to the root site folder.
#COPY . /home/site/wwwroot

#EXPOSE 8080

# Install requirements
#RUN cd /home/site/wwwroot && pip install -r requirements.txt