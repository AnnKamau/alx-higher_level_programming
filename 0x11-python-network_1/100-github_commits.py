#!/usr/bin/python3
"""
You must use the GitHub API, documentation
https://developer.githu.com/v3/repos/commits/
Prints all commits by: `<sha>: <author name>` (one by line)
"""



if __name__ == '__main__':
    from requests import get
    from sys import argv

    repo = argv[1]
    owner = argv[2]
    w = 0

    URL = "https://developer.githu.com/v3/repos/{}/{}/commits/".format(owner, repo)

    response = get(URL)
    json = response.json()

    for element in json:
        if w > 9:
            break
        sha = element.get('sha')
        author = element.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
        w += 1

