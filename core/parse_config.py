'''
This module handles CSM-P3 configure definition
Create on 2014.7.3
author:zhangtao slnazhangtao@gmail.com
'''

from xml.dom import minidom , Node
import commpara

class CSM_P3_XML(object):
	"""This class handles CSM-P3 configure definition"""
	def __init__(self, doc):
		for child in doc.childNodes:
			if child.nodeType == Node.ELEMENT_NODE and child.tagName == "public" :
				#print "public"
				self.handle_public(child)
			if child.nodeType == Node.ELEMENT_NODE and child.tagName == "schedule" :
				#print "schedule"
				self.handle_schedule(child)

	def handle_public(self, node):
		#for child in node.childNodes:
		for child in node.getElementsByTagName("entry") :
			key=child.getAttribute("key")
			if (key == "case_number"):
				commpara.case_number=child.getAttribute("value")
				print "case_number: ", commpara.case_number
			elif (key == "non"):
				commpara.non=child.getAttribute("value")
				print "non: ", commpara.non

	def handle_schedule(self, node):
		for child in node.getElementsByTagName("entry"):
			 key=child.getAttribute("key")
			 if (key == "job_scheduler"):
			 	commpara.job_scheduler=child.getAttribute("value")
			 	print "job_scheduler: ", commpara.job_scheduler
			 elif (key == "machine_hosts"):
			 	commpara.machine_hosts=child.getAttribute("value")
			 	print "machine_hosts: ", commpara.machine_hosts
			 elif (key == "ntasks_per_node"):
			 	commpara.ntasks_per_node=child.getAttribute("value")
			 	print "ntasks_per_node: ", commpara.ntasks_per_node
			 elif (key == "process_per_case"):
			 	commpara.process_per_case=child.getAttribute("value")
			 	print "process_per_case: ", commpara.process_per_case


doc = minidom.parse("../csm-p3.xml")
for child in doc.childNodes:
	if child.nodeType == Node.COMMENT_NODE :
		print "Conment: ", child.nodeValue
	elif child.nodeType == Node.ELEMENT_NODE : 
		CSM_P3_XML(child)