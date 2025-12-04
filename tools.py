# tools.py

import requests
from langchain.tools import Tool

# Tool 1 - Greeting
def greet(name: str):
    return f"Hello {name}, I am your LangChain Agent!"

# Tool 2 - Weather
def weather(city: str):
    url = f"https://wttr.in/{city}?format=j1"
    res = requests.get(url).json()
    temp = res["current_condition"][0]["temp_C"]
    return f"Current temperature in {city} is {temp}°C"

# Convert into LangChain Tools
greet_tool = Tool(
    name="greeting_tool",
    func=greet,
    description="Use this to greet a person by name."
)

weather_tool = Tool(
    name="weather_tool",
    func=weather,
    description="Get current temperature of a city."
)

# Export list of tools
tools = [greet_tool, weather_tool]
