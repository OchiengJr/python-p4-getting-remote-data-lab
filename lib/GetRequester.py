import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """
        Fetches the raw response body from the given URL.

        Returns:
            bytes: The raw response content in bytes.

        Raises:
            requests.exceptions.RequestException: If an error occurs during the request.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise HTTPError for bad responses
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def load_json(self):
        """
        Converts the response body from the URL to a JSON object.

        Returns:
            dict or list: The JSON response parsed into a Python dictionary or list.

        Raises:
            json.JSONDecodeError: If the response body is not valid JSON.
        """
        response_body = self.get_response_body()
        if response_body:
            try:
                return json.loads(response_body)
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e}")
                return None
        return None

# Example usage:
if __name__ == "__main__":
    url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
    requester = GetRequester(url)

    response_body = requester.get_response_body()
    if response_body:
        print("Response Body:")
        print(response_body)

    json_data = requester.load_json()
    if json_data:
        print("JSON Data:")
        print(json.dumps(json_data, indent=2))
