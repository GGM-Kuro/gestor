import copy
import unittest

import database as db
import helpers


class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Clients.list=[
            db.Client('45H','Carlos','Rojas'),
            db.Client('13D','Juan','Perez'),
            db.Client('24J','Pedro','Lopez')
        ]

    def test_search_client(self):
        existing_client = db.Clients.search('13D')
        dont_existing_client = db.Clients.search('10D')
        self.assertIsNotNone(existing_client)
        self.assertIsNone(dont_existing_client)

    def test_create_client(self):
        new_client = db.Clients.create('13C','Carlos','Rojas')
        self.assertEqual(len(db.Clients.list),4)
        self.assertEqual(new_client.dni,'13C')
        self.assertEqual(new_client.name,'Carlos')
        self.assertEqual(new_client.last_name,'Rojas')

    def test_modify_client(self):
        client_to_modify = copy.copy( db.Clients.search('13D') )
        client_modified = db.Clients.modify('13D','Andres','Perez')
        # noqa: E999
        self.assertEqual(client_to_modify.name,'Juan') # pyright: ignore
        self.assertEqual(client_modified.name,'Andres') # pyright: ignore

    def test_delete_client(self):
        deleted_client = db.Clients.delete('13D')
        lost_client = db.Clients.search('13D')
        self.assertEqual(deleted_client.dni,'13D') # pyright: ignore
        self.assertIsNone(lost_client)

    def test_valid_dni(self):
        self.assertTrue(helpers.validate_dni('00A',db.Clients.list))
        self.assertFalse(helpers.validate_dni('213015u',db.Clients.list))
        self.assertFalse(helpers.validate_dni('45H',db.Clients.list))
