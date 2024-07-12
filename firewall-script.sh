#! /bin/bash


# Assert that the default policy are ACCEPT in order to maintain our current connection
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT

# Flush existing firewall rules
sudo iptables -F




# Accept all current connections to remain unaffected
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT


# Create a chain named KNOCKING
sudo iptables -N KNOCKING
# Transfer all traffic to our KNOCKING chain
sudo iptables -A INPUT -j KNOCKING



# Create a chain named GAT1
sudo iptables -N GATE1
# Define our initial knocking test 
sudo iptables -A GATE1 -p tcp --dport 22 -m recent --name AUTH1 --set -j DROP
# If the test do not pass we want to drop the packet 
sudo iptables -A GATE1 -j DROP



# Create a chain named GATE2
sudo iptables -N GATE2
# Clean the name set by the previous test
sudo iptables -A GATE2 -m recent --name AUTH1 --remove
# Second test
sudo iptables -A GATE2 -p tcp --dport 80 -m recent --name AUTH2 --set -j DROP
# If second test does not succeed redirect to GATE1
sudo iptables -A GATE2 -j GATE1



# Create a chain named GATE3
sudo iptables -N GATE3
# Clean the name set by the previous test
sudo iptables -A GATE3 -m recent --name AUTH2 --remove
# Third test
sudo iptables -A GATE3 -p tcp --dport 15022 -m recent --name AUTH3 --set -j DROP
# If Third test does not succeed redirect to GATE1
sudo iptables -A GATE3 -j GATE1



# Create a chain named PASSED
sudo iptables -N PASSED
# Clean the name set by the previous test
sudo iptables -A PASSED -m recent --name AUTH3 --remove
# Open the port 7843 to the client that successfully knocked the correct sequence
sudo iptables -A PASSED -p tcp --dport 7843 -j ACCEPT
# Else redirect to GATE1
sudo iptables -A PASSED -j GATE1


# The following commands create the logic for how to pass off the traffic

# Redirect KNOCKING traffic to GATE3 if the name flag is AUTH3 and no older than 30sec
sudo iptables -A KNOCKING -m recent --rcheck --name AUTH3 -j PASSED
# Redirect KNOCKING traffic to GATE2 if the name flag is AUTH2 and no older than 15sec
sudo iptables -A KNOCKING -m recent --rcheck --seconds 15 --name AUTH2 -j GATE3
# Redirect KNOCKING traffic to GATE2 if the name is flag AUTH1 and no older than 30sec
sudo iptables -A KNOCKING -m recent --rcheck --seconds 30 --name AUTH1 -j GATE2
# Redirect all KNOCKING traffic to GATE1
sudo iptables -A KNOCKING -j GATE1