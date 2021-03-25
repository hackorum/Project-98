def swapFileData():
    firstFile = input("Enter the first file: ")
    secondFile = input("Enter the second file: ")
    # print(firstFile, secondFile)
    with open(firstFile, 'r') as file1:
        file1data = file1.read()
    with open(secondFile, 'r') as file2:
        file2data = file2.read()

    with open(firstFile, 'w') as file1:
        file1.write(file2data)
    with open(secondFile, 'w') as file2:
        file2.write(file1data)

    print('Files Swapped!')


swapFileData()
