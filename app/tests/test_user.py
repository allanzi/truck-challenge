from app.tests import set_up
import unittest

class TestUser(unittest.TestCase):

    def setUp(self):
        self.app = set_up.app.test_client()

    def test_not_found_in_find_user_route(self):
        # arrange
        response = self.app.get('/api/users/badah')

        # act
        responseData = eval(response.data.decode('utf-8'))

        # assert
        self.assertEqual(404, response.status_code)
        self.assertEqual('This user does not exists!', responseData['message'])