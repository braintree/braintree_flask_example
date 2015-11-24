# Braintree Flask Example
An example Braintree integration for python in the Flask framework.

## Setup Instructions

1. Install requirements
  `pip install -r requirements.txt`

2. Copy the `application.cfg.sample` file to `application.cfg` and fill in your Braintree API credentials. Credentials can be found by navigating to Account > My user > View API Keys in the Braintree control panel. Full instructions can be [found on our support site](https://articles.braintreepayments.com/control-panel/important-gateway-credentials#api-credentials).

3. Start server
  `python app.py`

## Running tests

Unit tests do not make api calls to Braintree and do not require Braintree credentials. You can run this project's unit tests by calling `python test_app.py` on the command line.

## Pro Tips

- The `application.cfg.example` contains an `APP_SECRET_KEY` setting. Even in development you should [generate your own custom secret key for your app](http://flask.pocoo.org/docs/0.10/quickstart/#sessions).

## Disclaimer

This code is provided as is and is only intended to be used for illustration purposes. This code is not production-ready and is not meant to be used in a production environment. This repository is to be used as a tool to help merchants learn how to integrate with Braintree. Any use of this repository or any of its code in a production environment is highly discouraged.
