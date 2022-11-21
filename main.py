import glob

unifiedFile = []
# All files and directories ending with .txt and that don't begin with a dot:
nameOfFiles = glob.glob("./*.txt")

def search(list, element):
    for i in range(len(list)):
        if list[i] == element:
            return True
    return False

for nameOfFile in nameOfFiles:
    nameOfFile=(nameOfFile[2:])
    file = open(nameOfFile, 'r')
    print("In file: "+nameOfFile)
    # Read file
    lines = file.readlines()
    count = 0
    # Strips the newline character
    for line in lines:
        count += 1
        print("Line{}: {}".format(count, line.strip()), end=" ")
        if search(unifiedFile, line.strip()):
            print(" is found")
        else:
            print(" does not found")
            unifiedFile.append(line.strip())

#Print efect
print("unifiedFile: ")
print(unifiedFile)

with open(r'./unifiedFile.txt', 'w') as fp:
    fp.write('\n'.join(unifiedFile))


