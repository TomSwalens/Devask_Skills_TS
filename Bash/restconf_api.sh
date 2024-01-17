#!/bin/bash

# Variables
IP_HOST="192.168.56.101"
RESTCONF_USERNAME="cisco"
RESTCONF_PASSWORD="cisco123!"
DATA_FORMAT="application/yang-data+json"
LOOPBACK_INTERFACE="Loopback199"
LOOPBACK_IP="10.1.99.1"

# RESTCONF URLs
API_URL_PUT="https://$IP_HOST/restconf/data/ietf-interfaces:interfaces/interface=$LOOPBACK_INTERFACE"
API_URL_GET="https://$IP_HOST/restconf/data/ietf-interfaces:interfaces"

# Function to make RESTCONF GET request
make_get_request() {
    curl -s -k --user "$RESTCONF_USERNAME:$RESTCONF_PASSWORD" \
        --header "Content-Type: $DATA_FORMAT" \
        --url "$API_URL_GET" \
        "$@"
}

# Function to make RESTCONF PUT request
make_put_request() {
    # Modify the payload based on your specific requirements
    local payload='{"ietf-interfaces:interface": {"name": "'$LOOPBACK_INTERFACE'", "description": "Updated description"}}'

    curl -s -k --user "$RESTCONF_USERNAME:$RESTCONF_PASSWORD" \
        --header "Content-Type: $DATA_FORMAT" \
        --url "$API_URL_PUT" \
        --request PUT \
        --data-raw "$payload" \
        "$@"
}

# Retrieve information using GET request
get_response=$(make_get_request)

# Print GET response
echo "GET Response:"
echo "$get_response"

# Perform a PUT request (modify the payload as needed)
put_response=$(make_put_request)

# Print PUT response
echo "PUT Response:"
echo "$put_response"
