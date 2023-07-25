import copy


string1 = "meow"
string2 = "woof"
strin3 = "chirp"

deeplist = [string1, string2, strin3]
print("deeplist: ", deeplist)

toplist = [deeplist, "moooo"]
print("\ntoplist: ", toplist)

toplist1 = toplist
print("\ntoplist1", toplist1)

toplist2 = toplist[:]
print("\ntoplist2: ", toplist2)

toplist3 = copy.deepcopy(toplist)
print("\ntoplist3: ", toplist3)