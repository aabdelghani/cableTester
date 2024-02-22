#!/bin/bash

# Adjust the path to your custom script
CUSTOM_SCRIPT="$(pwd)/start_on_boot.sh"

# Command to add to rc.local
CMD="(sleep 5; sh $CUSTOM_SCRIPT)&"

# Check if the custom script command is already in rc.local
if grep -Fxq "$CMD" /etc/rc.local; then
    echo "Autostart command already exists in /etc/rc.local."
else
    # Insert the command before 'exit 0' in rc.local
    sudo sed -i "/^exit 0/i $CMD" /etc/rc.local
    echo "Autostart command added to /etc/rc.local."
fi

# Make sure your custom script is executable
sudo chmod +x $CUSTOM_SCRIPT

# Prompt the user to restart
read -p "Autostart configuration applied. Do you want to restart now? (y/n): " answer
if [ "$answer" == "y" ]; then
    echo "Restarting the system..."
    sudo reboot
else
    echo "Please restart the system later to apply the changes."
fi

