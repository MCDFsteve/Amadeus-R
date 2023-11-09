__version__ = "1.0.0"

# Import required libraries
import requests
import json
def get_url_from_server(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                return None
        except Exception as e:
            print("连接失败：", e)
            return None
def get_gpt(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                return None
        except Exception as e:
            print("连接失败：", e)
            return None
# Define the completion function that takes messages and an API key as input
def completion(messages, api_key="", proxy=''):
    # Set the API endpoint URL for ChatGPT completions
    url = get_url_from_server('http://api.dfsteve.top/api_url')

    # If a proxy is set, then it should use that instead
    if proxy is not None and proxy != '': url = proxy

    # Set the headers for the API request, including the Content-Type and Authorization with the API key
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Set the data for the API request, including the model and the input messages
    data = {
        "model": "gpt-3.5-turbo",
        "messages": messages
    }

    # Send the API request using the POST method, passing the headers and the data as JSON
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check if the response status code is 200 (successful)
    if response.status_code == 200:
        # Extract the message from the response JSON and append it to the messages list
        completion = response.json()["choices"][0]["message"]
        messages.append(completion)
        return messages  # Return the updated messages list
    else:
        # If the status code is not 200, raise an exception with the error details
        raise Exception(f"Error: {response.status_code}, {response.text}")
