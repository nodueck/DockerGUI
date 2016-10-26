#from django.db import models
from docker import Client


# Create your models here.
class Docker:
	cli = Client(base_url='tcp://127.0.0.1:2375')

	@classmethod
	def getCLI(cls):
		return cls.cli

	@classmethod
	def getContainerList(cls):
		return cls.getCLI().containers(all=True)

	@classmethod
	def getContainer(cls, id):
		for container in getContainerList():
			return cls.getCLI().containers(all=True, filters={'id':id})


	@classmethod
	def getImageList(cls):
		return cls.getCLI().images()

	@classmethod
	def getImage(cls, id):
		return cls.getCLI().images(filters={'id':id})

