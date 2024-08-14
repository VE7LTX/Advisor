# GET Validate API-KEY

## Endpoint
GET https://api.personal.ai/v1/api-key/validate

## Purpose
Validate the provided API key to ensure it is correct and active.

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

url = "https://api.personal.ai/v1/api-key/validate"

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