from scgen.base_components.Element import Element

class Plants(Element):
	name = "plants"

	def __init__(self, count, **additionalSettings):
		self.__members = ["plant_" + str(i) for i in range(1,count+1)]

	def members(self):
		return self.__members