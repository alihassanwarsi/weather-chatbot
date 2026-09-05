# SkyCast AI

A simple AI powered weather chatbot that uses Gemini and WeatherAPI to provide current weather information through a Streamlit interface.

## Tech Stack

* Python
* Google Gemini
* WeatherAPI
* Streamlit
* Requests
* python-dotenv

## Features

* Conversational weather assistant
* Current weather lookup by location
* Gemini tool/function calling
* Temperature, condition, humidity, and wind information
* Streamlit chat interface
* Environment variable configuration

## Project Structure

```text
weather-chatbot/
├── chatbot.py
├── ui.py
├── system_prompt.txt
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
WEATHER_API_KEY=your_weather_api_key
```

## Run the Application

Start the Streamlit application:

```bash
streamlit run ui.py
```

The application will open in your browser.

## Example Queries

* What's the weather in Karachi?
* Is it raining in London?
* What's the temperature in Tokyo?
* How windy is it in Dubai?

## How It Works

```text
User
  ↓
Streamlit UI
  ↓
Gemini
  ↓
get_current_weather()
  ↓
WeatherAPI
  ↓
Weather Data
  ↓
Gemini Response
```

Gemini uses the `get_current_weather` tool when the user asks for weather information about a specific location. The tool retrieves current weather data from WeatherAPI, which is then used to generate the response.

## APIs

### Google Gemini

Used as the language model for understanding user requests and generating responses.

### WeatherAPI

Used to retrieve current weather information for a requested location.
