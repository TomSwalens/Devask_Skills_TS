import requests

# Set your Webex OAuth 2.0 access token
WEBEX_ACCESS_TOKEN = 'Y2NjZjdkMWUtMGJmMC00ZGRlLWI1YmItOWEwZmUxNGQ3ZTQ4YWM5MDc4YTktMzMw_P0A1_f385d8b4-839f-42c4-9819-c9b577f54c40'

# Webex API endpoint for creating a room
CREATE_ROOM_ENDPOINT = 'https://webexapis.com/v1/rooms'

# Function to create a Webex room
def create_webex_room(room_name):
    headers = {
        'Authorization': f'Bearer {WEBEX_ACCESS_TOKEN}',
        'Content-Type': 'application/json',
    }

    data = {
        'title': room_name,
    }

    response = requests.post(CREATE_ROOM_ENDPOINT, headers=headers, json=data)

    if response.status_code == 200:
        room_id = response.json().get('id')
        print(f"Webex room '{room_name}' created successfully. Room ID: {room_id}")
    else:
        print(f"Failed to create Webex room. Status Code: {response.status_code}, Error: {response.text}")

# Example: Create a Webex room with the name 'My Webex Room'
create_webex_room('devask_skills_toms')



