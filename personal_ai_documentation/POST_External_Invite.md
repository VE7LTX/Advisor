# POST External Invite

## Endpoint
POST https://api.personal.ai/v1/invite


## Purpose
Send an Email Invite to a Personal AI or a Lounge.

## Query Parameters

| Key         | Type               | Description                                                               | Example                        |
|-------------|--------------------|---------------------------------------------------------------------------|--------------------------------|
| domain_name | string, required   | The AI persona where the invite will be sent from. This is the full domain of your AI persona or AI lounge URL. | `"ai-climbing"` for lounge URL of `ai-climbing.personal.ai` |
| email       | string, required   | The email to send the invitation to. If the request is successful, a confirmation will be in the response. | `"xiaoranz1986@gmail.com"` is the email to send the invitation to. |

## Authorization Headers

| Key          | Type               | Description                                        | Example                       |
|--------------|--------------------|----------------------------------------------------|-------------------------------|
| Content-Type | string, required    | The type of content of the body - only accepts JSON | `"application/json"`          |
| x-api-key    | string, required    | Unique API key per user (in App under Settings)     | `"4234ab78d31423a09a7bf8723467b"` |

## Payload
No body is required.

## Example Request

```python
import requests

url = "https://api.personal.ai/v1/invite?email=xiaoranz1986@gmail.com&domain_name=ai"

payload = "{}"
headers = {
  'x-api-key': 'user-api-key',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

## Status Code
200 OK

## Response Body
Invite Sent to xiaoranz1986@gmail.com