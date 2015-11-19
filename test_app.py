# -*- coding: utf-8 -*-
import unittest
from mock import mock

import os
import app
import tempfile

@mock.patch('braintree.ClientToken.generate', staticmethod(lambda: "test_client_token"))
class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def test_checkouts_new_route_available(self):
        res = self.app.get('/checkouts/new')
        self.assertEquals(res.status_code, 200)

    def test_root_redirect_to_checkout(self):
        res = self.app.get('/')
        self.assertEquals(res.status_code, 302)
        self.assertTrue('/checkouts/new' in res.location)

    def test_checkout_contains_client_token(self):
        res = self.app.get('/checkouts/new')
        self.assertTrue('var client_token = \'test_client_token\';' in res.data)

    def test_checkout_contains_checkout_form(self):
        res = self.app.get('/checkouts/new')
        self.assertTrue('<form id="checkout"' in res.data)

    def test_checkout_contains_payment_form_div(self):
        res = self.app.get("/checkouts/new")
        self.assertTrue('<div id="payment-form"' in res.data)

if __name__ == '__main__':
    unittest.main()
