#!/bin/bash

# Set variables
IP_HOST="192.168.56.101"
RESTCONF_USERNAME="cisco"
RESTCONF_PASSWORD="cisco123!"
DATA_FORMAT="application/yang-data+json"
LOOPBACK_INTERFACE="Loopback199"
LOOPBACK_IP="10.1.99.1"


API_URL_GET=http://$IP_HOST/restconf/data/ietf-interfaces:interfaces

# Get today's date
TODAY=$(date +"%Y-%m-%d")

# Output the first line
echo "Today's date: $TODAY"

# Output the second line
echo "START REST API CALL"
echo "============"

# Output for FIRST API CALL
echo "FIRST API CALL"
echo "============"

# Execute the first API call and capture the status code
STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}" -u $RESTCONF_USERNAME:$RESTCONF_PASSWORD -H "Accept: $DATA_FORMAT" "$API_URL_GET")
echo "Status Code: $STATUS_CODE"
echo "============"

# Output for SECOND API CALL
echo "SECOND API CALL"
echo "============"

# Execute the second API call and capture the status code
STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}" -u $RESTCONF_USERNAME:$RESTCONF_PASSWORD -H "Accept: $DATA_FORMAT" "$API_URL_GET")
echo "Status Code: $STATUS_CODE"

# Output interfaces information (realtime output)
echo "Interfaces: (realtime output)"
# Add the command to get interfaces information

# Output the last line
echo "END REST API CALL"
