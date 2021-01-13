import requests

url = "http://192.168.0.101:3000/assistant"

payload = "{\r\n    \"user\": \"js-teoh\",\r\n    \"command\": \"turn potato off\",\r\n    \"converse\": false,\r\n    \"broadcast\": false\r\n}"
headers = {
  'AssistantRelay': '',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
