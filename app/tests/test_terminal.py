from app.tests import set_up
import unittest
import json

class TestTerminal(unittest.TestCase):

    def setUp(self):
        self.app = set_up.app.test_client()

        response = self.app.get('/api/users')
        responseData = json.loads(response.data.decode('utf-8'))['data'][0]

        self.mockCreateData = {
            'user_id': responseData['id'],
            'is_busy': True
        }
        self.validKeys = [
            'created_at',
            'id',
            'is_active',
            'is_busy',
            'updated_at',
            'user_id'
        ]

    def test_create(self):
        response = self.app.post('/api/terminals', json={})
        responseData = json.loads(response.data.decode('utf-8'))
        validatonError = {
            'errors': {
                'user_id': ['Missing data for required field.'],
                'is_busy': ['Missing data for required field.'],
            }, 'message': 'Bad request!'
        }
        
        self.assertEqual(400, response.status_code)
        self.assertEqual(validatonError, responseData)
        
        response = self.app.post('/api/terminals', json=self.mockCreateData)
        responseData = json.loads(response.data.decode('utf-8'))['data']
        
        self.assertEqual(201, response.status_code)
        self.assertEqual(self.validKeys, list(responseData.keys()))

    def test_report(self):
        response = self.app.get('/api/reports/terminals')
        responseData = json.loads(response.data.decode('utf-8'))['data']
        
        self.assertEqual(200, response.status_code)
        self.assertEqual(['daily', 'monthly', 'weekly'], list(responseData.keys()))
        self.assertEqual(['date', 'trucks'], list(responseData['daily'][0].keys()))
        self.assertEqual(['month', 'trucks'], list(responseData['monthly'][0].keys()))
        self.assertEqual(['trucks', 'week'], list(responseData['weekly'][0].keys()))