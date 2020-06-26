import os
import sowerest

host = "http://api.sowemail.com:9000"
api_key = os.environ.get('SOWEMAIL_API_KEY')
request_headers = {
    "Authorization": 'Bearer {}'.format(api_key)
}
version = 1
client = sowerest.Client(host=host,
                         request_headers=request_headers,
                         version=version)

# Send email
data = {
    "personalizations": [
        {
            "to": [
                {
                    "email": "fourat@sowemail.com"
                }
            ]
        }
    ],
    "from": {
        "email": "fourat@gmail.com"
    },
    "subject": "Hello from SoWeMail",
    "content": [
        {
            "type": "text/plain",
            "value": "Simple email sending example using python's sowerest library"
        }
    ]
}
response = client.mail.send.post(request_body=data)
print(response.status_code)
print(response.headers)
print(response.body)
