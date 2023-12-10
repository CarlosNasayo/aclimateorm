from mongoengine import Document, StringField
import uuid

class Roles(Document):
    """
    Represents the Users in the database.

    Attributes:
    ----------
    _id: str
        Id of User. (Primary key) Required.
    Name: str
        Username of Rol. Required.
    NormalizedName: str
        Normalized Name of Rol. Optional.
    ConcurrencyStamp: str
        Attribute used to implement concurrency control. Required.
    
    Methods:
    -------
    save()
        Saves the Rol object to the database.
    delete()
        Deletes the Rol object from the database.
    """
    meta = {
        'collection': 'Roles'
    }
    _id = StringField(primary_key=True, default=str(uuid.uuid4()))
    Name = StringField(required=True)
    NormalizedName = StringField()
    ConcurrencyStamp = StringField(required=True)
    

