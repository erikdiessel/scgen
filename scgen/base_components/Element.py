from abc import ABCMeta, abstractmethod

import pandas as pd

class Element(metaclass=ABCMeta):
	
	@property
	@abstractmethod
	def name(self):
		pass

	@abstractmethod
	def members(self):
		pass

	def toDataFrame(self):
		return pd.DataFrame({
			self.name: self.members()
		})