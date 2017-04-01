#!/bin/bash
a=$(whoami)
if [ $a = "root" ]; then
	echo "Copying file to /usr/bin"
	cp ./intel_pstate_control.py /usr/bin/psctrl
	echo "Making the file executable"
	chmod +x /usr/bin/psctrl
	echo "Done! run psctrl to control your cpu."
else
	echo "You are not root, be root to continue..."
	echo Try "sudo ./install.py"
	echo Or run "su", then "./install.py"
fi
