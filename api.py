import requests
def check_api_response(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 404:
            print("API is reachable. Response content:")
            print(response.json())  # Assuming the response is JSON
        else:
            print(f"Failed to hit the API. Status code: {response.status_code}")
    except request.RequestsException as e:
        print(f"Error occurred while sending request: {e}")

# Example usage:
api_url = "https://reqres.in/api/users/23" # Example API URL
check_api_response(api_url)



import requests
def check_api_responses(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code ==404:
            print("API is reachable")
            print(response.json())
        else:
            print(f"failed to hit api.status code")
    except request.RequestsException as e:
        print(f"error occurred :{e}")
api_url = "https://reqres.in/api/users/23"
check_api_responses(api_url)