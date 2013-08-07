# -*- coding: utf-8 -*-
#!/usr/bin/python
# Filename: christieSplus16.py

import socket   #for sockets
import struct
import time



#create an INET, STREAMing socket
class projector:
  """christe projector"""
	def __init__(self, host, port):

		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		 
		self.host = host;
		self.port = port;

		self.s.connect((host , port))
	
	def recv_timeout(self,the_socket,message,timeout=1):
		
		self.s.sendall(message)
		
		# create asynchronous socket
		the_socket.setblocking(0)
		total_data=[];
		data='';
		# get actual time for timeout handling
		begin=time.time()
		while 1:
			# if there is some data break after timeout
			if total_data and time.time()-begin > timeout:
				break
			# if you got no data wait till timeout
			elif time.time()-begin > timeout*2:
				break

			# fetch data into the temporary data buffer
			try:
				data = the_socket.recv(4096)
				if data:
					total_data.append(data)
					# reset timeout
					begin=time.time()
				else:
					# wait till reinitiate fetch
					time.sleep(0.1)
			except:
				pass

   		# seperatte the data into an array 
		data_string = (""+''.join(total_data)).split('(')
		return data_string

	# get all temparature values	
	def getTemperatures(self):
		temparatureList = []
		# set message to retrieve part 3 of the protocoll: see christie communication protocoll for details
		# get only the temperatures by slicing the returned list
		for i,d in enumerate(self.recv_timeout(self.s, "(SST?3)")[5:13]):
			#split the data string d at '"' to separate data from description, then get the second to las element which is the description of the sensor
			# part of example answer "01013 00000 SST!003 012 00035 "Backplane Temperature")(" 
			description = d.split('"')[-2]
			#split the data string d at whitespace and print out the 5th group, which is the actual temoparatur
			temparature = d.split(' ')[4]
			# convert the srting which holds the temparature into an int to get rid of the leading zeros
			# not all sensors are used in christie projectors, they respond with "N/A" for the temp value, 
			# this can't be converted with int(), thats why we need to try:except: 
			try:
				temparature = int(temparature)

			except:
				temparature = "N/A"
			temparatureList.append(temparature)

		temperaturesDict = {"ImageProcessor":temparatureList[0], "PanelDriver":temparatureList[1], "BackPlane":temparatureList[2], "OptionSlot1":temparatureList[3], "OptionSlot2":temparatureList[4], "red":temparatureList[5], "green":temparatureList[6], "blue":temparatureList[7]}
		return temperaturesDict

		
	# get all LightBulb values	
	def getLampInfo(self):
		# set message to retrieve part 1 of the protocoll: see christie communication protocoll for details
		# get only the temperatures by slicing the returned list		
		valueList = []
		for i,d in enumerate(self.recv_timeout(self.s, "(SST?1)")[3:6]):
			#split the data string d at '"' to separate data from description, then get the second to last element which is the description of the sensor
			description = d.split('"')[-2]
			#split the data string d at whitespace and print out the 5th group, which is the actual temoparatur
			value = d.split(' ')[4]
			# convert the srting which holds the value into an int to get rid of the leading zeros
			# not all sensors are used in christie projectors, they respond with "N/A" for the value, 
			# this can't be converted with int(), we need to try:except: 
			try:
				value = int(value)
			except:
				value = value
			valueList.append(value)

		valuesDict = {"LampExpired":valueList[0], "LampHours":valueList[1], "LampCounter":valueList[2]}
		return valuesDict

	







