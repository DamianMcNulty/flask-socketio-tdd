import unittest
import json

from server import app

class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_getdata(self):
        tester = app.test_client(self)
        response = tester.get('/data', content_type='application/json')
        users = json.loads(response.data)
        self.assertEqual(users[0]['id'], 1)
        self.assertEqual(users[0]['name'], 'Juan')


if __name__ == '__main__':
    unittest.main()
