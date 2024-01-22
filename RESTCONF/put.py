import requests

# Set variables
url = "https://192.168.56.101:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"
headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}
auth = ('cisco', 'cisco123!')

# Define the payload
payload = {
    "severity": "warnings"
}

# Make the RESTCONF request with the PUT method
response = requests.put(url, headers=headers, auth=auth, json=payload, verify=False)

# Print the response headers and content
print(f"Response Headers:\n{response.headers}\n")
print(f"Response Content:\n{response.text}")
