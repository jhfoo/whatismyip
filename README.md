# whatismyip

## Purpose
tl;dr: Network routing analyzer by showing the IP a host sees coming from a specific network.

Long answer: Sometimes Ping is not good enough; traceroute sometimes works but not Ping. Why? Because they work slightly differently. In my case, my network between 2 hosts located in different geolocations route through a few potential (as in they should be disabled) NAT config, and it's important to confirm which NAT is seen by the receiving host. 

## Installation
This is now a Python app. Installation involves creating a virtual environment so dependencies can be installed in the user space.

```sh
%git clone https://github.com/jhfoo/whatismyip.git
%cd whatismyip
%./bin/setup
```

## Running
This spins up a simple HTTP REST service listening on all addresses.
```sh
%./bin/dev
```

To see what the receiving host sees simply go a HTTP GET on port 8001
```sh
curl <remote host>:8001
# sample response
# {"RemoteIp":"192.168.130.8"}
```

# Tested config
- FreeBSD w/ Python 3.11