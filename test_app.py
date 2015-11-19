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

if __name__ == '__main__':
    unittest.main()
