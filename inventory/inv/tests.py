from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class CategoryTests(APITestCase):
    def test_post_unauthenticated_category(self):
        data = {'name': 'Bath'}
        response = self.client.post('/api/category/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_create_category(self):
        user = User.objects.create_user('test', 'test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
             
        data = {'name': 'Bath'}
        response = self.client.post('/api/category/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_get_category(self):
        user = User.objects.create_user('test', 'test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
             
        data = {'name': 'Bath'}
        self.client.post('/api/category/', data, format='json')
        
        data1 = {'name': 'Office'}
        self.client.post('/api/category/', data1, format='json')
        
        response = self.client.get('/api/category/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_a_category(self):
        user = User.objects.create_user('test', 'test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
             
        data = {'name': 'Bath'}
        self.client.post('/api/category/', data, format='json')
        
        response = self.client.get('/api/category/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_update_category(self):
        user = User.objects.create_user('test', 'test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
        
        data = {'name': 'Bath'}
        self.client.post('/api/category/', data, format='json')
        
        data_update = {'name': 'Bathroom'}
        response = self.client.put('/api/category/1/', data_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_delete_category(self):
        user = User.objects.create_user('test', 'test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
             
        data = {'name': 'Bath'}
        self.client.post('/api/category/', data, format='json')
        
        response = self.client.delete('/api/category/1', format='json')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
        
class ProductTests(APITestCase):
    def test_post_unauthenticated_product(self):
        data = {
                "name": "Soap",
                "price": 1.00,
                "qty": 5,
                "out_of_stock": False,
                "category": [1]
                }
        
        response = self.client.post('/api/product/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_create_product(self):
        user = User.objects.create_user('test', 'test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
             
        data_category = {'name': 'Bath'}
        self.client.post('/api/category/', data_category, format='json')
        
        data_product = {
                        "name": "Soap",
                        "price": 1.00,
                        "qty": 5,
                        "out_of_stock": False,
                        "category": [1]
                        }
        
        response = self.client.post('/api/product/', data_product, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_get_product(self):
        user = User.objects.create_user('test', 'test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
             
        data = {'name': 'Bath'}
        self.client.post('/api/category/', data, format='json')
        
        data_product = {    
                        "name": "Soap",
                        "price": 1.00,
                        "qty": 5,
                        "out_of_stock": False,
                        "category": [1]
                        }
        
        self.client.post('/api/product/', data_product, format='json')
        
        response = self.client.get('/api/product/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_a_product(self):
        user = User.objects.create_user('test', 'test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
             
        data = {'name': 'Bath'}
        self.client.post('/api/category/', data, format='json')
        
        data_product = {    
                "name": "Shampoo",
                "price": 1.00,
                "qty": 5,
                "out_of_stock": False,
                "category": [1]
                }
        
        self.client.post('/api/product/', data_product, format='json')
        
        response = self.client.get('/api/product/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_update_product(self):
        user = User.objects.create_user('test', 'test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
        
        data_category = {'name': 'Bath'}
        self.client.post('/api/category/', data_category, format='json')
        
        data_product = {    
                "name": "Soap",
                "price": 1.00,
                "qty": 5,
                "out_of_stock": False,
                "category": [1]
                }
        
        self.client.post('/api/product/', data_product, format='json')
        
        data_update = {    
                        "name": "Soap",
                        "price": 1.00,
                        "qty": 0,
                        "out_of_stock": True,
                        "category": [1]
                        }
        response = self.client.put('/api/product/1/', data_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_delete_product(self):
        user = User.objects.create_user('test', 'test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
             
        data_category = {'name': 'Bath'}
        self.client.post('/api/category/', data_category, format='json')
        
        data_product = {    
                "name": "Soap",
                "price": 1.00,
                "qty": 5,
                "out_of_stock": False,
                "category": [1]
                }
        
        self.client.post('/api/product/', data_product, format='json')
        response = self.client.delete('/api/product/1', format='json')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)