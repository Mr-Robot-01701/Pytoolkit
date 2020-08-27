import os
from urllib.request import urlopen
import json
import socket
import sys
import threading
from pytoolkitupd import * 



os.system('clear')

print('*'*70)
os.system('figlet Welcome To PY TOOL KIT   !')

print('*' * 70)
print('\nwelcome to ip-toolkit!!\n')

def ip():

	input1 = str(input('ip-tool>: '))
	if input1 =='help':
		print('-' * 70)
		print('\nenter 1 for ip-informer')
		print('\nenter 2 to now your ip')
		print('\nenter 3 to use nmap')
		print('\nenter [clear] to clear the terminal')
		print('\nenter [exit] to exit the tool')
		print('\nenter [ upd ] to update the tool (user should be rooted!!!!)')
	print('-' * 70)




	if input1 == '1':
		ip = input('what is your target ip: ')

		url = 'http://ip-api.com/json/'
		response = urlopen(url + ip)
		data = response.read()
		values = json.loads(data)

		print('\nip: ' + values['query'])
		print('city: ' + values['city'])
		print('ISP: ' + values['isp'])
		print('Country: ' + values['country'])
		print('region: ' + values['region'])
		print('-' * 70)

	



	if input1 == '2':
	 	hostname = socket.gethostname()
	 	ipv = socket.gethostbyname_ex(hostname)
	 	print(ipv, '\n')



	if input1 == '3':
		os.system("clear")
		os.system('figlet Nmap')
		print('\nusage = nmap\nip_address = <enter targets_ip>\nscanning arguments = give scanning argumetns ex. -sS -v etc.\nnote: [everything must be in a single line to run this programme]\n')
		ip_address = input('ip_address/web-address = ')
		scanning_arguments = input('scanning_arguments = ')

		nmap_collaps = (f'nmap {scanning_arguments} {ip_address}')
		os.system(nmap_collaps)




	if input1 == 'upd':
		os.system('clear')
		os.system('updating you tool!!')
		os.system(upda)
		os.system(updb)




	if input1 == 'clear':
		os.system('clear')

	if input1 == "exit":
		os.system('clear')
		exit()

if __name__ == '__main__':

	
	while True:
		ip()