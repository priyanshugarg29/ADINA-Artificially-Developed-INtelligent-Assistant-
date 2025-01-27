#analyzeWolframBasedSearches

def analyzeWolframBasedSearches(query):
    from accessUserAttributes import accessUserAttributes
    user_attributes = accessUserAttributes()
    if "what" in query:
        for i in range  (0, int(len(user_attributes))):
            if "what" in user_attributes[i]:
                user_attributes[i][1]+=1
    if "why" in query:
        for i in range  (0, int(len(user_attributes))):
            if "why" in user_attributes[i]:
                user_attributes[i][1]+=1
    if "how" in query:
        for i in range  (0, int(len(user_attributes))):
            if "how" in user_attributes[i]:
                user_attributes[i][1]+=1
    if "does" in query:
        for i in range  (0, int(len(user_attributes))):
            if "does" in user_attributes[i]:
                user_attributes[i][1]+=1
    from updateUserAttributes import updateUserAttributes
    updateUserAttributes(user_attributes)
    
