#!/usr/bin/python
# Start of license shit
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
# End of license shit
import sys                                        # To use know arguments using argv
import os                                         # To execute shell commands
def root_check():                                 # Function to determine if program runs as root
	a=os.popen('whoami').read()		  # Using whoami command
	if (a[:-1]=='root'):			  # Check with the real value
		return 1                          # Returning 1 if the user is root
	else:					  # Returning 0 is the user is any other
		return 0                          # '' '' '' '' '' '' '' '' '' '' '' ''
def status() :					  # print function for configured values
	turbo=os.popen('cat /sys/devices/system/cpu/intel_pstate/no_turbo').read()[:-1]                       # Saving details in the file to turbo
	pct_max=os.popen('cat /sys/devices/system/cpu/intel_pstate/max_perf_pct').read()[:-1]                 # Saving details in the file to pct_max
	pct_min=os.popen('cat /sys/devices/system/cpu/intel_pstate/min_perf_pct').read()[:-1]                 # Saving details in the file to pct_min
	if (turbo=='0'):										      # Checking if turbo is on
		print("\tTurbo status: ON!")								      # Outputting the details to user
	else:												      # Outputting flase to user
		print("\tTurbo status: OFF!")
	print("\tCPU MAX PWR :"+pct_max+"%")                                                                  # Outputting cpu max power to user
	print("\tCPU MIN PWR :"+pct_min+"%")                                                                  # Outputting cpu min power to user
def write_max_pct(i):                                                                                         # Writing user values to max pct
	write_p=sys.argv[i+1]                                                                                 # Getting user defined value
	write_p="echo "+write_p+" >> /sys/devices/system/cpu/intel_pstate/max_perf_pct"                       # Making it a single string and a command
	os.system(write_p)                                                                                    # Executing the string as a command
def write_min_pct(i):                                                                                         # Writing user values to min pct
	write_p=sys.argv[i+1]                                                                                 # Getting user defined value
	write_p="echo "+write_p+" >> /sys/devices/system/cpu/intel_pstate/min_perf_pct"                       # Making it a single string and a command
	os.system(write_p)                                                                                    # Executing the command
def write_turbo(i):                                                                                           # Writing user value to turbo
	write_t=sys.argv[i+1]                                                                                 # Getting user defined values
	write_t="echo "+write_t+" >> /sys/devices/system/cpu/intel_pstate/no_turbo"                           # Combining strings and making it a command
	os.system(write_t)                                                                                    # Executng the command
def print_help():                                                                                             # Help function
	license()                                                                                             # Executing previously defined license function
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
j=len(sys.argv)                                                                                              # Getting number of arguments
if (j>1):                                                                                                    # Getting rid of file name as argument
	for i in range (1,j):                                                                                # Itration so that user can enter parameters dyanmically
		if(sys.argv[i]=='-max'):                                                                     # Finding -max argument
			if(root_check()==1):                                                                 # Checking if it is a root user and executing
				write_max_pct(i)                                                             # Executing earlier function
			else:
				print("\t Sorry, you are not root. You are not authorized to write max_pct .")
		if(sys.argv[i]=='-min'):                                                                     # Finding -min argument
			if(root_check()==1):                                                                 # Checking if it is root user and executing
				write_min_pct(i)
			else:
				print("\t Sorry, you are not root. You are not authorized to wite min_pct .")
		if(sys.argv[i]=='-t'):                                                                       # Finding -t argumnet
			if(root_check()==1):                                                                 # Checking if it is a root user and executing
				write_turbo(i)
			else:
				print("\t Sorry, you are not root. You are not authorized to change turbo .")
		if(sys.argv[i]=='-s'):                                                                      # Finding -s argument
			status()                                                                            # Executing status function
		if(sys.argv[i]=='-h'):                                                                      # Finding -h argument
			print_help()                                                                        # Executong help function
else:                                                                                                       # Checking if no argument specified
	print("You have not given any arguments, try intel_pstate_control -h for more details")
