'''
This module handles CSM-P3 configure definition
Create on 2014.7.3
author:zhangtao slnazhangtao@gmail.com
'''

from xml.dom import minidom , Node

class CSM-P3-XML(object):
	"""This class handles CSM-P3 configure definition"""
	def __init__(self, doc):
		for child in doc.childNodes:
			if child.nodeType == Node.ELEMENT_NODE and child.tagName == "public" :
				self.handle_public(child)
			if child.nodeType == Node.ELEMENT_NODE and child.tagName == "schedule" :
				self.handle_schedule(child)

	def handle_public(self, node):
		child=node.childNodes
		case-number=child.getAttribute("value")
		print "case-number: ", case-number

			
	def handle_schedule(self, node):
		for child in node.childNodes:
