"""

Run this test file outside of hfsharpness folder. Using:

	python -m unittest hfsharpness.tests.import_trainer_args_test

or

Run this test file from hfsharpness dir. Using:
	python tests/import_trainer_args_test.py

"""

import unittest

class TestImportSiblingFiles(unittest.TestCase):
	def test_import_from_outside_hfsharpness_dir(self):
		import sys
		sys.path.append("..")
		try:
			from hfsharpness.nlpsharpness import BaseTrainer, TrainingArguments
			from hfsharpness.nlpsharpness.sharpness import SAM
			from hfsharpness.nlpsharpness.hessian import HFHessian
		except Exception as e:
			print(f'Exception thrown is: {e}')
			raise e

if __name__ == "__main__":
    unittest.main()