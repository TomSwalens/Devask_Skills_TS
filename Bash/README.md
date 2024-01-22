Task name:
BASH
Task preparation:
VM with linux OS.
Task implementation:

I asked Chat GPT to help me write a scripte for these curl statements.

Task troubleshooting:

Status code stayed 000

curl -u cisco:cisco123! -H "Accept application/yang-data+json" http://192.168.56.101/restconf/data/ietf-interfaces:interfaces
curl: (7) Failed to connect to 192.168.56.101 port 80: Connection refused

Ping 192.168.56.101 OK

asked GTP for help:
# Enter global configuration mode
configure terminal

# Enter RESTCONF configuration mode
restconf

# Enable RESTCONF over HTTP
transport type http

But no fix still connection refused.




Task verification:

Task failed 

Status code's stayed 000