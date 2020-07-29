from scgen.base_components.Element import Element

class TimePeriods(Element):
	name = "timePeriods"

	def __init__(self, count, **additionalSettings):
		self.__members = [f"2020-{i:02}" for i in range(1,count+1)]

	def members(self):
		return self.__members