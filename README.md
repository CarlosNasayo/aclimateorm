# ORM ACLIMATE

![GitHub release (latest by date)](https://img.shields.io/github/v/release/CIAT-DAPA/aclimate_orm) ![](https://img.shields.io/github/v/tag/CIAT-DAPA/aclimate_orm)

## Features

- Built using Mongoengine for MongoDB
- Supports Python 3.x

## Getting Started

To use this Models, it is necessary to have an instance of MongoDB running.

### Prerequisites

- Python 3.x
- MongoDB

## Usage

This ORM can be used as a library in other Python projects. The models are located in the my_orm/models folder, and can be imported like any other Python module. To install this orm as a library you need to execute the following command:

````bash
pip install git+https://github.com/CIAT-DAPA/aclimate_orm
````

If you want to download a specific version of orm you can do so by indicating the version tag (@v0.0.0) at the end of the install command 

````bash
pip install git+https://github.com/CIAT-DAPA/aclimate_orm@v0.2.0
````

## Test
````bash
python -m unittest discover -s ./src/tests/ -p 'test_*.py'
````

## Models

### Users

Represents a User in the database.

Attributes:

- id: `ObjectId` - Id of the user.
- Username: `str` - User's username.
- NormalizedUserName: `str` - Normalized username.
- Email: `str` - User's email address.
- NormalizedEmail: `str` - Normalized email address.
- EmailConfirmed: `bool` - Indicates whether the user's email has been confirmed. Default is False.
- PasswordHash: `str` - Hashed password for the user.
- SecurityStamp: `str` - A random value that should change whenever a user's credentials have changed.
- ConcurrencyStamp: `str` - A value used for optimistic concurrency, ensuring updates are not based on stale data.
- PhoneNumber: `str` - User's phone number.
- PhoneNumberConfirmed: `bool` - Indicates whether the user's phone number has been confirmed. Default is False.
- TwoFactorEnabled: `bool` - Indicates whether two-factor authentication is enabled for the user. Default is False.
- LockoutEnd: `str` - Date and time in string format when the user's lockout period will end.
- LockoutEnabled: `bool` - Indicates whether lockout is enabled for the user. Default is True.
- AccessFailedCount: `int` - Number of failed access attempts.
- AuthenticatorKey: `str` - Key used for two-factor authentication.
- Roles: `List` - List of roles assigned to the user.
- Claims: `List` - List of claims associated with the user.
- Logins: `List` - List of external logins linked to the user.
- Tokens: `List` - List of tokens associated with the user.
- RecoveryCodes: `List` - List of recovery codes for two-factor authentication recovery.

Methods:

- `save()`: Saves the User object to the database.
- `delete()`: Deletes the User object from the database.

### Roles

Represents a Rol entry in the database.

Attributes:
- _id: `StringField` - Id of the user. (Primary Key)
- Name: `StringField` - User's name. (Required)
- NormalizedName: `StringField` - Normalized name.
- ConcurrencyStamp: `StringField` - A value used for optimistic concurrency, ensuring updates are not based on stale data. (Required)

Methods:

- `save()`: Saves the Rol object to the database.
- `delete()`: Deletes the Rol object from the database.

