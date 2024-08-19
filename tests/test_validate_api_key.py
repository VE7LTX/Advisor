import os
import requests
import json
from dotenv import load_dotenv
from typing import Dict, Any

class PersonalAIValidator:
    """
    A class to validate the Personal.AI API key.
    """

    def __init__(self, config_path: str = '../config/.env'):
        """
        Initialize the validator by loading environment variables.

        :param config_path: Path to the .env file containing environment variables.
        """
        # * Load environment variables from .env file located in the config folder
        load_dotenv(dotenv_path=config_path)
        
        # * Debug: Print the loaded environment variables (excluding sensitive information)
        print("Loaded Environment Variables:")
        print("PERSONAL_AI_BASE_URL:", os.getenv('PERSONAL_AI_BASE_URL'))
        print("PERSONAL_AI_API_KEY:", "***" + os.getenv('PERSONAL_AI_API_KEY')[-4:])

    def validate_api_key(self) -> Dict[str, Any]:
        """
        Validate the provided API key to ensure it is correct and active.

        :return: A dictionary containing the validation status and user information if successful.
        """
        url = f"{os.getenv('PERSONAL_AI_BASE_URL')}/v1/api-key/validate"
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': os.getenv('PERSONAL_AI_API_KEY')
        }

        try:
            # * Debug: Print the request details (excluding sensitive information)
            print("Request URL:", url)
            print("Request Headers: {'Content-Type': 'application/json', 'x-api-key': '***" + os.getenv('PERSONAL_AI_API_KEY')[-4:] + "'}")

            response = requests.get(url, headers=headers)
            
            # * Debug: Print the full response details
            print(f"Response Status Code: {response.status_code}")
            print(f"Response Headers: {response.headers}")
            print(f"Response Body: {response.text}")

            response.raise_for_status()  # ! Raise an exception for HTTP errors
            
            # * Return the full JSON response for detailed information
            if response.content:
                try:
                    json_response = response.json()
                    print("Parsed JSON Response:", json.dumps(json_response, indent=4))
                except ValueError:
                    # ! Handle JSON decoding error
                    return {"validation": "failed", "error": "Invalid JSON response", "response_body": response.text}
                
                validation_status = json_response.get("validation", "failed")
                
                # ! Check if validation failed despite a 200 status code
                if validation_status != "success":
                    return {"validation": "failed", "error": "Validation failed despite 200 status code, Unable to Return Data for Validation.", "response_body": json_response}
                
                return {
                    "validation": validation_status,
                    "firstName": json_response.get("firstName"),
                    "lastName": json_response.get("lastName"),
                    "email": json_response.get("email"),
                    "response_body": json_response
                }
            else:
                return {"validation": "failed", "error": "Empty response", "response_body": None}
        except requests.exceptions.RequestException as e:
            # ! Print detailed error information
            print(f"An error occurred while validating the API key: {e}")
            print(f"URL: {url}")
            print(f"Headers: {{'Content-Type': 'application/json', 'x-api-key': '***{os.getenv('PERSONAL_AI_API_KEY')[-4:]}'}}")
            return {"validation": "failed", "error": str(e), "response_body": None}

# ! Example usage with proper error handling and detailed output
try:
    validator = PersonalAIValidator()
    validation_response = validator.validate_api_key()
    print("Validation Response:", validation_response)
except Exception as e:
    # ! Print detailed error information if the validation process fails
    print(f"An error occurred during the validation process: {e}")