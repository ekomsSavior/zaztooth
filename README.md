# zaztooth

Zaztooth is a local web interface for Bluetooth Low Energy (BLE) operations including scanning, mesh broadcasting, and optional Ubertooth support.

INSTALLATION

Install required packages

sudo apt install python3-flask bluez ubertooth -y

Clone the repository

git clone https://github.com/ekomsSavior/zaztooth.git

cd zaztooth

RUNNING

Start the local server

sudo python3 app.py

ACCESS

Once running, open your browser and go to

http://localhost:5000

SCAN MODES

Use the dropdown in the interface to choose from

Basic BLE Scan: uses hcitool for standard BLE device discovery

Ubertooth Scan: uses ubertooth-scan if installed and connected

Mesh Broadcast: runs mesh_broadcast.py to send commands to BLE mesh bots (coming soon)
