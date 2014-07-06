from xml.dom import minidom , Node
import commpara
import parse_config

#parse csm-p3 configure xml file
doc = minidom.parse("../csm-p3.xml")
for child in doc.childNodes:
	if child.nodeType == Node.COMMENT_NODE :
		print "Conment: ", child.nodeValue
	elif child.nodeType == Node.ELEMENT_NODE : 
		parse_config.CSM_P3_XML(child)


#handle scheduler
print commpara.job_scheduler

#handle other scheduler, small clusters without jobs scheduler system
if (commpara.job_scheduler == "other"):
	