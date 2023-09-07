import os
import requests

def Github(url):
    # GitHub API endpoint URL for the folder
    url = url

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            # Iterate through the folder contents and download each file
            for item in data:
                if item["type"] == "file" and item["name"].endswith(".md"):
                    file_url = item["download_url"]
                    file_name = os.path.join("../data", item["name"])

                    # Download the file
                    file_response = requests.get(file_url)

                    if file_response.status_code == 200:
                        with open(file_name, 'wb') as f:
                            f.write(file_response.content)
                            print(f"Downloaded: {file_name}")
                    else:
                        print(f"Failed to download file: {file_name}")
        else:
            print(f"Failed to fetch folder. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
