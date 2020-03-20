#import unittest
import search

import io
import unittest
import unittest.mock

#from .solution import fizzbuzz

test_json1 = [{'active': "false", 'tags': ['1', '2']}, {'active': "true", 'tags': ['5', '6']}, {'active': "xyz", 'tags': ['2', '3']}]
test_json2 = [{'_id': 1, 'details': "null"}, {'_id': 2, 'details': "Temp Details"}, {'_id': 3, 'details': ""}]


class TestSearch(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    
    def test_json_search_list_values(self):
        results = search.search_json(test_json1,"tags","1")
        self.assertEqual(results, [{'active': "false", 'tags': ['1', '2']}])

    def test_json_search_boolean_values(self):
        results = search.search_json(test_json1,"active","false")
        self.assertEqual(results, [{'active': "false", 'tags': ['1', '2']}])

    def test_json_search_null_values(self):
        results = search.search_json(test_json2,"details","null")
        self.assertEqual(results, [{'_id': 1, 'details': "null"}])

    def test_json_search_int_values(self):
        results = search.search_json(test_json2,"_id","1")
        self.assertEqual(results, [{'_id': 1, 'details': "null"}])

#"active": false

#"details": null
if __name__ == '__main__':
    unittest.main()