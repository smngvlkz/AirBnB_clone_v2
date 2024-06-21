#!/usr/bin/python3
import unittest
import MySQLdb
from models.state import State

class TestDBStorage(unittest.TestCase):
    """Test the DB storage engine"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        # Connect to the MySQL database
        cls.db = MySQLdb.connect(host="localhost",
                                 user="hbnb_test",
                                 passwd="hbnb_test_pwd",
                                 db="hbnb_test_db")
        cls.cursor = cls.db.cursor()

    @classmethod
    def tearDownClass(cls):
        """Tear down the test"""
        cls.cursor.close()
        cls.db.close()

    def setUp(self):
        """Set up before each test"""
        self.db.autocommit(True)

    def tearDown(self):
        """Tear down after each test"""
        self.db.rollback()

    def test_create_state(self):
        """Test creating a new State"""
        initial_count = self.get_count()
        print(f"Initial count: {initial_count}")

        # Create a new State object
        new_state = State(name="California")
        new_state.save()

        new_count = self.get_count()
        print(f"New count: {new_count}")

        # Assert that the number of records increased by 1
        self.assertEqual(new_count, initial_count + 1)

    def get_count(self):
        """Helper method to get the count of states in the database"""
        self.cursor.execute("SELECT COUNT(*) FROM states")
        count = self.cursor.fetchone()[0]
        return count

if __name__ == "__main__":
    unittest.main()
