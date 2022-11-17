# Chapter 10: Files and Exeptions

# with open('filepath') as aliasNameForTheFile:
#     line1 = aliasNameForTheFile.readline()
#     # will open memory location
#     # line1 - assigning variable
#
#     line2 = aliasNameForTheFile.readline()
#     line3 = aliasNameForTheFile.readline()
#
#     all_lines = aliasNameForTheFile.readlines() #- list of values
#
#     file_content = aliasNameForTheFile.read() #- whole content

####### aliasNameForTheFile.close()

# need to close location, otherwise happens memory leak
# no need to close when you read a file starting with "with"


filepath = '../data/products.txt'

print('***************** READ file ************')
with open('../data/products.txt') as prod_list:
    contents = prod_list.read()
    print('Contents of the file: \n', contents)

with open(filepath, 'r') as prod_list:
    print('now we are trying to loop through the contents')
    all_lines = prod_list.readlines()
    print(all_lines)
    print('printing the line5:', all_lines[4])

for line in all_lines:
    print(line)

print('***************** WRITE file appending new content ************')
with open(filepath, 'a') as prod_list:
    prod_list.write('playstation')  # no variable needed
    # check the file content - a  - appends content
    prod_list.write('Learning Python book\n') # -if dont put \n will return everyrhing in one line
    prod_list.write('First head to Selenium Book\n')

    print('***************** WRITE file deleting old content ************')
#
# with open(filepath, 'w') as prod_list:
#     prod_list.write('spiderman jacket')  # no variable needed
#     # check the file content - w deletes all content leaving just spiderman jacket
#     prod_list.write('batman mask\n') # -if don't put \n will return everyrhing in one line
#     prod_list.write('smart tv samsung 70\n')
