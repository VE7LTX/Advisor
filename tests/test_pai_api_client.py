import unittest
from unittest.mock import patch, Mock
from src.pai_api_client import PersonalAIClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file located in the config folder
load_dotenv(dotenv_path=os.path.join('config', '.env'))

class TestPersonalAIClient(unittest.TestCase):
    """
    Unit tests for the PersonalAIClient class.
    """

    def setUp(self):
        """
        Set up the test environment by initializing the PersonalAIClient with test data.
        """
        self.api_key = os.getenv('PERSONAL_AI_API_KEY')
        self.domain_name = os.getenv('PERSONAL_AI_DOMAIN_NAME')
        self.client = PersonalAIClient(api_key=self.api_key, domain_name=self.domain_name)

    @patch('src.pai_api_client.requests.post')
    def test_send_external_invite(self, mock_post):
        """
        Test the send_external_invite method of the PersonalAIClient class.
        """
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        response = self.client.send_external_invite(email="test@example.com")
        self.assertEqual(response.status_code, 200)
        mock_post.assert_called_once()

    @patch('src.pai_api_client.requests.get')
    def test_validate_api_key(self, mock_get):
        """
        Test the validate_api_key method of the PersonalAIClient class.
        """
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.client.validate_api_key()
        self.assertEqual(response.status_code, 200)
        mock_get.assert_called_once()

    @patch('src.pai_api_client.requests.get')
    def test_validate_token(self, mock_get):
        """
        Test the validate_token method of the PersonalAIClient class.
        """
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.client.validate_token(token="test_token", challenge="test_challenge")
        self.assertEqual(response.status_code, 200)
        mock_get.assert_called_once()

    @patch('src.pai_api_client.requests.post')
    def test_send_ai_message(self, mock_post):
        """
        Test the send_ai_message method of the PersonalAIClient class.
        """
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        response = self.client.send_ai_message(text="Hello AI")
        self.assertEqual(response.status_code, 200)
        mock_post.assert_called_once()

    @patch('src.pai_api_client.requests.post')
    def test_upload_memory(self, mock_post):
        """
        Test the upload_memory method of the PersonalAIClient class.
        """
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        response = self.client.upload_memory(text="This is a test memory", source_name="TestSource")
        self.assertEqual(response.status_code, 200)
        mock_post.assert_called_once()

if __name__ == '__main__':
    unittest.main()

