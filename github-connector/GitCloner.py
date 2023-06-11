# by Jakub Wawak
# kubawawak@gmail.com
# all rights reserved


import git
import time
from git import RemoteProgress


# object for showing progress in terminal
class CloneProgress(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        if message:
            print(message)


# object for cloning given repository to given directory
class GitCloner:
    source_url = ""
    source_path = ""
    fa_token = ""
    repository_private = 0
    github_user_login = ""

    # constructor
    def __init__(self, source_url, source_path, fa_token, repository_private,github_user_login):
        self.source_path = source_path
        self.source_url = source_url
        self.fa_token = fa_token
        self.repository_private = repository_private
        self.github_user_login = github_user_login

    # function for downloading repository to computer and store in folder
    def download(self):
        if self.repository_private == 0:
            # repository is not private
            git.Repo.clone_from(self.source_url, self.source_path,
                                branch='master', progress=CloneProgress())
        else:
            pass
