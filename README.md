# AuTor
Automated mass Tor nodes distribution script. Distribute hundreds of Tor nodes within 5 minutes.

This only has been tested on Ubuntu 24.04 servers. Please proceed with caution.

# Installation
Linux
```
git clone https://github.com/lilmond/AuTor
cd AuTor
python3 -m venv venv
source venv/lib/activate
pip install -r requirements.txt
```

# Distribute Tor Nodes
First things first, you'll need a server list, which quite obviously you own and have access to (**via private key**).

Write down your server IP's into the `server_list.txt` file.

Next thing you'll have to do is to copy your **private key** into **AuTor** directory.

Now edit `AuTor.py` and set `PRIVATE_KEY` variable according to your **private key's file** name.

Now you might wanna edit `TORRC` variable for your own custom torrc configuration.

Run AuTor via `python AuTor.py`

Goodluck!
