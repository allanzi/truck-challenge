from app.tests import set_up
import unittest
import json

class TestUser(unittest.TestCase):

    def setUp(self):
        self.app = set_up.app.test_client()
        self.notFoundMessage = 'This user does not exists!'
        self.id = ''
        self.mockCreateData = {
            'age': 20,
            'driver_license_type': 'B',
            'has_vehicle': True,
            'is_busy': False,
            'name': 'Badah',
            'vehicle_type_id': 1
        }
        self.mockUpdateData = {
            'age': 30,
            'driver_license_type': 'D',
            'has_vehicle': False,
            'is_busy': True,
            'name': 'Badah Badah',
            'vehicle_type_id': 2
        }
        self.validKeys = [
            'age',
            'created_at',
            'driver_license_type',
            'has_vehicle',
            'id',
            'is_active',
            'is_busy',
            'name',
            'updated_at',
            'vehicle_type_id'
        ]

    def test_create_and_update_and_delete(self):
        response = self.app.post('/api/users', json={})
        responseData = json.loads(response.data.decode('utf-8'))
        validatonError = {
            'errors': {
                'age': ['Missing data for required field.'],
                'driver_license_type': ['Missing data for required field.'],
                'has_vehicle': ['Missing data for required field.'],
                'is_busy': ['Missing data for required field.'],
                'name': ['Missing data for required field.'],
                'vehicle_type_id': ['Missing data for required field.']
            }, 'message': 'Bad request!'
        }
        
        self.assertEqual(400, response.status_code)
        self.assertEqual(validatonError, responseData)
        
        response = self.app.post('/api/users', json=self.mockCreateData)
        responseData = json.loads(response.data.decode('utf-8'))['data']
        self.id = responseData['id']
        
        self.assertEqual(201, response.status_code)
        self.assertEqual(self.validKeys, list(responseData.keys()))

        response = self.app.put('/api/users/' + self.id, json=self.mockUpdateData)
        responseData = json.loads(response.data.decode('utf-8'))['data']

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.mockUpdateData['age'], responseData['age'])
        self.assertEqual(self.mockUpdateData['driver_license_type'], responseData['driver_license_type'])
        self.assertEqual(self.mockUpdateData['has_vehicle'], responseData['has_vehicle'])
        self.assertEqual(self.mockUpdateData['is_busy'], responseData['is_busy'])
        self.assertEqual(self.mockUpdateData['name'], responseData['name'])
        self.assertEqual(self.mockUpdateData['vehicle_type_id'], responseData['vehicle_type_id'])

        response = self.app.delete('/api/users/' + self.id)

        self.assertEqual(204, response.status_code)

    def test_reports(self):
        response = self.app.get('/api/reports/bused-users')
        responseData = json.loads(response.data.decode('utf-8'))['data'][0]
        
        self.assertEqual(200, response.status_code)
        self.assertEqual(self.validKeys, list(responseData.keys()))
        
        response = self.app.get('/api/reports/users-has-vehicle')
        responseData = json.loads(response.data.decode('utf-8'))['data'][0]
        
        self.assertEqual(200, response.status_code)
        self.assertEqual(self.validKeys, list(responseData.keys()))

    def test_list_and_show_users(self):
        response = self.app.get('/api/users')
        responseData = json.loads(response.data.decode('utf-8'))['data'][0]
        
        self.assertEqual(200, response.status_code)
        self.assertEqual(self.validKeys, list(responseData.keys()))

        response = self.app.get('/api/users/'+responseData['id'])
        responseData = json.loads(response.data.decode('utf-8'))['data']

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.validKeys, list(responseData.keys()))

    def test_not_found(self):
        response = self.app.get('/api/users/5e8790ffd17e430aad038a0c')
        responseData = json.loads(response.data.decode('utf-8'))

        self.assertEqual(404, response.status_code)
        self.assertEqual(self.notFoundMessage, responseData['message'])
        
        response = self.app.put('/api/users/5e8790ffd17e430aad038a0c', json={})
        responseData = json.loads(response.data.decode('utf-8'))

        self.assertEqual(404, response.status_code)
        self.assertEqual(self.notFoundMessage, responseData['message'])
        
        response = self.app.delete('/api/users/5e8790ffd17e430aad038a0c')
        responseData = json.loads(response.data.decode('utf-8'))

        self.assertEqual(404, response.status_code)
        self.assertEqual(self.notFoundMessage, responseData['message'])
