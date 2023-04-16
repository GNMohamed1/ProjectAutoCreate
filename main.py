import sys
import requests
import json
import os

def main():
    repo_name = str(sys.argv[1])
    description = str(sys.argv[2])
    token = str(sys.argv[3])
    main_dir = str(sys.argv[4])
    private = bool(sys.argv[5])
    
    create_directory(main_directory=main_dir, filename=repo_name)
    
    create_repo(repo_name,description,token,private)

def create_directory(main_directory, filename) -> None:
    path = os.path.join(main_directory, filename)
    if not os.path.exists(path):
        os.makedirs(path)
        print("Successfully created directory %s" % path)
        return
    
    print("Directory %s already exists" % path)

def create_repo(repo_name:str, description: str, token: str, private:bool):
    user_url = "https://api.github.com/user/repos"
    
    visibility = "public" if not private else "private"
    
    payload = {"name": repo_name, "description": description, "visibility": visibility}
    
    headers = {"Authorization": f"token {token}"}
    
    response = requests.post(url=user_url, headers=headers, data=json.dumps(payload))
    
    status_code = response.status_code
    
    if status_code == 201:
        print("Successfully Created Repository")
    else:
        print("Failed to Create Repository")


if __name__ == "__main__":
    main()
