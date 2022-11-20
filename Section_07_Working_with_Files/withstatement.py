with open('demo.txt',mode='r') as f:
    line=f.readline()
    while line:
        print(line)
        line = f.readline()
    print("File is closed:",f.closed)
print("done")
print("FIle is closed:",f.closed)        