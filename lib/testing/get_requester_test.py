import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)


class GetRequesterTest:
    '''Class GetRequesterTest in test_get_requester.py'''

    URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
    JSON_STRING = b"[\n  {\n    \"name\": \"Daniel\",\n    \"occupation\": \"LG Fridge Salesman\"\n  },\n  {\n    \"name\": \"Joe\",\n    \"occupation\": \"WiFi Fixer\"\n  },\n  {\n    \"name\": \"Avi\",\n    \"occupation\": \"DJ\"\n  },\n  {\n    \"name\": \"Howard\",\n    \"occupation\": \"Mountain Legend\"\n  }\n]\n"
    CONVERTED_DATA = [
        {'name': 'Daniel', 'occupation': 'LG Fridge Salesman'},
        {'name': 'Joe', 'occupation': 'WiFi Fixer'},
        {'name': 'Avi', 'occupation': 'DJ'},
        {'name': 'Howard', 'occupation': 'Mountain Legend'}
    ]

    @staticmethod
    def test_get_response():
        '''get_response_body function returns response.'''
        requester = GetRequester(GetRequesterTest.URL)
        assert requester.get_response_body() == GetRequesterTest.JSON_STRING, \
            f"Expected {GetRequesterTest.JSON_STRING}, but got {requester.get_response_body()}"

    @staticmethod
    def test_load_json():
        '''load_json function returns response.'''
        requester = GetRequester(GetRequesterTest.URL)
        assert requester.load_json() == GetRequesterTest.CONVERTED_DATA, \
            f"Expected {GetRequesterTest.CONVERTED_DATA}, but got {requester.load_json()}"

# Running the tests
if __name__ == "__main__":
    test = GetRequesterTest()
    test.test_get_response()
    test.test_load_json()
    print("All tests passed!")
