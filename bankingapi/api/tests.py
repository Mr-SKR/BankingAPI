from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

# Create your tests here.
# from .models import Bucketlist
from .models import Banks, Branches


class ModelTestCase(TestCase):
    """This class defines the test suite for the banks model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.bank_name = "Bank name"
        self.bank_id = 1
        self.banks = Banks(name=self.bank_name, id=self.bank_id)

    def test_model_can_create_a_bank(self):
        """Test the banks model can create a bank."""
        old_count = Banks.objects.count()
        self.banks.save()
        new_count = Banks.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.bank_data = {'name': 'HDFC BANK', 'id': 1}
        self.response = self.client.post(
            reverse('create'),
            self.bank_data,
            format="json")

    def test_api_can_create_a_bank(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_bank(self):
        """Test the api can get a given bank."""
        bank = Banks.objects.get()
        response = self.client.get(
            reverse('details',
                    kwargs={'pk': bank.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bank)

    def test_api_can_update_bank(self):
        """Test the api can update a given bank."""
        bank = Banks.objects.get()
        change_bucketlist = {'name': 'Something new', 'id': 1}
        res = self.client.put(
            reverse('details', kwargs={'pk': change_bucketlist['id']}),
            change_bucketlist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bank(self):
        """Test the api can delete a bucketlist."""
        bank = Banks.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bank.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
