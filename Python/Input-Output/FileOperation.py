# Writing to a file

text = "This is my first txt file \nLet there be joy"
writeFile = open('sampleFile.txt','w')
writeFile.write(text)
writeFile.close()


# Appending to a file
appendTxt = "Appending this text"
appendFile = open('sampleFile.txt','a')
appendFile.write('\n')
appendFile.write(appendTxt)
appendFile.close()


# Reading from a file
readFile = open('sampleFile.txt','r').read()
readLine = open('sampleFile.txt','r').readlines()
print(readFile)
print(readLine)
