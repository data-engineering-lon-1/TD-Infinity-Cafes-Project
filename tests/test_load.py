import sys
sys.path.append('.')
from src.transform import transform_rows, transform_row
from src.persistance import query, update, connect_to_rds
from src.load import load_location_row, load_transaction_row, load_by_row, load_product_row
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
    def setUp(self):
        self.t_data = [[1604599325, 'Horwich Green', [{'size': '', 'name': 'Glass of milk', 'price': '0.7'}, {'size': '', 'name': 'Glass of milk', 'price': '0.7'}, {
            'size': 'Large', 'name': 'Flavoured hot chocolate - Vanilla', 'price': '2.9'}], 'CASH', '4.30']]

    @patch('uuid.uuid4', return_value='123456')
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

        mock_update.assert_called_once()
        mock_update.assert_called_with(
            "INSERT INTO Location (id, l_name) VALUES (%s, %s)", 
            (
                '123456', 
                'Isle of Wight'
                )
            )

        mock_query.assert_called()
        mock_query.assert_called_once()

        self.assertEqual(expected, actual)
        
    
    @patch('uuid.uuid4', return_value = '123456789')
    def test_load_transaction_row(self, mock_uuid):

        l_id = '123456'

        mock_update = Mock()
        mock_update.return_value = None

        expected = '123456789'
        actual = load_transaction_row(data, l_id, mock_update)

        mock_update.assert_called()
        mock_update.assert_called_with(
            "INSERT INTO Transactions (id, date_time, l_id, payment_type, total) VALUES (%s, %s, %s, %s, %s)", ('123456789', 1601539200, l_id, 'CARD', 10.9))

        self.assertEqual(expected, actual)


    @patch('uuid.uuid4', return_value = '9876')
    def test_load_product_row(self, mock_uuid):
        
        mock_query = Mock()
        mock_update = Mock()

        mock_query.return_value = None
        mock_update.return_value = None

        expected = {'9876': 2.3, '9876': 1.3, '9876': 2.75, '9876': 2.75,'9876': 1.8}
        actual = load_product_row(data, mock_query, mock_update)

        self.assertEqual(expected, actual)



    @patch('src.load.load_orders_row')
    @patch('src.load.load_product_row', return_value={'345': 3.5})
    @patch('src.load.load_transaction_row', return_value='234')
    @patch('src.load.load_location_row', return_value='123')
    def test_load_by_row(self, mock_location, mock_transaction, mock_product, mock_orders):
        
        load_by_row(self.t_data)

        mock_location.assert_called_with(self.t_data[0], query, update)
        mock_transaction.assert_called_with(self.t_data[0], '123', update)
        mock_product.assert_called_with(self.t_data[0])
        mock_orders.assert_called_with(1604599325, '234', '345', 3.5)


if __name__ == '__main__':
    unittest.main()
