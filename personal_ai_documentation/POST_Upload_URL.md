# POST Upload Url

## Endpoint
POST https://api.personal.ai/v1/upload

## Purpose
Upload a URL to your Personal AI memory.

## Payloads

| Name        | Type               | Description                                                                               | Example                                                         |
|-------------|--------------------|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| Url         | string, required    | URL to upload, including public YouTube URLs, LinkedIn profiles, news articles, blogs, etc.| `"https://www.linkedin.com/in/kanugantisuman"`                  |
| Title       | string, optional    | Title of the uploaded document                                                            | `"How to create your Personal AI"`                              |
| StartTime   | string, optional    | ISO timestamp string indicating start time - UTC. Defaults to the current time.           | `"2023-07-09T10:00:00.000Z"`                                    |
| EndTime     | string, optional    | ISO timestamp string indicating end time - UTC. Defaults to the current time.             | `"2023-07-09T10:00:00.000Z"`                                    |
| DomainName  | string, optional    | Domain name of AI Persona to upload to (e.g., `justintan-work.personal.ai`)               | `"justintan-work"`                                              |
| Tags        | string, optional    | Comma-delimited list of tags for context and reference                                    | `"new york","san francisco"`                                    |
| is_stack    | boolean, optional   | Boolean to specify whether to add the document to memory. Defaults to `true`.             | `true`                                                          |

**Authorization** to upload to your memory stack is done via including your unique API key in the header.

## Headers

| Key          | Type               | Description                                        | Example                       |
|--------------|--------------------|----------------------------------------------------|-------------------------------|
| Content-Type | string, required    | The type of content of the body - only accepts JSON | `"application/json"`          |
| x-api-key    | string, required    | Unique API key per user (in App under Settings)     | `"4234ab78d31423a09a7bf8723467b"` |

## Example Request

```python
import requests
import json

url = "https://api.personal.ai/v1/upload"

payload = json.dumps({
  "Url": "https://www.linkedin.com/in/kanugantisuman",
  "StartTime": "2023-07-09T10:00:00.000Z",
  "EndTime": "2023-07-09T10:00:00.000Z",
  "SourceApp": "AI Bot",
  "DomainName": "justintan-work"
})
headers = {
  'Content-Type': 'application/json',
  'x-api-key': '{{user-api-key}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

## Status Code
200 OK

## Example Response
```json
{
  "success": true
}
```