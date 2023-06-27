from git import Repo

def git_repo_clone(source_path,local_path):
    try:
        # if local_path is None:
            Repo.clone_from(source_path,local_path)
            print(f"Cloned Sucessfully to local path {local_path}")
        # else:
            # print("Data Already Available")
    except Exception as e:
        print(f"The error found is : str{e}") 
    
    
    
source_path = 'https://github.com/PhonePe/pulse.git'
local_path = "D:\Phonepe"    
git_repo_clone(source_path,local_path)    