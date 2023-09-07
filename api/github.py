import requests
# Define the repository details
owner=""
repo = ""
folder_path = ""
# GitHub API endpoint URL
url = f"https://api.github.com/repos/{owner}/{repo}/contents/{folder_path}"

try:
    # Send a GET request to the GitHub API
    response = requests.get(url)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        data = response.json()

        # Iterate through the folder contents and print their names
        for item in data:
            print(item["name"])

    else:
        print(f"Failed to fetch folder. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
