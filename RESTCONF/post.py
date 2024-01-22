import requests

# Set variables
url = "https://192.168.56.101:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor"
headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}
auth = ('cisco', 'cisco123!')

# Define the payload
payload = {
    "severity": "alerts"
}

# Make the RESTCONF request with the POST method
response = requests.post(url, headers=headers, auth=auth, json=payload, verify=False)

# Print the response headers and content
print(f"Response Headers:\n{response.headers}\n")
print(f"Response Content:\n{response.text}")
