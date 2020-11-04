import sys
sys.path.append('.')
from src.extract import read_data_from_s3
from src.transform import transform_rows, transform_row
from src.persistance import query, update, connect_to_rds
import uuid
import unittest
from unittest import TestCase, mock

class TestLoad(unittest.TestCase):
    def setUp(self):
        self.l_id = None
        self.location_name = 'London'
        
    def tearDown(self):
        pass
    
    @mock.patch('src.persistance.update')
    @mock.patch('src.persistance.query')
    def test_load_location_row(self, mock_query, mock_update):
        # Arrange
        checkDbQuery = f"""SELECT id from Location WHERE l_name ='{self.location_name}'"""
        updateDbQuery = "INSERT INTO Location (id, l_name) VALUES (%s, %s)"
        mock_query.return_value = []
        
        # Act        

        if len(check) == 0:
            self.l_id = str(uuid.uuid4())
            # self.l_id += 'morestringcharacters'
            mock_update(updateDbQuery, (self.l_id, self.location_name))
        else:
            self.l_id = check[0][0]

        # Assert
        expected = 36
        actual = len(self.l_id)
        
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()