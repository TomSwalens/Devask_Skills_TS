import requests

# Set the variables
url = "https://192.168.56.101:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"
headers = {'Accept': 'application/yang-data+json'}
auth = ('cisco', 'cisco123!')

# Make the RESTCONF request
response = requests.get(url, headers=headers, auth=auth, verify=False)

# Print the response headers and content
print(f"Response Headers:\n{response.headers}\n")
