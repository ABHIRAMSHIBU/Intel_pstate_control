#!/bin/bash
a=$(whoami)
if [ $a = "root" ]; then
	echo "Copying file to /usr/bin"
	cp ./intel_pstate_control.py /usr/bin/intel_pstate_ctrl
	echo "Making the file executable"
	chmod +x /usr/bin/intel_pstate_ctrl
	echo "Done! run intel_pstate_ctrl to control your cpu."
else
	echo "You are not root, be root to continue..."
	echo Try "sudo ./install.py"
	echo Or run "su", then "./install.py"
fi
