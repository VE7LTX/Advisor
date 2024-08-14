# GET Validate Token

## Endpoint
GET {{command_url}}/external/api/webhook/verification?token=chatbot&challenge=12345

## Purpose
Validate the provided token and challenge for webhook verification.

## Query Parameters

| Key        | Type               | Description                                 | Example  |
|------------|--------------------|---------------------------------------------|----------|
| token      | string, required    | The token to validate                       | `chatbot`|
| challenge  | string, required    | The challenge to validate                   | `12345`  |

## Authorization Headers

| Key          | Type               | Description                                        | Example                       |
|--------------|--------------------|----------------------------------------------------|-------------------------------|
| Content-Type | string, required    | The type of content of the body - only accepts JSON | `"application/json"`          |
| x-api-key    | string, required    | Unique API key per user (in App under Settings)     | `"your api key here"`         |

## Payload
No body is required.

## Example Request

```python
import requests

url = "{{command_url}}/external/api/webhook/verification?token=chatbot&challenge=12345"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'x-api-key': 'your api key here'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

## Status Code
200 OK

## Response Body
```json
{
  "validation": "success",
  "firstName": "Sharon",
  "lastName": "Zhang",
  "email": "sharon@personal.ai"
}
```

