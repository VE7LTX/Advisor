# Trading Advisor

## Overview
Trading Advisor is a Python-based application designed to provide AI-driven trading advice based on market data and analysis. The application integrates with various financial APIs to fetch real-time data, process it, and generate trading recommendations using advanced algorithms and AI models.

## Features
- **AI-Driven Analysis:** Utilizes Personal.AI agents to analyze market data and provide tailored trading recommendations.
- **Real-Time Data Integration:** Fetches real-time market data from multiple sources via APIs.
- **Modular Design:** Clean, modular codebase, allowing for easy updates and enhancements.
- **Secure API Access:** Managed access to API keys and other sensitive information, ensuring security and privacy.

## AI Integration with Personal.AI Agents
Trading Advisor is powered by **Personal.AI** agents, which deliver personalized trading insights based on cutting-edge artificial intelligence technologies. Users can access these AI-driven features through a subscription model:

- **Monthly Subscription:** Access to AI-driven trading advice is available to any user who subscribes to the monthly plan.
- **API Access:** Subscribers will receive API keys, granting them the ability to integrate their own data sources or customize the AI's behavior to suit their personal trading strategies.

## Features
- Fetches real-time market data from APIs
- Analyzes data to provide trading recommendations
- Modular and extensible codebase
- Secure management of API keys and other sensitive information

## Project Structure
```plaintext
advisor/
│
├── config/
│   ├── settings.py        # General configuration settings
│   ├── .env               # Encrypted or access-controlled file for API keys and sensitive data
│   ├── .env.template      # Template file for environment variables (Rename to .env)
│   ├── __init__.py        # Makes config a package
│
├── data/
│   ├── raw/               # Raw data files, if any
│   ├── processed/         # Processed data files, if any
│
├── logs/
│   ├── *.log              # Log files for tracking application behavior and errors
│
├── src/
│   ├── __init__.py        # Makes src a package
│   ├── main.py            # Entry point of your application
│   ├── advisor.py         # Core logic for trading advice
│   ├── data_handler.py    # Functions for handling data
│   ├── pai_api_client.py  # Interactions with the Personal AI APIs (e.g., sending messages, uploading documents)
│   ├── data_api_client.py # Interactions with Forex and Crypto APIs (e.g., fetching market data)
│   ├── misc_api_client.py # Interactions with other APIs (e.g., additional data sources)
│   ├── utils.py           # Utility functions and helpers
│
├── tests/
│   ├── __init__.py        # Makes tests a package
│   ├── test_advisor.py    # Unit tests for advisor.py
│   ├── test_api_client.py # Unit tests for api_client.py
│   ├── ...                # Additional test files
│
├── notebooks/
│   ├── exploration.ipynb  # Jupyter notebooks for exploratory analysis
│
├── personal_ai_documentation/
│   ├── POST_External_Invite.md       # Documentation for the POST /invite API call
│   ├── GET_Validate_Token.md         # Documentation for the GET /api-key/validate API call
│   ├── GET_Validate_API-KEY.md       # Documentation for the GET /api-key/validate API call
│   ├── POST_AI_Instruction.md        # Documentation for the POST /instruction API call
│   ├── POST_Upload_Document.md       # Documentation for the POST /upload-text API call
│   ├── POST_Upload_URL.md            # Documentation for the POST /upload API call
│   ├── POST_AI_Message.md            # Documentation for the POST /message API call
│   ├── POST_AI_Memory.md             # Documentation for the POST /memory API call
│
├── requirements.txt       # List of dependencies (output from `pip freeze`)
├── .gitignore             # Files and directories to ignore in git (e.g., .env, secrets.json, __pycache__/)
├── README.md              # Project overview and setup instructions
└── LICENSE                # License for your project

```

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/VE7LTX/advisor.git
    ```

2. 
    **Create and activate a virtual environment in Linux:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
    **Create and activate a virtual environment in Windows:**
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```sh
    python.exe -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

## Usage

1. **Set up your API keys and other credentials in `config/.env`.**

2. **Configure settings in `config/settings.py`.**

3. **Run the application:**
    ```sh
    python src/main.py
    ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](./LICENSE) file for details.

## Acknowledgments

Thank you to all the open-source contributors who helped in my education and making this project possible.
