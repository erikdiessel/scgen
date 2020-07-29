from scgen.base_components.Element import Element

class Materials(Element):
	name = "materials"

	def __init__(self, count, **additionalSettings):
		self.__members = ["material_" + str(i) for i in range(1,count+1)]

	def members(self):
		return self.__members

