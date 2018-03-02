FROM python:3.6.4

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app

# run server
CMD python managa.py run -h 0.0.0.0