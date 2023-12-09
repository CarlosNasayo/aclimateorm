import sys
import unittest
import os
import mongomock
from mongoengine import *
dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)
from aclimate_orm.models.roles import Roles

class TestRol(unittest.TestCase):

    def setUp(self):
        disconnect()
        connect('mongoenginetest', host='mongodb://localhost', mongo_client_class=mongomock.MongoClient)

 
        self.rol = Roles(
            Name='name',
            NormalizedName='NormalizedName',
            ConcurrencyStamp='9d2c6cbe-f6e9-42d2-b7ae-d4a8f65c4d96',
        )

    def tearDown(self):
        
        self.rol.delete()
    def test_create_rol(self):

        self.rol.save()
        self.assertIsNotNone(self.rol._id)


        rol = Roles.objects(_id=self.rol._id).first()
        self.assertEqual(rol.Name, 'name')
        self.assertEqual(rol.NormalizedName, 'NormalizedName')
        self.assertEqual(rol.ConcurrencyStamp, '9d2c6cbe-f6e9-42d2-b7ae-d4a8f65c4d96')
        #coment for merge

if __name__ == '__main__':
    unittest.main()