FROM python:2.7

RUN apt-get update && apt-get install -y build-essential

ADD . /var/www/braintree_flask_example
WORKDIR /var/www/braintree_flask_example

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
