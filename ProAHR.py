## Open and read the file
file = open("recs.txt", "r")


lines=file.readlines()
for line in lines:
    print(line)
    rec_split=line.split(",")
    print("• " + rec_split[0])
    print("    •" + rec_split[1])
    print("    •" + rec_split[2]) 


##Input the recommendations and parse them
##print("What are your recommendations? (Separate with comma)")
##recs = input()
##print(recs)
##list_recs=recs.split(",")
##print(list_recs)



