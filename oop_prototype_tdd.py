import unittest

from oop_prototype_classes import Herbicide

class TddforHerbicideProject(unittest.TestCase):

	#def setUp(self):
	#	self.herbs = Herbicide()
	#	#self.pre = Preherbs()

	def test_string_entered_for_conc_value(self):
		self.herbs = Herbicide("Revolver", 0.19, 0.011875, 9)
		self.herbs.concUnits('liquid')
		x = self.herbs.calc_formulation_rate()
		#result = x.calc_formulation_rate()
		self.assertEqual(0.0625,x)
	