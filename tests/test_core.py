import unittest
from deployscope import group
class Tests(unittest.TestCase):
 def test_group(self): self.assertEqual(group([{'name':'api','environment':'prod'},{'name':'web','environment':'prod'}]),{'prod':['api','web']})
if __name__=='__main__': unittest.main()
