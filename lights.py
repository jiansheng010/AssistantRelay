import requests

# pyuic5 -x AssistantRelay.ui -o AssistantRelay.py
# pyinstaller --noconsole AssistantRelayProg.py -n "Assistant Relay"

url = "http://192.168.0.101:3000/assistant"

light_setting = input('Turn lights off or on: ')

payload = "{\r\n    \"user\": \"js-teoh\",\r\n    \"command\": \"turn ninja and potato "+ light_setting + "\",\r\n    \"converse\": false,\r\n    \"broadcast\": false\r\n}"
headers = {
  'AssistantRelay': 'AIzaSyCSRXfziq7-NFGqMvFLXxYcA-TspJ1DCHM',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
