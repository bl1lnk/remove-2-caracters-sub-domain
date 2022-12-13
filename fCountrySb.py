try:
    file = input("Enter your file path:")
except:
    print("wrong file path")
    file = input("Enter your file path:")

result=open("result.txt","w")
with open(file) as f:
    for line in f:
        line=line.rstrip("\n")
        fltr=line.split("//")[1]
        if(len(fltr.split(".")[0]) > 2):
            result.write(line+"\n")
            print(line)
result.close()
