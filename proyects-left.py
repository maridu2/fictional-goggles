from github import Github

prs = Github().search_issues(query="author:maridu2 is:pr")

print("Para conseguir la mega camisetilla que te reconoce oficialmente como un hacker of the world te queda por completar un " + str(int((4 - prs.totalCount) * 100 / 4)) + "% de Pull Requests")
