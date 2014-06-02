
class Herbicide(object):
	"""The following establishes a class for herbicides
	which includes the concentration of the herbicide in lb ai/gal or %wt/wt, 
	the rate of the herbicide in lb ai/a, and the cost per acre at the given rate.
	Cost should be listed in cost per lb ai."""
	
	def __init__(self, name, concentration, ai_rate, cost):
		self.name = name
		self.conc = float(concentration)
		self.ai_rate = float(ai_rate)
		self.cost = float(cost)
		self.herbs = []
	
		"""Used to calculate the product rate."""
	def concUnits(self, formulation):
		self.form = formulation
		if self.form == "dry":
			print self.name, "is formulated as a", self.form
			print "Concentration is", self.conc, "% wt/wt."
		else:
			print self.name, "is formulated as a", self.form
			print "Concentration is a liquid in", self.conc, "lbs/gallon."
	
	def rateUnits(self):
		pass
		
	def insertHerb(self):
		self.herbs.append(self.name) 
	
	def getaiRate(self):
		print self.ai_rate, "lbs ai/a"
		
	def calc_formulation_rate(self):
		if self.form == "dry":
			lbs_per_acre = self.ai_rate/(self.conc/100)
			print self.name, "can be applied at", lbs_per_acre, "pounds per acre", \
			"which is equivalent to", self.ai_rate, "lbs ai per acre."
			return lbs_per_acre
		else:
			gal_per_acre = self.ai_rate/self.conc
			print self.name, "can be applied at", gal_per_acre, "pounds per acre", \
			"which is equivalent to", self.ai_rate, "lbs ai per acre."
			return gal_per_acre
		

		
#	def __str__(self):
#		print self.name

class Preherbs(Herbicide):
	""" Separation of preemergence herbicides primarily for the fact that 
	these type herbicides can be applied either as a liquid application or as a 
	granular-spreadable application. For application type enter 'spread' or 'spray'"""
	
	def applicationType(self, apptype):
		self.apptype = apptype

	def distinguish_application_method(self):
		if self.apptype == "spread":
			print self.name, "is a granular formulation and must be spread."
			lbs_per_acre = self.ai_rate/(self.conc/100)
			print self.name, "can be applied at", lbs_per_acre, "pounds per acre", \
			"which is equivalent to", self.ai_rate, "lbs ai per acre."
			return lbs_per_acre
		else:
			print name, "is a sprayable formulation and must be diluted in water."
			return self.calc_formulation_rate()


class Graminicides(Herbicide):
	"""Graminicides are only used for control of grass monocot plant species with 
	little to no toxicity to broadleaf plant species."""
	pass
	

	
class AuxinHerbs(Herbicide):
	"""Auxinic herbicides are the opposite of graminicides.  Auxinic herbicides only 
	cause plant toxicity to dicot broadleaf plants with little to no damage to most
	monocot grass species."""
	pass




# y = Preherbs("Barricade", 65, 1, 20)
# y.insertHerb()
# y.concUnits("dry")
# print y.herbs
# print y.getaiRate()
# print y.calc_formulation_rate()
# 
# 		
# x = Herbicide("Revolver", 0.19, 0.011875, 90)
# x.concUnits("liquid")
# x.insertHerb()
# print x.herbs
# print x.getaiRate()
# print "Apply %s at %0.3f gallons per acre" % (x.name, x.calc_formulation_rate())
# 
# #qhelp(Preherbs)
# 
# g = Preherbs("Ronstar 2G", 2, 1, 100)
# g.insertHerb()
# g.applicationType("spread")
# print g.distinguish_application_method()
# print g.herbs
# print g.getaiRate()

