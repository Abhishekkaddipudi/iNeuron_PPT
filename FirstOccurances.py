def FirstUniqueString(string:list)->list:
    
    """
    returns index of first non-repeating character else return -1
    """
    HashMap={}
    n=len(string)
    for i in string:
        if i in HashMap:
            HashMap[i]+=1
        else:
            HashMap[i]=1
    for index in range(n):
        if HashMap[string[index]]==1:
            return index
            
    return -1