#!/usr/bin/python3
""" Unit tests for the HBNBCommand class """
import unittest
from io import StringIO
from unittest.mock import patch
import sys
import os

# Append the path to the directory containing console.py
sys.path.append(os.path.abspath('..'))

from console import HBNBCommand
from models import storage
from models.state import State
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.review import Review


class TestHBNBCommand(unittest.TestCase):
    """Unit tests for HBNBCommand class"""

    def setUp(self):
        """Set up for tests"""
        self.console = HBNBCommand()
        # Reset the storage before each test
        storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after tests"""
        storage._FileStorage__objects = {}

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State name="California"')
            state_id = f.getvalue().strip()
            self.assertIn('State.' + state_id, storage.all())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
            place_id = f.getvalue().strip()
            self.assertIn('Place.' + place_id, storage.all())

    def test_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State name="Texas"')
            state_id = f.getvalue().strip()
            self.console.onecmd('show State {}'.format(state_id))
            output = f.getvalue().strip()
            self.assertIn(state_id, output)

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State name="Nevada"')
            state_id = f.getvalue().strip()
            self.console.onecmd('destroy State {}'.format(state_id))
            self.assertNotIn('State.' + state_id, storage.all())

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State name="Ohio"')
            self.console.onecmd('create State name="Oregon"')
            self.console.onecmd('all State')
            output = f.getvalue().strip()
            self.assertIn('[State]', output)

    def test_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State name="Washington"')
            state_id = f.getvalue().strip()
            self.console.onecmd(f'update State {state_id} name "New Washington"')
            self.console.onecmd(f'show State {state_id}')
            output = f.getvalue().strip()
            self.assertIn('New Washington', output)

    def test_count(self):
        """Test count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State name="Alaska"')
            self.console.onecmd('create State name="Hawaii"')
            f.truncate(0)
            f.seek(0)
            self.console.onecmd('count State')
            output = f.getvalue().strip()
            self.assertEqual(int(output), 2)


if __name__ == "__main__":
    unittest.main()
