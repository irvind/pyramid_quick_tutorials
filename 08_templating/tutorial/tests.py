import unittest
from pyramid import testing

from .views import home, hello


class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        response = home(testing.DummyRequest())
        self.assertEqual(response['name'], 'Home view')

    def test_hello(self):
        response = hello(testing.DummyRequest())
        self.assertEqual(response['name'], 'Hello view')


class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main
        from webtest import TestApp

        app = main({})
        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'<h1>Hi Home view', res.body)

    def test_hello(self):
        res = self.testapp.get('/howdy', status=200)
        self.assertIn(b'<h1>Hi Hello view', res.body)
