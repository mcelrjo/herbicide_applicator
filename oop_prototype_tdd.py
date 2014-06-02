import unittest

from oop_prototype_classes import Herbicide

class TddforHerbicideProject(unittest.TestCase):

	def setUp(self):
		self.herbs = Herbicide()
		#self.pre = Preherbs()

	def test_string_entered_for_conc_value(self):
		x = self.herbs.calc_formulation_rate("Revolver", 0.19, 0.011875, 90)
		#result = x.calc_formulation_rate()
		self.assertEqual(0.062,x)
	