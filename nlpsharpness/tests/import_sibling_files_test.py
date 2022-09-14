import unittest

class TestImportSiblingFiles(unittest.TestCase):
	def test_import(self):
		import sys
		sys.path.append("..")
		from hessian import HFHessian
		from sharpness import SAM