mydict = {"IND":[8, 1.391], "PAK":[6, 1.028], "SA":[5,0.874], "NED":[4,-0.849], "BAN":[4,-1.176], "ZIM":[3,-1.138]}

def sortdict(dictionary):
    var = sorted(dictionary.items(), key= lambda x:(x[1][0], x[1][1]), reverse=True)
    return dict(var)
print(sortdict(mydict))
