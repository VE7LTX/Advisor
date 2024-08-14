# src/api_client.py

"""
api_client.py - A client for interacting with the Personal.AI API

This module provides a class, `PersonalAIClient`, that encapsulates the functionality required
to interact with the Personal.AI API. It includes methods for sending various types of API requests
to Personal.AI, such as uploading documents, validating API keys, sending AI messages, and more.

Key Features of the `PersonalAIClient` class:
    - Initialization (`__init__` method):
        - Sets up the API key, base URL, and domain name.
    - Private method `_get_headers`:
        - Prepares the headers for every API call, ensuring that the API key is included.
    - API Methods:
        - Each method corresponds to a specific API call (e.g., `send_external_invite`, `validate_api_key`, `send_ai_message`).
        - Methods include optional parameters where applicable, making them flexible for different use cases.
        - Uses Python's `requests` library to send HTTP requests.
    - Error Handling:
        - Each method uses `response.raise_for_status()` to automatically raise an exception for HTTP errors.
    - Extensibility:
        - The class is designed to be easily extended with additional methods or modified as needed.

Usage Example:
    from api_client import PersonalAIClient

    # Initialize the API client
    client = PersonalAIClient(api_key="your_personal_ai_api_key", domain_name="ai-climbing")

    # Send an AI message
    response = client.send_ai_message(text="Who is Einstein?", user_name="Leila", source_name="slack")
    print(response.json())

    # Upload a memory
    response = client.upload_memory(text="My first memory with Personal AI", source_name="Notes")
    print(response.json())
"""
import requests
import json
import logging
from typing import Optional, Dict, Any
from dotenv import load_dotenv
import os

# Load environment variables from .env file located in the config folder
load_dotenv(dotenv_path=os.path.join('config', '.env'))

# Configure logging based on environment settings
ENABLE_LOGGING = os.getenv('ENABLE_LOGGING', 'false').lower() == 'true'
APP_MODE = os.getenv('APP_MODE', 'development').lower()
LOG_FILE_PATH = os.getenv('LOG_FILE_PATH', './logs/trading_advisor.log')

