# tests/test_database.py
import pytest
from app.database import Database

@pytest.fixture
def db():
    database = Database(":memory:") # Use RAM for speed
    database.connect()
    yield database
    database.disconnect()
    

def test_add_user(db): 
    # Must have 3 arguments now!
    success = db.add_user("james", "user@example.com")
    assert success is True
def test_add_another_user(db): 
    # Must have 3 arguments now!
    db.add_user("james", "user@example.com")
    success = db.add_user("james", "user@example.com")
    assert success is False
    
def test_add_same_user(db):
    db.add_user("james", "user@example.com")
    # Act
    success = db.add_user("james", "user@example.com")
    # Assert
    assert success is False

def get_user(db):
    success = db.add_user("Toto le brave","user@example.com")
    assert success is True
    assert db.get_user("Toto le brave","user@example.com") == {"email": "user@example.com","username": "Toto le brave"}
def get_john_doe_user(db):

    assert db.get_user("Toto le brave","user@example.com") == None

def delete_user(db):
    
    # Act
    db.delete_user("james","user@example.com")
    # Assert
    
    assert db.get_user("james","user@example.com") == None
    
    
    

