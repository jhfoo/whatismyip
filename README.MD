
# Purpose
Simple app to validate NAT configuration from VPNs.

# Usage
1. Install and start app in destination environment, usually a host or jail with a different IP from source.
```sh
# To install
npm i

# To start
npm start
```

2. Do a HTTP GET from source environment.
```sh
curl http://<destination ip>:8080
```

3. App in destination will list IP received. Curl response will also show the same.


