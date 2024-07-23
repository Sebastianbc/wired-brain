# Start from the Python official image
FROM python

#Set the container working directory. The remaining statements in this Docker file
#will be relative to this path
WORKDIR /code

#Copy the requirements.txt file in the current project path 
#to the current container working directory
COPY requirements.txt .

#Run command
RUN pip install -r requirements.txt

#Copy the defined folder to the container working directory
COPY /src .

#Run python ./app.py
CMD ["python", "./app.py"]