if ENABLE_LOGGING:
    logging.basicConfig(filename=LOG_FILE_PATH, level=logging.DEBUG if APP_MODE == 'development' else logging.ERROR,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class PersonalAIClient:
    """
    A client for interacting with the Personal.AI API.

    This class provides methods for sending requests to the Personal.AI API, such as
    sending messages to an AI, uploading documents, and validating API keys.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.personal.ai", domain_name: Optional[str] = None):
        """
        Initialize the PersonalAIClient.

        :param api_key: Your Personal.AI API key.
        :param base_url: The base URL for the Personal.AI API (default: https://api.personal.ai).
        :param domain_name: The domain name of your AI persona, if applicable.
        """
        self.api_key = api_key
        self.base_url = base_url
        self.domain_name = domain_name

        if ENABLE_LOGGING and APP_MODE == 'development':
            logging.debug(f"Initialized PersonalAIClient with api_key={api_key}, base_url={base_url}, domain_name={domain_name}")

    def _get_headers(self) -> Dict[str, str]:
        """
        Internal method to generate the headers required for API requests.

        :return: A dictionary of headers including the API key.
        """
        headers = {
            "Content-Type": "application/json",
            "x-api-key": self.api_key
        }

        if ENABLE_LOGGING and APP_MODE == 'development':
            logging.debug(f"Generated headers: {headers}")

        return headers

    def _log_error(self, error: Exception):
        """
        Internal method to log errors based on the application mode.

        :param error: The exception to log.
        """
        if ENABLE_LOGGING:
            if APP_MODE == 'development':
                logging.error(f"Error occurred: {error}", exc_info=True)
            else:
                logging.error(f"Error occurred: {error}")

    def send_external_invite(self, email: str, domain_name: Optional[str] = None) -> requests.Response:
        """
        Send an email invite to a Personal AI or Lounge.

        :param email: The email to send the invitation to.
        :param domain_name: The AI persona domain where the invite will be sent from (optional).
        :return: The response from the API.
        """
        try:
            domain_name = domain_name or self.domain_name
            url = f"{self.base_url}/v1/invite"
            params = {
                "email": email,
                "domain_name": domain_name
            }
            response = requests.post(url, headers=self._get_headers(), params=params)
            response.raise_for_status()
            if ENABLE_LOGGING and APP_MODE == 'development':
                logging.debug(f"Sent external invite to {email} with response: {response.status_code}")
            return response
        except Exception as e:
            self._log_error(e)
            raise

    def validate_api_key(self) -> requests.Response:
        """
        Validate the provided API key.

        :return: The response from the API.
        """
        try:
            url = f"{self.base_url}/v1/api-key/validate"
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()
            if ENABLE_LOGGING and APP_MODE == 'development':
                logging.debug(f"Validated API key with response: {response.status_code}")
            return response
        except Exception as e:
            self._log_error(e)
            raise

    def validate_token(self, token: str, challenge: str) -> requests.Response:
        """
        Validate the provided token and challenge for webhook verification.

        :param token: The token to validate.
        :param challenge: The challenge to validate.
        :return: The response from the API.
        """
        try:
            url = f"{self.base_url}/external/api/webhook/verification"
            params = {
                "token": token,
                "challenge": challenge
            }
            response = requests.get(url, headers=self._get_headers(), params=params)
            response.raise_for_status()
            if ENABLE_LOGGING and APP_MODE == 'development':
                logging.debug(f"Validated token {token} with response: {response.status_code}")
            return response
        except Exception as e:
            self._log_error(e)
            raise

    def send_ai_instruction(self, text: str, context: Optional[str] = None, domain_name: Optional[str] = None,
                            user_name: Optional[str] = None, session_id: Optional[str] = None,
                            source_name: Optional[str] = None, is_stack: bool = False, is_draft: bool = False) -> requests.Response:
        """
        Interact with an AI message by sending an instruction.

        :param text: The message to send to your AI for a response.
        :param context: Additional context for the AI response (optional).
        :param domain_name: The domain part of the AI profile URL (optional).
        :param user_name: The name of the user sending the request (optional).
        :param session_id: The session ID to continue the conversation (optional).
        :param source_name: The source app of the inbound message (optional).
        :param is_stack: Flag to add the user message to memory (default: False).
        :param is_draft: Flag to create a copilot message for the AI (default: False).
        :return: The response from the API.
        """
        try:
            domain_name = domain_name or self.domain_name
            url = f"{self.base_url}/v1/instruction?cmd=search"
            payload = {
                "Text": text,
                "Context": context,
                "DomainName": domain_name,
                "UserName": user_name,
                "SessionId": session_id,
                "SourceName": source_name,
                "is_stack": is_stack,
                "is_draft": is_draft
            }
            response = requests.post(url, headers=self._get_headers(), data=json.dumps(payload))
            response.raise_for_status()
            if ENABLE_LOGGING and APP_MODE == 'development':
                logging.debug(f"Sent AI instruction with text '{text}' and response: {response.status_code}")
            return response
        except Exception as e:
            self._log_error(e)
            raise

    def upload_document(self, text: str, title: Optional[str] = None, start_time: Optional[str] = None,
                        end_time: Optional[str] = None, domain_name: Optional[str] = None,
                        tags: Optional[str] = None, is_stack: bool = True) -> requests.Response:
        """
        Upload a document to your Personal AI memory.

        :param text: The body of text to upload.
        :param title: The title of the uploaded document (optional).
        :param start_time: ISO timestamp string indicating start time (optional).
        :param end_time: ISO timestamp string indicating end time (optional).
        :param domain_name: The domain name of the AI persona to upload to (optional).
        :param tags: Comma-delimited list of tags for the document (optional).
        :param is_stack: Whether to add the document to memory or as a draft (default: True).
        :return: The response from the API.
        """
        try:
            domain_name = domain_name or self.domain_name
            url = f"{self.base_url}/v1/upload-text"
            payload = {
                "Text": text,
                "Title": title,
                "StartTime": start_time,
                "EndTime": end_time,
                "DomainName": domain_name,
                "Tags": tags,
                "is_stack": is_stack
            }
            response = requests.post(url, headers=self._get_headers(), data=json.dumps(payload))
            response.raise_for_status()
            if ENABLE_LOGGING and APP_MODE == 'development':
                logging.debug(f"Uploaded document with title '{title}' and response: {response.status_code}")
            return response
        except Exception as e:
            self._log_error(e)
            raise

    def upload_url(self, url_to_upload: str, title: Optional[str] = None, start_time: Optional[str] = None,
                   end_time: Optional[str] = None, domain_name: Optional[str] = None,
                   tags: Optional[str] = None, is_stack: bool = True) -> requests.Response:
        """
        Upload a URL to your Personal AI memory.

        :param url_to_upload: The URL to upload.
        :param title: The title of the uploaded document (optional).
        :param start_time: ISO timestamp string indicating start time (optional).
        :param end_time: ISO timestamp string indicating end time (optional).
        :param domain_name: The domain name of the AI persona to upload to (optional).
        :param tags: Comma-delimited list of tags for the document (optional).
        :param is_stack: Whether to add the document to memory or as a draft (default: True).
        :return: The response from the API.
        """
        try:
            domain_name = domain_name or self.domain_name
            url = f"{self.base_url}/v1/upload"
            payload = {
                "Url": url_to_upload,
                "Title": title,
                "StartTime": start_time,
                "EndTime": end_time,
                "DomainName": domain_name,
                "Tags": tags,
                "is_stack": is_stack
            }
            response = requests.post(url, headers=self._get_headers(), data=json.dumps(payload))
            response.raise_for_status()
            if ENABLE_LOGGING and APP_MODE == 'development':
                logging.debug(f"Uploaded URL '{url_to_upload}' with response: {response.status_code}")
            return response
        except Exception as e:
            self._log_error(e)
            raise

    def send_ai_message(self, text: str, context: Optional[str] = None, domain_name: Optional[str] = None,
                        user_name: Optional[str] = None, session_id: Optional[str] = None,
                        source_name: Optional[str] = None, is_stack: bool = False, is_draft: bool = False) -> requests.Response:
        """
        Send a message to your AI for a response.

        :param text: The message to send to your AI.
        :param context: Additional context for the AI response (optional).
        :param domain_name: The domain part of the AI profile URL (optional).
        :param user_name: The name of the user sending the request (optional).
        :param session_id: The session ID to continue the conversation (optional).
        :param source_name: The source app of the inbound message (optional).
        :param is_stack: Flag to add the user message to memory (default: False).
        :param is_draft: Flag to create a copilot message for the AI (default: False).
        :return: The response from the API.
        """
        try:
            domain_name = domain_name or self.domain_name
            url = f"{self.base_url}/v1/message"
            payload = {
                "Text": text,
                "Context": context,
                "DomainName": domain_name,
                "UserName": user_name,
                "SessionId": session_id,
                "SourceName": source_name,
                "is_stack": is_stack,
                "is_draft": is_draft
            }
            response = requests.post(url, headers=self._get_headers(), data=json.dumps(payload))
            response.raise_for_status()
            if ENABLE_LOGGING and APP_MODE == 'development':
                logging.debug(f"Sent AI message with text '{text}' and response: {response.status_code}")
            return response
        except Exception as e:
            self._log_error(e)
            raise

    def upload_memory(self, text: str, created_time: Optional[str] = None, source_name: Optional[str] = None,
                      raw_feed_text: Optional[str] = None, domain_name: Optional[str] = None,
                      tags: Optional[str] = None) -> requests.Response:
        """
        Upload text memories to your Personal AI memory stack.

        :param text: The plain text memory to upload.
        :param created_time: Time (including timezone) of the memory to help recall when it is from (optional).
        :param source_name: The source or application of the memory to help recall where it is from (required).
        :param raw_feed_text: The formatted text that can be stored as is (optional).
        :param domain_name: The AI persona where the memory will be uploaded (optional).
        :param tags: Comma delimited list of tags for the memory (optional).
        :return: The response from the API.
        """
        try:
            domain_name = domain_name or self.domain_name
            url = f"{self.base_url}/v1/memory"
            payload = {
                "Text": text,
                "CreatedTime": created_time,
                "SourceName": source_name,
                "RawFeedText": raw_feed_text,
                "DomainName": domain_name,
                "Tags": tags
            }
            response = requests.post(url, headers=self._get_headers(), data=json.dumps(payload))
            response.raise_for_status()
            if ENABLE_LOGGING and APP_MODE == 'development':
                logging.debug(f"Uploaded memory with text '{text}' and response: {response.status_code}")
            return response
        except Exception as e:
            self._log_error(e)
            raise
