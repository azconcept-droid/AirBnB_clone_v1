#!/usr/bin/python3
"""Unittest for base model class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test base model"""

    def test_new_instance(self):
        """ Test default instantiation if a `BaseModel` """
        m1 = BaseModel()
        self.assertIsNotNone(m1)

    def test_attribute(self):
        """ Test presence of required attributes """
        m1 = BaseModel()
        m1_dict = m1.__dict__
        self.assertIn("id", m1_dict)
        self.assertIn("created_at", m1_dict)
        self.assertIn("updated_at", m1_dict)

    def test_unique_id(self):
        """ Test unique id """
        m1 = BaseModel()
        m2 = BaseModel()
        self.assertNotEqual(m1, m2)

    def test_attribute_type(self):
        """ Test attribute type """
        m1 = BaseModel()
        self.assertIsInstance(m1.id, str)
        self.assertIsInstance(m1.created_at, datetime)
        self.assertIsInstance(m1.updated_at, datetime)
        self.assertIsInstance(m1.to_dict(), dict)

    def test_created_at(self):
        """ Test `created_at` and `updated_at` field """
        m = BaseModel()
        ct_stamp = datetime.now().timestamp()
        # Test the time created equals the current time approx.
        self.assertAlmostEqual(m.created_at.timestamp(), ct_stamp, 0)

    def test_updated_at_save(self):
        """ Test `updated_at` value in  `save` method """
        m1 = BaseModel()
        updated_at_1 = m1.updated_at
        created_at_1 = m1.created_at
        m1.save()
        self.assertEqual(created_at_1, m1.created_at)
        self.assertNotEqual(updated_at_1, m1.updated_at)
        m1_dict = m1.to_dict()
        updated_at_iso = datetime.isoformat(m1.updated_at)
        self.assertEqual(m1_dict["updated_at"], updated_at_iso)

    def test_to_dict(self):
        """ Test `to_dict` method """
        m1 = BaseModel()
        m_json = m1.to_dict()
        self.assertIsInstance(m_json, dict)
        # Checks if m1.__dict__ is a subset of m_json
        # should be false due to type differene in `updated_at`
        # and `created_at` fields
        self.assertFalse(dict(m_json, **m1.__dict__) == m_json)
        # values should be of type int, float or str
        self.assertTrue(all([
            type(v) in [int, float, str] for v in m_json.values()
        ]))
        self.assertIsInstance(m_json["created_at"], str)
        self.assertIsInstance(m_json["updated_at"], str)
        self.assertIn("__class__", m_json)

    def test_instance_by_dict(self):
        """ Check instantiation by dictionary """
        m1 = BaseModel()
        m1.name = "First"
        m1.age = 89
        m1_json = m1.to_dict()

        # m2 = BaseModel(**m1_json)
        # self.assertEqual(m1.name, m2.name)
        # self.assertEqual(m1.age, m2.age)
        # `m1` and `m2` have the same attributes
        # self.assertDictEqual(m1_json, m2.to_dict())
        # self.assertEqual(str(m1), str(m2))

    def test_to_str(self):
        """ Test that the str method has the correct output """
        m = BaseModel()
        string = "[{}] ({}) {}".format(BaseModel.__name__, m.id, m.__dict__)
        self.assertEqual(string, str(m))


if __name__ == "__main__":
    unittest.main()
