# -*- coding: utf-8 -*-
import unittest

import os
import app
import tempfile

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

if __name__ == '__main__':
    unittest.main()
