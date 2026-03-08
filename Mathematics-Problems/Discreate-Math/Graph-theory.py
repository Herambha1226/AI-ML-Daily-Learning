# Social Network which is recomended the friends of friends
friends =  {
    "Alice" : {"Bob","Charlie"},
    "Bob" : {"Alice","David"},
    "Charlie" : {"Alice"},
    "David" : {"Bob"}
}

def friends_of_friends(graph,user):
    fof = set()
    for friend in graph[user]:
        fof |= graph[friend]
    fof.discard(user)
    fof -= graph[user]
    return fof
print(friends_of_friends(friends,"Alice"))
