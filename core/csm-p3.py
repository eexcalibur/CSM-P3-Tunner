'''
This is the main module
author: zhangtao slnazhangtao@gmail.com
2014.7.6
'''

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
	#set hosts list from mdp.hosts
	hosts_list = []
	fp_hosts = open("../mpd.hosts", 'r')
	for host in fp_hosts:
		host_format = host.strip('\n')
		hosts_list.append(host_format)
	fp_hosts.close();

	#set each machine is availab (default is 1)
	hosts = {}.fromkeys(hosts_list, 1)
	hosts_avail = len(hosts)
	#print hosts
	#print hosts_avail


	#assign hosts for each instance
	hosts_per_case = commpara.process_per_case / commpara.ntasks_per_node
	for instance in xrange(0,commpara.case_number):
		counter = 0
	 	hosts_group = []
	 	if(hosts_avail < hosts_per_case):
	 		continue
	 	for host in hosts_list:
			if(hosts[host] == 1 and counter != hosts_per_case):
	 			hosts_group.append(host)
	 			hosts[host] = 0
	 			counter = counter + 1
	 			hosts_avail = hosts_avail - 1
			elif(counter == hosts_per_case):
				break
	 	print hosts_group
 




