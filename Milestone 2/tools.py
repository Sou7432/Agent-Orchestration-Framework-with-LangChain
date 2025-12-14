import requests
from langchain.tools import Tool
from exceptions import ToolInputError, ToolExecutionError
# -----------------------------
# Tool 1: Unit Converter
# -----------------------------
def unit_converter(query: str):
    """
    Query format: '10 km to miles'
    """
    try:
        amount, from_unit, _, to_unit = query.split()

        amount = float(amount)

        # Simple conversion table
        conversions = {
            ("km", "miles"): 0.621371,
            ("miles", "km"): 1.60934,
            ("kg", "lbs"): 2.20462,
            ("lbs", "kg"): 0.453592,
        }

        key = (from_unit, to_unit)

        if key not in conversions:
            raise ToolInputError("Conversion not supported.")

        result = amount * conversions[key]
        return f"{amount} {from_unit} = {result:.2f} {to_unit}"

    except ValueError:
        raise ToolInputError("Invalid format. Use: '10 km to miles'.")
    except Exception as e:
        raise ToolExecutionError(str(e))


unit_converter_tool = Tool(
    name="unit_converter",
    func=unit_converter,
    description="Convert units. Example: '10 km to miles'"
)
# -----------------------------
# Tool 2: Random Joke Tool
# -----------------------------
def random_joke(_):
    try:
        url = "https://official-joke-api.appspot.com/random_joke"
        res = requests.get(url).json()
        return f"{res['setup']} - {res['punchline']}"
    except:
        raise ToolExecutionError("Unable to fetch a joke at the moment.")


joke_tool = Tool(
    name="joke_tool",
    func=random_joke,
    description="Returns a random joke."
)


# Export all tools
tools = [unit_converter_tool, joke_tool]
