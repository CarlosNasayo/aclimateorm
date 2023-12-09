import sys
import unittest
import os
import mongomock
from mongoengine import *
dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)
from aclimate_orm.models.users import Users

class TestUser(unittest.TestCase):

    def setUp(self):
        disconnect()
        connect('mongoenginetest', host='mongodb://localhost', mongo_client_class=mongomock.MongoClient)

 
        self.user = Users(
            UserName='name',
            NormalizedUserName='Normalized',
            Email='email@mail.com',
            NormalizedEmail='normalized@email.com',
            EmailConfirmed=True,
            PasswordHash='hashed_password',
            SecurityStamp='security_stamp',
            ConcurrencyStamp='concurrency_stamp',
            PhoneNumber='123456789',
            PhoneNumberConfirmed=True,
            TwoFactorEnabled=True,
            LockoutEnd='2023-12-31T00:00:00',
            LockoutEnabled=True,
            AccessFailedCount=2,
            AuthenticatorKey='authenticator_key',
            Roles=['role1', 'role2'],
            Claims=['claim1', 'claim2'],
            Logins=['login1', 'login2'],
            Tokens=['token1', 'token2'],
            RecoveryCodes=['recovery_code1', 'recovery_code2']
        )

    def tearDown(self):
        
        self.user.delete()
    def test_create_user(self):

        self.user.save()
        self.assertIsNotNone(self.user._id)


        user = Users.objects(_id=self.user._id).first()
        self.assertEqual(user.UserName, 'name')
        self.assertEqual(user.NormalizedUserName, 'Normalized')
        self.assertEqual(user.Email, 'email@mail.com')
        self.assertEqual(user.NormalizedEmail, 'normalized@email.com')
        self.assertTrue(user.EmailConfirmed)
        self.assertEqual(user.PasswordHash, 'hashed_password')
        self.assertEqual(user.SecurityStamp, 'security_stamp')
        self.assertEqual(user.ConcurrencyStamp, 'concurrency_stamp')
        self.assertEqual(user.PhoneNumber, '123456789')
        self.assertTrue(user.PhoneNumberConfirmed)
        self.assertTrue(user.TwoFactorEnabled)
        self.assertEqual(user.LockoutEnd, '2023-12-31T00:00:00')
        self.assertTrue(user.LockoutEnabled)
        self.assertEqual(user.AccessFailedCount, 2)
        self.assertEqual(user.AuthenticatorKey, 'authenticator_key')
        self.assertListEqual(user.Roles, ['role1', 'role2'])
        self.assertListEqual(user.Claims, ['claim1', 'claim2'])
        self.assertListEqual(user.Logins, ['login1', 'login2'])
        self.assertListEqual(user.Tokens, ['token1', 'token2'])
        self.assertListEqual(user.RecoveryCodes, ['recovery_code1', 'recovery_code2'])

if __name__ == '__main__':
    unittest.main()