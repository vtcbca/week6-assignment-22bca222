
# 1. Read Python.txt file and Print it in Reverse.

with open('C:\\22bca222\\python\\SQLITE3\\python.txt','r') as file:
    file_read=file.read()
    print(file_read)

f1=open('C:\\22bca222\\python\\SQLITE3\\pyt_rev.txt','w',newline='')
with open('C:\\22bca222\\python\\SQLITE3\\python.txt','r') as file:
    read_text=file.read()
file_rev=  read_text[::-1]
f1.write(file_rev)
f1.close()

with open('C:\\22bca222\\python\\SQLITE3\\pyt_rev.txt','r') as f:
    read_txt=f.read()
    print(read_txt)

# 2.Read Python.txt file and Print total number of lines and words in it.

with open('C:\\22bca222\\python\\SQLITE3\\python.txt','r') as file:
    file_read=file.read()
    print(file_read)

with open('C:\\22bca222\\python\\SQLITE3\\python.txt','r') as file:
    lines = len(file.readlines())
    print('Total Number of lines:', lines)

w = 0 
with open('C:\\22bca222\\python\\SQLITE3\\python.txt','r') as file:
    data = file.read()
    lines = data.split()
    print(lines)
    w += len(lines)
print("Total Number Of Words : ",w)

#  3.Read Python.txt file and Print unique word with its count.

with open('C:\\22bca222\\python\\SQLITE3\\python.txt','r') as file:
    data= file.read()
    split_word = data.split()
    for i in set(split_word):
        print(i)
    print("\nTotal No Of Unique Word :: {}".format(len(set(split_word))))

# 4.Read Python.txt file and Print largest and smallest word from it.

# 5.Read Python.txt file. Convert it into upper case and write into another file "Python_Upper.txt"

f1=open('C:\\22bca222\\python\\SQLITE3\python_upper.txt','w',newline='')
with open('C:\\22bca222\\python\\SQLITE3\\python.txt','r') as file:
    print("Python.txt file in UPPER CASE:-\n")
    for lines in file:
        f1.write(lines.upper())
f1.close()
with open('C:\\22bca222\\python\\SQLITE3\\python_upper.txt','r') as f:
    read_txt=f.read()
    print(read_txt)



