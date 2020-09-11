from django.urls import reverse

from rest_framework.test import APITestCase

from db_script import db_init
from result.models import Company, Result


class CompanyTestCase(APITestCase):

    def setUp(self):  # --keepdb to avoid building the db on each run
        db_init()

    def test_count(self):
        self.assertEqual(Company.objects.count(), 1000)
        self.assertEqual(Result.objects.count(), 2000)

    def test_api_get(self):
        url_list = reverse('company-list')
        response = self.client.get(url_list)
        assert response.status_code == 200

        url_detail = reverse('company-detail', kwargs={'pk': 1})
        response = self.client.get(url_detail)
        assert response.status_code == 200
