###Read the File
#Method 1 - You will have to open as well as close the file
# file = open('myfile.txt')
# content = file.read()
# print(content)
# file.close()

#Method 2 - you donr have to close the file
#
# with open('myfile.txt') as file:
#     content= file.read()
#     print(content)

### Write the File
## mode a= append, w - write
with open('myfile.txt', mode ='w') as file:
    file.write("Hello world")
