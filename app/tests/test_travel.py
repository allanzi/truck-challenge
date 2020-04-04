from app.tests import set_up
import unittest
import json

class TestTravel(unittest.TestCase):

    def setUp(self):
        self.app = set_up.app.test_client()
        self.notFoundMessage = 'This travel does not exists!'
        self.id = ''

        response = self.app.get('/api/users')
        responseData = json.loads(response.data.decode('utf-8'))['data'][0]

        self.mockCreateData = {
            'user_id': responseData['id'],
            'from_': {
                'latitude': -23.6370655,
                'longitude': -46.7147759,
            },
            'to': {
                'latitude': -23.6233618,
                'longitude': -46.7010292
            }
        }
        self.mockUpdateData = {
            'user_id': responseData['id'],
            'to': {
                'latitude': -23.6370655,
                'longitude': -46.7147759,
            },
            'from_': {
                'latitude': -23.6233618,
                'longitude': -46.7010292
            }
        }
        self.validKeys = [
            'created_at',
            'from',
            'id',
            'to',
            'updated_at',
            'user_id'
        ]

    def test_create_and_update_and_delete(self):
        response = self.app.post('/api/travels', json={})
        responseData = json.loads(response.data.decode('utf-8'))
        validatonError = {
            'errors': {
                'user_id': ['Missing data for required field.'],
                'from_': ['Missing data for required field.'],
                'to': ['Missing data for required field.'],
            }, 'message': 'Bad request!'
        }
        
        self.assertEqual(400, response.status_code)
        self.assertEqual(validatonError, responseData)
        
        response = self.app.post('/api/travels', json=self.mockCreateData)
        responseData = json.loads(response.data.decode('utf-8'))['data']
        self.id = responseData['id']
        
        self.assertEqual(201, response.status_code)
        self.assertEqual(self.validKeys, list(responseData.keys()))

        response = self.app.put('/api/travels/' + self.id, json=self.mockUpdateData)
        responseData = json.loads(response.data.decode('utf-8'))['data']

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.mockUpdateData['user_id'], responseData['user_id'])
        self.assertEqual(self.mockUpdateData['from_'], responseData['from'])
        self.assertEqual(self.mockUpdateData['to'], responseData['to'])

        response = self.app.delete('/api/travels/' + self.id)

        self.assertEqual(204, response.status_code)

    def test_reports(self):
        response = self.app.get('/api/reports/travels')
        responseData = json.loads(response.data.decode('utf-8'))['data'][0]
        
        self.assertEqual(['user_id'], list(responseData['_id'].keys()))
        self.assertEqual(['from', 'to'], list(responseData['travels'][0].keys()))
        self.assertEqual(['latitude', 'longitude'], list(responseData['travels'][0]['to'].keys()))
        self.assertEqual(['latitude', 'longitude'], list(responseData['travels'][0]['from'].keys()))

    def test_list_and_show_travels(self):
        response = self.app.get('/api/travels')
        responseData = json.loads(response.data.decode('utf-8'))['data'][0]
        
        self.assertEqual(200, response.status_code)
        self.assertEqual(self.validKeys, list(responseData.keys()))

        response = self.app.get('/api/travels/'+responseData['id'])
        responseData = json.loads(response.data.decode('utf-8'))['data']

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.validKeys, list(responseData.keys()))

    def test_not_found(self):
        response = self.app.get('/api/travels/5e8790ffd17e430aad038a0c')
        responseData = json.loads(response.data.decode('utf-8'))

        self.assertEqual(404, response.status_code)
        self.assertEqual(self.notFoundMessage, responseData['message'])
        
        response = self.app.put('/api/travels/5e8790ffd17e430aad038a0c', json={})
        responseData = json.loads(response.data.decode('utf-8'))
        validationError = {'errors': {'user_id': ['Must be a valid ObjectId or Not found.']}, 'message': 'Bad request!'}

        self.assertEqual(400, response.status_code)
        self.assertEqual(validationError, responseData)

        response = self.app.delete('/api/travels/5e8790ffd17e430aad038a0c')
        responseData = json.loads(response.data.decode('utf-8'))

        self.assertEqual(404, response.status_code)
        self.assertEqual(self.notFoundMessage, responseData['message'])
