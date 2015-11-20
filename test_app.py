# -*- coding: utf-8 -*-
import unittest
import mock
import test_helpers

import os
import app
import tempfile

@mock.patch('braintree.ClientToken.generate', staticmethod(lambda: "test_client_token"))
@mock.patch('braintree.Transaction.find', staticmethod(lambda x: test_helpers.MockObjects.TRANSACTION))
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
        self.assertIn('/checkouts/new', res.location)

    def test_checkout_contains_client_token(self):
        res = self.app.get('/checkouts/new')
        self.assertIn('var client_token = \'test_client_token\';', res.data)

    def test_checkout_contains_checkout_form(self):
        res = self.app.get('/checkouts/new')
        self.assertIn('<form id="checkout"', res.data)

    def test_checkout_contains_payment_form_div(self):
        res = self.app.get("/checkouts/new")
        self.assertIn('<div id="payment-form"', res.data)

    def test_checkouts_show_route_available(self):
        res = self.app.get("/checkouts/1")
        self.assertEquals(res.status_code, 200)

    def test_checkouts_show_displays_info(self):
        res = self.app.get("/checkouts/1")
        self.assertIn('my_id', res.data)
        self.assertIn('10.00', res.data)
        self.assertIn('MasterCard', res.data)
        self.assertIn('ijkl', res.data)
        self.assertIn('Billson', res.data)
        self.assertIn('Billy Bobby Pins', res.data)

if __name__ == '__main__':
    unittest.main()
