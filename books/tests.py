from django.test import TestCase

class SimpleTest(TestCase):
    def test_home_page_status(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
