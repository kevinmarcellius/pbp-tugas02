from django.test import TestCase
class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        response = self.client.get('/mywatchlist/')
        self.assertEqual(response.status_code, 200)
    def test_xml_loads_properly(self):
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)
    def test_json_loads_properly(self):
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
    def test_index_html_properly(self):
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)