#!/usr/bin/python
def license():
	print("Copyright (C) 2016  Abhiram Shibu")
	print("")
	print("    This program is free software: you can redistribute it and/or modify")
	print("    it under the terms of the GNU General Public License as published by")
	print("    the Free Software Foundation, either version 3 of the License, or")
	print("    (at your option) any later version.")
	print("")
	print("    This program is distributed in the hope that it will be useful,")
	print("    but WITHOUT ANY WARRANTY; without even the implied warranty of")
	print("    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the")
	print("    GNU General Public License for more details.")
	print("")
	print("    You should have received a copy of the GNU General Public License")
	print("    along with this program.  If not, see <http://www.gnu.org/licenses/>.\n")
import sys                                        # To use know arguments using argv
import os                                         # To execute shell commands
def root_check():
	a=os.popen('whoami').read()
	if (a[:-1]=='root'):
		return 1
	else:
		return 0
def status() :
	turbo=os.popen('cat /sys/devices/system/cpu/intel_pstate/no_turbo').read()[:-1]
	pct_max=os.popen('cat /sys/devices/system/cpu/intel_pstate/max_perf_pct').read()[:-1]
	pct_min=os.popen('cat /sys/devices/system/cpu/intel_pstate/min_perf_pct').read()[:-1]
	if (turbo=='0'):
		print("\tTurbo status: ON!")
	else:
		print("\tTurbo status: OFF!")
	print("\tCPU MAX PWR :"+pct_max+"%")
	print("\tCPU MIN PWR :"+pct_min+"%")
def write_max_pct(i):
	write_p=sys.argv[i+1]
	write_p="echo "+write_p+" >> /sys/devices/system/cpu/intel_pstate/max_perf_pct"
	os.system(write_p)
def write_min_pct(i):
	write_p=sys.argv[i+1]
	write_p="echo "+write_p+" >> /sys/devices/system/cpu/intel_pstate/min_perf_pct"
	os.system(write_p)
def write_turbo(i):
	write_t=sys.argv[i+1]
	write_t="echo "+write_t+" >> /sys/devices/system/cpu/intel_pstate/no_turbo"
	os.system(write_t)
def print_help():
	license()
	print("This program is written in python, tested in 3.0")
	print("Normal usage 'intel_pstate_control <arguments>'")
	print("Example Usage : intel_pstate_control -t 0 -max 100 -min 10 -s")
	print("Author : Abhiram Shibu Git: github.com/ABHIRAMSHIBU Email: abhiramshibu1998@gmail.com")
	print("")
	print("")
	print("\t-max : It sets maximum pct for your CPU")
	print("\t-min : It sets minimum pct for your CPU")
	print("\t-t   : It sets turbo mode for your CPU, 0=ON and 1=OFF")
	print("\t-h   : Displays this dialogue")
	print("\t-s   : Displays current settings for your CPU")
j=len(sys.argv)
if (j>1):
	for i in range (1,j):
		if(sys.argv[i]=='-max'):
			if(root_check()==1):
				write_max_pct(i)
			else:
				print("\t Sorry, you are not root. You are not authorized to write max_pct .")
		if(sys.argv[i]=='-min'):
			if(root_check()==1):
				write_min_pct(i)
			else:
				print("\t Sorry, you are not root. You are not authorized to wite min_pct .")
		if(sys.argv[i]=='-t'):
			if(root_check()==1):
				write_turbo(i)
			else:
				print("\t Sorry, you are not root. You are not authorized to change turbo .")
		if(sys.argv[i]=='-s'):
			status()
		if(sys.argv[i]=='-h'):
			print_help()
else:
	print("You have not given any arguments, try intel_pstate_control -h for more details")
