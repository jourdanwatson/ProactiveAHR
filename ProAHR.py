## Open and read the file
file = open("recs.txt", "r")

global lines
lines=file.readlines()


##for line in lines:
##    rec_split=line.split(",")
##    print("• " + rec_split[0])
##    print("    •" + rec_split[1])
##    print("    •" + rec_split[2]) 

def sub_index(sub):
    for index in range(0,len(lines)):
        if lines[index].find(sub)!=-1:
            return index
    
def print_recs(list_recs):
    for index in range(0,len(list_recs)):
        sub=list_recs[index]
        print("sub: ", sub)
        rec_index=sub_index(sub)
        print("rec index: ", rec_index)
        ##rec_index=lines.index(list_recs[index])
       ## print(index, " : ", rec_index)

##Input the recommendations and parse them
print("What are your recommendations? (Separate with comma)")
recs = input().lower()
print(recs)
list_recs=recs.split(",")


print_recs(list_recs)


