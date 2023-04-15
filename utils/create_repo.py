import requests
import json


def create(repo_name:str, description: str, username: str, token: str):
    user_url = "https://api.github.com/user/repos"
    
    payload = {"name": repo_name, "description": description}
    
    headers = {"Authorization": f"token {token}"}
    
    response = requests.post(url=user_url, headers=headers, data=json.dumps(payload))
    
    status_code = response.status_code
    
    if status_code == "201":
        print("Successfully Created Repository")
    else:
        print("Failed to Create Repository")


if __name__ == "__main__":
    create()