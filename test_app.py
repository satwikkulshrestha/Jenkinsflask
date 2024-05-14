import pytest
from app import app

class TestApp(pytest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello World')

if __name__ == '__main__':
    pytest.main()
