try:
    file = input("Enter your file path:")
except:
    print("wrong file path")
    file = input("Enter your file path:")
    
result=open(file,"w")
with open("live_domain") as f:
    for line in f:
        line=line.rstrip("\n")
        fltr=line.split("//")[1]
        if(len(fltr.split(".")[0]) > 2):
            result.write(line+"\n")
            print(line)
result.close()
