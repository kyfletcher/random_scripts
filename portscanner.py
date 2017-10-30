#!/usr/bin/env python
from socket import *
import subprocess
import sys
from datetime import datetime
import getopt
from scapy.all import *

# At a minimum your tool should (40 points):
# 1.Allow command-line switches to specify a host and port.
# 2.Present a simple response to the user.
# Additional points are provided depending on the comprehensiveness of the feature. For example:
	Allow more than one host to be scanned – 10 points maximum.
	#		Reading a text file of host IP’s or reading a range from the command line – 5 points.
			Doing both +2 points
		Allowing different ways to specify hosts (subnet mask and range) – 5 points.
#	Allow multiple ports to be specified – 10 points maximum.
#	Use of more than one protocol (TCP or UDP is assumed within the base 40 points)
#		ICMP 5 points
		TCP or UDP (to complement the one already provided) – 10 points
#	Traceroute – Max 5 points
	User experience results – eg. An HTML or PDF report:
		Max 10 points
	GUI or Web management of tool
		Max 10 points
	Other ideas or concepts not mentioned
		Max 20 points
		# Gives total time
		# Allows for CTRL+C exiting

def main(argv):

	if not argv:
		print "Syntax is `portscanner.py <host> <port> <proto>`"
		sys.exit()

	remoteServer = argv[0]
	remoteServerList = remoteServer.split(',')

	portRange = argv[1]
	portRangeList = portRange.split('-')

	if len(portRangeList) == 1:
		portRangeList.insert(1, portRange)



	t1 = datetime.now()

	for host in remoteServerList:
		remoteServerIP  = socket.gethostbyname(host)

		print "Traceroute Starting"
		#result, unans = traceroute(host,maxttl=32)


		print "-" * 60
		print "Please wait, scanning remote host", remoteServerIP
		print "-" * 60

		if argv[2] == "tcp":
			print "tcpscan"
			try:
			    for port in range(int(portRangeList[0]), int(portRangeList[1])+1):
			        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			        result = sock.connect_ex((remoteServerIP, port))
			        if result == 0:
			            print "Port {}: 	 Open".format(port)
			        sock.close()

			except KeyboardInterrupt:
			    print "You pressed Ctrl+C"
			    sys.exit()

			except socket.gaierror:
			    print 'Hostname could not be resolved. Exiting'
			    sys.exit()

			except socket.error:
			    print "Couldn't connect to server"
			    sys.exit()

		if argv[2] == "udp":
			try:
				for port in range(int(portRangeList[0]), int(portRangeList[1])+1):
					packet = IP(dst=host)/UDP(dport=port)
					resp = sr1(packet, timeout=2)
					if resp:
						print "Port {}: 	 Open".format(port)

					# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
					# data = "Testing"
					# sock.sendto(data,(host,port))
					# sock.settimeout(0)
					# print ((sock.recvfrom(1024)))
					# print "Port {}: 	 Open".format(port)
					# sock.close()


			except KeyboardInterrupt:
			    print "You pressed Ctrl+C"
			    sys.exit()

			except socket.gaierror:
			    print 'Hostname could not be resolved. Exiting'
			    sys.exit()

			except socket.error:
			    print "Couldn't connect to server"
			    sys.exit()



		if argv[2] == "icmp":
			try:
				print "Starting ICMP"
				pingr = IP(dst=host)/ICMP()
				resp = srloop(pingr,count=5)

			except KeyboardInterrupt:
			    print "You pressed Ctrl+C"
			    sys.exit()

			except socket.gaierror:
			    print 'Hostname could not be resolved. Exiting'
			    sys.exit()

			except socket.error:
			    print "Couldn't connect to server"
			    sys.exit()


		t2 = datetime.now()

		total =  t2 - t1

		print 'Scanning Completed in: ', total



if __name__ == "__main__":
   main(sys.argv[1:]) 
