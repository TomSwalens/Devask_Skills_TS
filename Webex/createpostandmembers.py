# Fill in this file with the code to create a room membership from the Webex Teams exercise
import requests

# Set your Webex OAuth 2.0 access token
WEBEX_ACCESS_TOKEN = 'Y2NjZjdkMWUtMGJmMC00ZGRlLWI1YmItOWEwZmUxNGQ3ZTQ4YWM5MDc4YTktMzMw_P0A1_f385d8b4-839f-42c4-9819-c9b577f54c40'
# Webex API endpoint for adding people to a room
ADD_PEOPLE_ENDPOINT = 'https://webexapis.com/v1/memberships'

# Webex API endpoint for posting a message to a room
POST_MESSAGE_ENDPOINT = 'https://webexapis.com/v1/messages'

# Function to add people to a Webex room
def add_people_to_webex_room(room_id, email_list):
    headers = {
        'Authorization': f'Bearer {WEBEX_ACCESS_TOKEN}',
        'Content-Type': 'application/json',
    }

    for email in email_list:
        data = {
            'roomId': room_id,
            'personEmail': email,
        }

        response = requests.post(ADD_PEOPLE_ENDPOINT, headers=headers, json=data)

        if response.status_code == 200:
            print(f"Added {email} to the Webex room.")
        else:
            print(f"Failed to add {email} to the Webex room. Status Code: {response.status_code}, Error: {response.text}")

# Function to post a message with a link and screenshots to a Webex room
def post_message_to_webex_room(room_id, message):
    headers = {
        'Authorization': f'Bearer {WEBEX_ACCESS_TOKEN}',
        'Content-Type': 'application/json',
    }

    data = {
        'roomId': room_id,
        'text': message,
    }

    response = requests.post(POST_MESSAGE_ENDPOINT, headers=headers, json=data)

    if response.status_code == 200:
        print(f"Message posted to the Webex room.")
    else:
        print(f"Failed to post message to the Webex room. Status Code: {response.status_code}, Error: {response.text}")

# Example: Get the room_id from the previous script or from the Webex interface
webex_room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vYzcwY2YwODAtYjU0Yy0xMWVlLTk0YWItOWYwYTljZTlmYjlk'

# Example: List of email addresses to add to the room
emails_to_add = ['yvan.rooseleer@biasc.be']

# Example: Message to post in the room
message_to_post = 'Check out my GitHub for the documentation of the Devasc skills: https://github.com/TomSwalens/Devask_Skills_TS\n\nAttached are screenshots.'

# Example: Add people to the room
add_people_to_webex_room(webex_room_id, emails_to_add)

# Example: Post a message with a link and screenshots to the room
post_message_to_webex_room(webex_room_id, message_to_post)
