import json
import os

def get_json_file_abspath() -> str:
    """Return the absolute path to the 'util.json' file."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, '..', 'util.json')

def get_api_key(api_name : str) -> str:
    """
    Retrieve the API key for a given api_name from 'util.json'.
    
    Args:
        api_name (str): The name of the API.

    Returns:
        str or None: The API key if found, otherwise None.
    """
    file_path = get_json_file_abspath()
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            api_key = data.get(f'{api_name}_api_key')
            if api_key is not None:
                return api_key
            else:
                print(f"API key for '{api_name}' not found.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {file_path}")
    except Exception as e:
        print(f"An unknown error occurred: {e}")

    return None
