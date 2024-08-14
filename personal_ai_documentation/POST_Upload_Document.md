# POST Upload Document

## Endpoint
POST https://api.personal.ai/v1/upload-text

## Purpose
Upload a document to your Personal AI memory.

## Payloads

| Name        | Type               | Description                                                                               | Example                                                         |
|-------------|--------------------|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| Text        | string, required    | Body of text to upload to the memory. This should be as clean as possible.                 | `"This is a wikipedia article about corgis. The following are all ..."` |
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

url = "https://api.personal.ai/v1/upload-text"

payload = json.dumps({
    "Text": "This is a long document that is consumed into the document view.",
    "Title": "Personal AI",
    "Tags": "#doc1",
    "DomainName": "ai",
    "is_stack": false
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