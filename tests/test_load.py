import sys
sys.path.append('.')
#from src.extract import read_data_from_s3
from src.transform import transform_rows, transform_row
from src.persistance import query, update, connect_to_rds
from src.load import load_location_row
import uuid
import unittest
from unittest import TestCase
from unittest.mock import Mock, patch


data = [
            1601539200, 
            'Isle of Wight', 
            [
                {'size': '', 'name': 'Mocha', 'price': '2.3'}, 
                {'size': '', 'name': 'Speciality Tea - Fruit', 'price': '1.3'}, 
                {'size': '', 'name': 'Flavoured iced latte - Vanilla', 'price': '2.75'}, 
                {'size': '', 'name': 'Frappes - Chocolate Cookie', 'price': '2.75'}, 
                {'size': 'Large', 'name': 'Filter coffee', 'price': '1.8'}
                ], 
                'CARD', 
                '10.90'
                ]

class TestLoad(unittest.TestCase):
    
    
   # @mock.patch('src.load.update', return_value = None)
   # @mock.patch('src.load.query', return_value = [])
    @patch('uuid.uuid4', return_value = '123456')
    def test_load_location_row(self, mock_uuid):
        #self.checkDbQuery = f"""SELECT id from Location WHERE l_name ='{self.location_name}'"""
        #check = query(self.checkDbQuery)
        #assert mock_output.return_value == []
        mock_query = Mock()
        mock_update = Mock()

        mock_query.return_value = []
        mock_update.return_value = None

        expected = '123456'
        actual = load_location_row(data, mock_query, mock_update)
        
        mock_update.assert_called()
        mock_update.assert_called_once()
        mock_update.assert_called_with("INSERT INTO Location (id, l_name) VALUES (%s, %s)", ('12345', 'Isle of Wight'))

        mock_query.assert_called()
        mock_query.assert_called_once()

        self.assertEqual(expected, actual)
        

    

    def test_load_transaction_row(self):
        pass

    def test_load_product_row(self):
        pass

    def test_load_by_row(self):
        pass



#     def setUp(self):
#         self.l_id = None
#         self.location_name = 'London'
        
#     def tearDown(self):
#         pass
    
#     @mock.patch('src.persistance.update')
#     @mock.patch('src.persistance.query')
#     def test_load_location_row(self, mock_query, mock_update):
#         # Arrange
#         mock
#         #checkDbQuery = f"""SELECT id from Location WHERE l_name ='{self.location_name}'"""
#         #updateDbQuery = "INSERT INTO Location (id, l_name) VALUES (%s, %s)"
#         mock_query.return_value = []
        
#         # Act        

#         if len(check) == 0:
#             self.l_id = str(uuid.uuid4())
#             # self.l_id += 'morestringcharacters'
#             mock_update(updateDbQuery, (self.l_id, self.location_name))
#         else:
#             self.l_id = check[0][0]

#         # Assert
#         expected = 36
#         actual = len(self.l_id)
        
#         self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()