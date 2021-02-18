import unittest
from functions import *

#---------------------------------------------------------------q1
# ep: -15(invalid), 15(valid), 60(invalid)
# bva: 0(invalid), 1(valid), 31(valid), 32(invalid)
class TestValidQ1(unittest.TestCase):
  def test_equiPartition(self):
    self.assertEqual(q1(15), "good")

  def test_BVA(self):
    self.assertEqual(q1(1), "good")
    self.assertEqual(q1(31), "good")

class TestInvalidQ1(unittest.TestCase):
  def test_equiPartition(self):
    self.assertEqual(q1(-15), "bad")
    self.assertEqual(q1(60), "bad")

  def test_BVA(self):
    self.assertEqual(q1(0), "bad")
    self.assertEqual(q1(32), "bad")

#---------------------------------------------------------------q2
# ep: ""(invalid), "aaaaaaaa"(valid), "aaaaaaaaaaaaaaa"(invalid)
# bva: "aaaaaa"(invalid), "aaaaaaa"(valid), "aaaaaaaaaa"(valid), 
#      "aaaaaaaaaaa"(invalid)
class TestValidQ2(unittest.TestCase):  
  def test_equiPartition(self):
    self.assertEqual(q2("aaaaaaaa"), "good")
  
  def test_BVA(self):
    self.assertEqual(q2("aaaaaaa"), "good")
    self.assertEqual(q2("aaaaaaaaaa"), "good")

class TestInvalidQ2(unittest.TestCase):
  def test_equiPartition(self):
    self.assertEqual(q2(""), "bad")
    self.assertEqual(q2("aaaaaaaaaaaaaaa"), "bad")

  def test_BVA(self):
    self.assertEqual(q2("aaaaaa"), "bad")
    self.assertEqual(q2("aaaaaaaaaaa"), "bad")

#---------------------------------------------------------------q3
# ep: 10(invalid), 30(valid), 63(invalid), 67(valid), 90(invalid)
# bva: 15(invalid), 16(valid), 59(valid), 60(invalid), 65(invalid), 
#      66(valid), 70(valid), 71(invalid)
class TestValidQ3(unittest.TestCase):
  def test_equiPartition(self):
    self.assertEqual(q3(30), "good")
    self.assertEqual(q3(67), "good")

  def test_BVA(self):
    self.assertEqual(q3(16), "good")
    self.assertEqual(q3(59), "good")
    self.assertEqual(q3(66), "good")
    self.assertEqual(q3(70), "good")

class TestInvalidQ3(unittest.TestCase):
  def test_equiPartition(self):
    self.assertEqual(q3(10), "bad")
    self.assertEqual(q3(63), "bad")
    self.assertEqual(q3(90), "bad")

  def test_BVA(self):
    self.assertEqual(q3(15), "bad")
    self.assertEqual(q3(60), "bad")
    self.assertEqual(q3(65), "bad")
    self.assertEqual(q3(71), "bad")

if(__name__ == '__main__'):
  unittest.main(verbosity=2)