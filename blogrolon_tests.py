# -*- coding: utf-8 -*-

import os
import blogrolon
import unittest
import tempfile


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, blogrolon.app.config['DATABASE'] = tempfile.mkstemp()
        blogrolon.app.config['TESTING'] = True
        self.app = blogrolon.app.test_client()
        blogrolon.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(blogrolon.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()
