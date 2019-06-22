#!/bin/bash
# TudrmeUpdate
# ============
# Updates the server on Tudrme v2
# -------------------------------
# Usage:
# ./upload.sh <key> <pass> <dir> <user> <ip>
# key (REQUIRED): Server SSH key
# pass (OPTIONAL): SSH key password - not implemented
# dir (OPTIONAL): Tudrme code directory - not implemented
# user (OPTIONAL): Server username - not implemented
# ip (OPTIONAL): Server IP address - not implemented
# -------------------------------
# Gideon Tong - 21/Jun/2019

# === CONSTANTS ===
SERVER="Tudrme"
SERVER_USERNAME=""
SERVER_IP=""
SCRIPT_VER="0.0.1"
SERVER_VER="19.6.2.PRERELEASE"

# Check for server password provided in arguments
if ["$1" == ""]; then
	echo "> The Tudrme server requires SSH keys!"
	exit 1
else
	echo "> SSH key provided, logging in..."
fi

# Attempt to access SSH key
if ["$2" == ""]; then
	echo "> No SSH key password was provided, detecting encryption..."
	if sed "2q;d" $1 =~ "ENCRYPTED"; then
		echo "> SSH keyfile was encrypted! Please provide a password."
		#exit 1
	fi
else
	echo "> Attempting to use provided SSH key..."
	ssh-keygen -y -f $1 -p $2
	if [$? == 255]; then
		echo "> Provided SSH key was incorrect."
		exit 1
	fi
fi

ssh -i $1 $SERVER_USERNAME@$SERVER_IP << EOF
sudo service tudrme stop
cd ~
mv tudrme tudrme-old
EOF

scp 

echo "Tudrme Upload Beginning..."