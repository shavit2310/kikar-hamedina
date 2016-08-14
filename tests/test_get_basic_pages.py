from unittest import TestCase

import django
django.setup()

import requests
from logging import getLogger

logger = getLogger("my_logger")

class BasicPagesTestCase(TestCase):

    def setUp(self):
        self.member_id = "731"
        self.party_id = 32

    def test_get_homepage(self):
        response = requests.get("http://localhost:8000")
        self.assertEqual(response.status_code, 200)

    def test_get_mk_page(self):
        mk_page_url = "http://localhost:8000/member/{member_id}".format(member_id=self.member_id)
        response = requests.get(mk_page_url)
        self.assertEqual(response.status_code, 200)

    def test_get_party_page(self):
        party_page_url = "http://localhost:8000/party/{party_id}".format(party_id=self.party_id)
        response = requests.get(party_page_url)
        self.assertEqual(response.status_code, 200)

