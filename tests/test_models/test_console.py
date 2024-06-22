#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.state import State
from models.place import Place

class TestHBNBCommand(unittest.TestCase):
    """Test the HBNBCommand class"""

    def setUp(self):
        """Set up the test environment"""
        storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up the test environment"""
        storage._FileStorage__objects = {}

    def test_create_no_class(self):
        """Test create with no class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class(self):
        """Test create with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_create_valid_class(self):
        """Test create with valid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State')
            state_id = f.getvalue().strip()
            self.assertIn("State." + state_id, storage.all().keys())

    def test_create_with_parameters(self):
        """Test create with parameters"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
            state_id = f.getvalue().strip()
            self.assertIn("State." + state_id, storage.all().keys())
            self.assertEqual(storage.all()["State." + state_id].name, "California")

    def test_create_multiple_parameters(self):
        """Test create with multiple parameters"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
            place_id = f.getvalue().strip()
            place = storage.all()["Place." + place_id]
            self.assertEqual(place.city_id, "0001")
            self.assertEqual(place.user_id, "0001")
            self.assertEqual(place.name, "My little house")
            self.assertEqual(place.number_rooms, 4)
            self.assertEqual(place.number_bathrooms, 2)
            self.assertEqual(place.max_guest, 10)
            self.assertEqual(place.price_by_night, 300)
            self.assertAlmostEqual(place.latitude, 37.773972)
            self.assertAlmostEqual(place.longitude, -122.431297)

    def test_create_with_invalid_parameters(self):
        """Test create with invalid parameters"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="New_York" invalid_param')
            state_id = f.getvalue().strip()
            state = storage.all()["State." + state_id]
            self.assertEqual(state.name, "New York")
            self.assertFalse(hasattr(state, "invalid_param"))

if __name__ == "__main__":
    unittest.main()
