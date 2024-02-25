import requests

class GitHubApi():
    
    headers = {
        'Authorization': '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',
        "request_id": "C6C4:13B1B6:1BBA2DD:1DF162E:65DBCCEF"
    }

    user_endpoint = "https://api.github.com/users/{}"
    commits_endoint = "https://api.github.com/users/{}/events/public"
    username = ""


    def getUser(self, username):
        
        self.username = username
        
        r = requests.get(self.user_endpoint.format(self.username), headers= self.headers)
        r = r.json()
        
        user_info = {
            "username":r["login"],
            "full_name":r["name"],
            "location":r["location"],
            "bio":r["bio"],
            "avatar_url":r["avatar_url"],
            "repos":r["repos_url"],
        }
        
        return user_info


    def getLastCommits(self, username, number):
        
        self.username = username
        
        r = requests.get(self.commits_endoint.format(self.username), headers=self.headers)
        
        push_list = [x for x in r.json() if x["type"]== "PushEvent"]
        push_list = push_list[:number]
        
        last_commits_info = []
        
        for push in push_list:
            
            commit_url = push["payload"]["commits"][0]["url"]
            email, commit_html = self.getCommitAdditionalInfo(commit_url)
            repo_html = self.getRepoHtmlUrl(push["repo"]["url"])
            
            commit = {
                "username":push["actor"]["display_login"],
                "email":email,
                "repo_name":push["repo"]["name"],
                "repo_url":repo_html,
                "commit_message":push["payload"]["commits"][0]["message"],
                "commit_url":commit_html,
                "commit_date":push["created_at"]
            }
            
            last_commits_info.append(commit)
        
        return last_commits_info


    def getCommitAdditionalInfo(self, api_commit_url):
        
        r = requests.get(api_commit_url, headers=self.headers)
        r = r.json()
        
        return (r["commit"]["author"]["email"], r["html_url"])
    
    def getRepoHtmlUrl(self, api_repo_url):
        
        r = requests.get(api_repo_url, headers=self.headers)
        r = r.json()
        
        return (r["html_url"])





