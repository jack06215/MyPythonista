import abc

class AbstractClass():
	__metaclass__ = abc.ABCMeta
	
	@abc.abstractclassmethod
	def method(self):
		print("Base Implemented Method Called")
		
class Implementation(AbstractClass):
	def method(self):
		print("Implemented Method Called")
		
impl = AbstractClass()
impl.method()
