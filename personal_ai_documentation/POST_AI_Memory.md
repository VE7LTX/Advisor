# POST AI Memory

## Endpoint
POST https://api.personal.ai/v1/memory

## Purpose
Upload text memories to your memory stack.

## Payloads

| Name        | Type               | Description                                                                               | Example                                                         |
|-------------|--------------------|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| Text        | string, required    | Plain text memories to upload to your stack                                               | `"My first memory with Personal AI"`                            |
| CreatedTime | string, optional    | Time (including timezone) of the memory to help you recall when it is from. Defaults to "Now". | `"Wed, 28 Jul 2021 13:30:00 PDT"`                                |
| SourceName  | string, required    | The source or application of the memory to help you recall where it is from               | `"Notes" or "My Thoughts"`                                      |
| RawFeedText | string, optional    | The formatted text that can be stored as it is                                            | `"My <b>cat</b> is born in <b>2000</b>"`                        |
| DomainName  | string, optional    | The AI persona where the memory will be uploaded. This is the full domain of your AI profile URL. | `"ai-climbing" for profile URL of `ai-climbing.personal.ai``     |
| Tags        | string, optional    | Comma delimited list of tags for the memory                                               | `"pet,dog,woof woof"`                                           |

**Authorization** to upload to your memory stack is done via including your unique API key in the header.

## Headers

| Key          | Type               | Description                                        | Example                       |
|--------------|--------------------|----------------------------------------------------|-------------------------------|
| Content-Type | string, required    | The type of content of the body - only accepts JSON | `"application/json"`          |
| x-api-key    | string, required    | Unique API key per user (in App under Settings)     | `"4234ab78d31423a09a7bf8723467b"` |

## Errors

| Key                | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| Authorization Failure | `{"detail": "AI memory api unauthorized."}` - API key is invalid.          |
| Upload Failure      | `{"detail": "AI memory cannot be uploaded."}` - Invalid date format or missing argument. |

## Example Request

```python
import requests
import json

url = "https://api.personal.ai/v1/memory"

payload = json.dumps({
  "Text": "my cat is born in #2000",
  "RawFeedText": "My <b>cat</b> is born in <b>2000</b>",
  "DomainName": "ai-climbing",
  "CreatedTime": "Wed, 19 Sep 2023 13:31:00 PDT",
  "SourceName": "Twitter",
  "Tags": "pet,cat,meow two"
})
headers = {
  'Content-Type': 'application/json',
  'x-api-key': '{{user_api_key}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

## Status Code
200 OK

## Example Response
```json
{
  "type": "memory",
  "payload": [
    {
      "data": [
        {
          "type": "MEMORY",
          "memlevel": "MEMBLOCK",
          "memlabel": "my cat is born in #2000",
          "start_time_utc": "2023-09-19T20:31:00.000+00:00",
          "end_time_utc": null,
          "creator": {
            "name": "Sharon Zhang",
            "identity_id": 2,
            "domain_id": 62,
            "identity_name": null,
            "email": "",
            "propertyBag": {
              "email": {
                "key": "email",
                "value": "sharon@personal.ai"
              },
              "picture": {
                "key": "picture",
                "value": "SOCXUX48PQMX9S5L8YM45O9J9DYG6Z.jpg"
              }
            }
          },
          "owner": {
            "name": "Sharon Zhang",
            "identity_id": 2,
            "domain_id": 16112,
            "identity_name": null,
            "email": "",
            "propertyBag": {
              "email": {
                "key": "email",
                "value": "sharon@personal.ai"
              },
              "picture": {
                "key": "picture",
                "value": "Y9X4OFS9MSSUQEBV908FEY8AFGDP41.jpg"
              }
            }
          },
          "follower": {
            "name": "",
            "identity_id": 2,
            "domain_id": 16112,
            "identity_name": null,
            "email": "",
            "propertyBag": {}
          },
          "source": {
            "type": "text",
            "name": "WebApp",
            "device": "Explore Mode",
            "propertyBag": {
              "source_app": {
                "key": "source_app",
                "value": "Twitter"
              },
              "source_id": {
                "key": "source_id",
                "value": "95032"
              },
              "chat_id": {
                "key": "chat_id",
                "value": "95032"
              },
              "follow_type": {
                "key": "follow_type",
                "value": "Individual"
              }
            }
          },
          "participants": [
            {
              "name": "Sharon Zhang",
              "identity_id": 2,
              "domain_id": 62,
              "identity_name": null,
              "email": "sharon@personal.ai",
              "propertyBag": {
                "email": {
                  "key": "email",
                  "value": "sharon@personal.ai"
                },
                "picture": {
                  "key": "picture",
                  "value": "2HNYYWHIEI8BISATZLGFVRYYHW8KVG.jpg"
                }
              }
            },
            {
              "name": "Sharon Zhang",
              "identity_id": 2,
              "domain_id": 16112,
              "identity_name": null,
              "email": "sharon@personal.ai",
              "propertyBag": {
                "email": {
                  "key": "email",
                  "value": "sharon@personal.ai"
                },
                "picture": {
                  "key": "picture",
                  "value": "Y9X4OFS9MSSUQEBV908FEY8AFGDP41.jpg"
                }
              }
            },
            {
              "name": "Sharon Zhang",
              "identity_id": 2,
              "domain_id": 16112,
              "identity_name": null,
              "email": "sharon@personal.ai",
              "propertyBag": {
                "email": {
                  "key": "email",
                  "value": "sharon@personal.ai"
                },
                "picture": {
                  "key": "picture",
                  "value": "Y9X4OFS9MSSUQEBV908FEY8AFGDP41.jpg"
                }
              }
            }
          ],
          "location": null,
          "feed_event": [],
          "topics": [
            {
              "value": "pet"
            },
            {
              "value": "cat"
            },
            {
              "value": "meow two"
            },
            {
              "value": "2000"
            }
          ],
          "contexts": [],
          "scope": "PERSONAL",
          "visibility": "PRIVATE",
          "internal_parent_mem_ids": [],
          "external_parent_mem_ids": [],
          "embedUrls": [],
          "metadata": {
            "prompt_type": "request",
            "feed_text": "my cat is born in #2000",
            "route_id": "ai-climbing",
            "participants": "[2]",
            "tags": "[2]",
            "is_stacked": "true"
          },
          "is_session": true,
          "id": "650a5ddeb3a6d353352aed51",
          "cmd": null,
          "time_start": null,
          "time_end": null,
          "top_topics": [],
          "actions": [],
          "scores": {},
          "prompt_id": "",
          "prompt_text": "",
          "text": "",
          "topic_list": {},
          "is_valid_response": true,
          "hint_text": null,
          "hint_suggest": []
        }
      ]
    }
  ],
  "internal_parent_mem_ids": [],
  "external_parent_mem_ids": []
}
```