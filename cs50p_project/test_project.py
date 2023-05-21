from project import retrieve_one , retrieve_all, delete_one, delete_all, add, update
from pytest import raises
import csv
from cryptography.fernet import Fernet


"""secrets.csv must be deleted before running the tests"""

def test_add():
    # the key is the same as the one in project.py
    key = b'6wFxOLQxDXvi5UqeIzJ9886-23geqARprsLSSBqJ82Q='
    f = Fernet(key)
    assert add(f,"netflix","alinasserelden@hotmail.com","ali123") == True
    assert add(f,"stackoverflow","alinasserelden@hotmail.com","ali123") == True
    # cannot add a repeated record
    # Note : repeated record is detected by the site name and the account (together)
    # the next line should return False as the record is repeated
    assert add(f,"netflix","alinasserelden@hotmail.com","ali123") == False
    # check if the records are added to the file
    with open ("secrets.csv","r") as file:
        reader = csv.DictReader(file)
        assert len(list(reader)) == 2

def test_update():
    key = b'6wFxOLQxDXvi5UqeIzJ9886-23geqARprsLSSBqJ82Q='
    f = Fernet(key)
    # update a record
    assert update(f,"netflix","alinasserelden@hotmail.com","newpassword") == True
    assert update(f,"slack","alinasserelden@hotmail.com","newpassword") == False




def test_retrieve_all():
    key = b'6wFxOLQxDXvi5UqeIzJ9886-23geqARprsLSSBqJ82Q='
    f = Fernet(key)
    assert retrieve_all(f) == True


def test_retrieve_one():
    key = b'6wFxOLQxDXvi5UqeIzJ9886-23geqARprsLSSBqJ82Q='
    f = Fernet(key)
    # retrieve a record with a right site name and a right account
    assert retrieve_one(f,"netflix","alinasserelden@hotmail.com") == True
    # retrieve a record with a right account but wrong site name
    assert retrieve_one(f,"slack","alinasserelden@hotmail.com") == False

def test_delete_one():
    # delete one record
    assert delete_one("netflix","alinasserelden@hotmail.com") == True
    # delete a with a right site name but wrong account
    assert delete_one("stackoverflow","ali") == False
    # delete a record with a wrong site name and a right account
    assert delete_one("slack","alinasserelden@hotmail.com") == False

    # check if the record is deleted from the file
    with open ("secrets.csv","r") as file:
        reader = csv.DictReader(file)
        assert len(list(reader)) == 1

def test_delete_all():
    # delete all records
    assert delete_all() == True
    # no records to delete
    assert delete_all() == False

