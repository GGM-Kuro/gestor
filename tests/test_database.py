import copy
import unittest
import database as db

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
        self.assertNotEqual(client_to_modify.name,db.Clients.search('13D').name)

    def test_delete_client(self):
        deleted_client = db.Clients.delete('13D')
        lost_client = db.Clients.search('13D')
        self.assertEqual(deleted_client.dni,'13D')
        self.assertIsNone(lost_client)
