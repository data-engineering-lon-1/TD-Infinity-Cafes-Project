import unittest
from src.transform import transform_row, transform_rows
import time
import numpy as np

class TestTransfom(unittest.TestCase):

    def setUp(self):
        self.raw_data_1 = [
            '2020-10-01 09:00:00',
            'Isle of Wight',
            'John Whitmire',
            ",Mocha,2.3,,Speciality Tea - Fruit,1.3,,Flavoured iced latte - Vanilla,2.75,,Frappes - Chocolate Cookie,2.75,Large,Filter coffee,1.8",
            'CARD','10.90',
            "americanexpress,379663269694145"
            ]

        self.raw_data_2 = [
            '2020-10-01 09:01:00',
            'Isle of Wight',
            'Sarah Perea',
            "Large,Americano,2.25,Regular,Americano,1.95,,Flavoured iced latte - Caramel,2.75",
            'CASH',
            '6.95',
            'None'
            ]
        
        self.raw_data_grouped = [
            [
                '2020-10-01 09:06:00',
                'Isle of Wight',
                'Roberto Hawn',
                "Large,Flavoured hot chocolate - Caramel,2.9,Regular,Flavoured hot chocolate - Hazelnut,2.6,Large,Flavoured latte - Gingerbread,2.85,,Red Label tea,1.2,,Flat white,2.15",
                'CARD',
                '11.70',
                "visa16,45371194845127210"
                ],
            [
                '2020-10-01 09:07:00',
                'Isle of Wight',
                'John Wilkes',
                "Large,Hot chocolate,2.9,,Frappes - Chocolate Cookie,2.75,Regular,Flavoured hot chocolate - Vanilla,2.6,Large,Flavoured latte - Gingerbread,2.85,,Frappes - Chocolate Cookie,2.75",
                'CARD',
                '13.85',
                "visa16,4449175651794936"
                ],
            [
                '2020-10-01 09:08:00',
                'Isle of Wight',
                'Andrew Sims',
                "Large,Luxury hot chocolate,2.7,Regular,Filter coffee,1.5,Large,Flavoured hot chocolate - Hazelnut,2.9",
                'CASH',
                '7.10',
                "None"
                ]
                        
                    ]

    def test_transform_row(self):
        
        expected_1 = [
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

        expected_2 = [
            1601539260, 
            'Isle of Wight', 
            [
                {'size': 'Large', 'name': 'Americano', 'price': '2.25'}, 
                {'size': 'Regular', 'name': 'Americano', 'price': '1.95'}, 
                {'size': '', 'name': 'Flavoured iced latte - Caramel', 'price': '2.75'}
                ], 
                'CASH', 
                '6.95'
                ]

        actual_1 = transform_row(self.raw_data_1)
        actual_2 = transform_row(self.raw_data_2)

        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)

    def test_transform_rows(self):

        expected = [
            [
                1601539560,
                'Isle of Wight',
                [
                    {'size': 'Large', 'name': 'Flavoured hot chocolate - Caramel', 'price': '2.9'}, 
                    {'size': 'Regular', 'name': 'Flavoured hot chocolate - Hazelnut', 'price': '2.6'}, 
                    {'size': 'Large', 'name': 'Flavoured latte - Gingerbread', 'price': '2.85'}, 
                    {'size': '', 'name': 'Red Label tea', 'price': '1.2'}, 
                    {'size': '', 'name': 'Flat white', 'price': '2.15'}
                    ], 
                 'CARD', 
                 '11.70'
                 ], 
            [
                1601539620, 
                'Isle of Wight', 
                [
                    {'size': 'Large', 'name': 'Hot chocolate', 'price': '2.9'}, 
                    {'size': '', 'name': 'Frappes - Chocolate Cookie', 'price': '2.75'}, 
                    {'size': 'Regular', 'name': 'Flavoured hot chocolate - Vanilla', 'price': '2.6'}, 
                    {'size': 'Large', 'name': 'Flavoured latte - Gingerbread', 'price': '2.85'}, 
                    {'size': '', 'name': 'Frappes - Chocolate Cookie', 'price': '2.75'}
                    ], 
                'CARD', 
                '13.85'
                ], 
            [   
                1601539680, 
                'Isle of Wight', 
                [
                    {'size': 'Large', 'name': 'Luxury hot chocolate', 'price': '2.7'}, 
                    {'size': 'Regular', 'name': 'Filter coffee', 'price': '1.5'}, 
                    {'size': 'Large', 'name': 'Flavoured hot chocolate - Hazelnut', 'price': '2.9'}
                    ], 
                'CASH', 
                '7.10'
                ]
                    ]

        actual = transform_rows(self.raw_data_grouped)

        self.assertEqual(expected,actual)


if __name__ == '__main__':
    unittest.main()