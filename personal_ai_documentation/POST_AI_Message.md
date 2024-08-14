# POST AI Message

## Endpoint
POST https://api.personal.ai/v1/message

## Purpose
Interact with your AI by sending a message and receiving a response.

## Payloads

| Name        | Type               | Description                                                                               | Example                                                         |
|-------------|--------------------|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| Text        | string, required    | Message to send to your AI for a response                                                 | `"how old is my dog?"`                                           |
| Context     | string, optional    | Message to add additional context to the AI for a response. Similar to the Reply function | `"My dog was born in 2008."`                                     |
| DomainName  | string, optional    | The domain part of the AI profile URL                                                     | `"ai-climbing" for `ai-climbing.personal.ai``                   |
| UserName    | string, optional    | Name of the user sending the request                                                      | `"Leila" if the request comes from her`                         |
| SessionId   | string, optional    | Use the same sessionId to continue the conversation in that session                       | If no SessionId is passed, a SessionId will be returned.        |
| SourceName  | string, optional    | **Required if using with triggers** - Name of the source app of the inbound message       | `"slack"`                                                       |
| is_stack    | boolean, optional   | Flag to also add the user message (Text) to memory. Defaults to `false`.                  | If `true`, the message will be added to memory.                 |
| is_draft    | boolean, optional   | Flag to create a copilot message for the AI. Defaults to `false`.                         |                                                                 |

**Authorization** to upload to your memory stack is done via including your unique API key in the header.

## Headers

| Key          | Type               | Description                                        | Example                       |
|--------------|--------------------|----------------------------------------------------|-------------------------------|
| Content-Type | string, required    | The type of content of the body - only accepts JSON | `"application/json"`          |
| x-api-key    | string, required    | Unique API key per user (in App under Settings)     | `"4234ab78sdf09a7bf8723467b"` |

## Errors

| Key                | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| Authorization Failure | `{"detail": "AI message api unauthorized."}` - API key is invalid.         |
| Threshold Failure   | `{"detail": "AI message does not meet threshold."}` - Below user threshold.  |

## Example Request

```python
import requests

url = "https://api.personal.ai/v1/message"

payload = "{\n    \"Text\": \"what are we talking about\",\n    \"Context\": \"\",\n    \"UserName\": \"Leila\",\n    \"DomainName\": \"ai\",\n    \"SessionId\": \"d5e9f208-937c-4a9c-92bf-5fb90ce68ff6\"\n}"
headers = {
  'x-api-key': '{{user-api-key}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

## Status Code
200 OK

## Example Response
```json
{
  "ai_message": "We are talking about your cat's age. Your cat was born in 2000, so it is around 23 years old now. How has your cat been doing lately? 🐱",
  "ai_score": 47.18898852308854,
  "ai_name": "Sharon",
  "ai_picture": "https://lis-profile-images-prod.s3-us-west-2.amazonaws.com/thumbnail_2HNYYWHIEI8BISATZLGFVRYYHW8KVG.jpg",
  "SessionId": "d5e9f208-937c-4a9c-92bf-5fb90ce68ff6",
  "source_app": "api"
}
```