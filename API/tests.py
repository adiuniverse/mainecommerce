from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework.test import APIClient
from rest_framework import status
# Create your tests here.


class TestSample(TestCase):
    def setup(self):
        self.client = APIClient

    def test_index(self):
        url = reverse ('api:index') # eg : api/index
        res = self.client.get(url) # to get the response from the server
         
        self.assertEquals(res.data, 'Congratulations, you have created an API')


    
    def test_home(self):
        url = reverse('api:home')
        res = self.client.get(url)
        

        data = res.data

        if type(data) != float:
            self.fail('not a floating point')
        






   









