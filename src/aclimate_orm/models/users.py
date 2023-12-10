from mongoengine import Document, StringField, IntField, BooleanField, ListField
import uuid

class Users(Document):
    """
    Represents the Users in the database.

    Attributes:
    ----------
    _id: str
        Id of User. (Primary key) Required.
    UserName: str
        Username of User. Required.
    NormalizedUserName: str
        Normalized username of User. Optional.
    Email: str
        Email address of User. Required.
    NormalizedEmail: str
        Normalized email address of User. Optional.
    EmailConfirmed: bool
        Indicates whether the email address has been confirmed. Defaults to False.
    PasswordHash: str
        Hashed password of User. Optional.
    SecurityStamp: str
        Security stamp used to invalidate cached security information. Optional.
    ConcurrencyStamp: str
        Concurrency stamp for optimistic concurrency control. Optional.
    PhoneNumber: str
        Phone number of User. Optional.
    PhoneNumberConfirmed: bool
        Indicates whether the phone number has been confirmed. Defaults to False.
    TwoFactorEnabled: bool
        Indicates whether two-factor authentication is enabled. Defaults to False.
    LockoutEnd: str
        Date and time when the lockout period ends, formatted as a string. Optional.
    LockoutEnabled: bool
        Indicates whether lockout is enabled. Defaults to True.
    AccessFailedCount: int
        Number of failed access attempts. Defaults to 0.
    AuthenticatorKey: str
        Authenticator key used for two-factor authentication. Optional.
    Roles: list of str
        List of roles assigned to the user.
    Claims: list of str
        List of claims associated with the user.
    Logins: list of str
        List of external logins linked to the user.
    Tokens: list of str
        List of tokens associated with the user.
    RecoveryCodes: list of str
        List of recovery codes for two-factor authentication recovery.

    Methods:
    -------
    save()
        Saves the User object to the database.
    delete()
        Deletes the User object from the database.
    """
    meta = {
        'collection': 'Users'
    }
    _id = StringField(primary_key=True, default=str(uuid.uuid4()))
    UserName = StringField(required=True)
    NormalizedUserName = StringField()
    Email = StringField(required=True)
    NormalizedEmail = StringField()
    EmailConfirmed = BooleanField(default=False)
    PasswordHash = StringField()
    SecurityStamp = StringField()
    ConcurrencyStamp = StringField()
    PhoneNumber = StringField()
    PhoneNumberConfirmed = BooleanField(default=False)
    TwoFactorEnabled = BooleanField(default=False)
    LockoutEnd = StringField()
    LockoutEnabled = BooleanField(default=True)
    AccessFailedCount = IntField(default=0)
    AuthenticatorKey = StringField()
    Roles = ListField()
    Claims = ListField()
    Logins = ListField()
    Tokens = ListField()
    RecoveryCodes = ListField()


