f = open('demo.txt',mode='a')
f.write("Writing again!\n")
f.close()

f = open('demo.txt',mode='r')
file_content = f.read()
print(file_content)
f.close()

f = open('demo.txt',mode='r')
file_content = f.readlines()
print(file_content)
f.close()

for line in file_content:
    print(line[:-1])

f = open('demo.txt',mode='r')
print(f.readline())
print(f.readline())
print(f.readline())
f.close()
