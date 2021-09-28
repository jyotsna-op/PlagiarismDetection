import PyPDF2
import difflib
file1 = open('file.pdf', 'rb')
file2 = open('sample.pdf', 'rb')

# create a pdf reader object
pdfReader1 = PyPDF2.PdfFileReader(file1)
pdfReader2 = PyPDF2.PdfFileReader(file2)

# get the number of pages in pdf file
pages1 = pdfReader1.numPages
pages2 = pdfReader2.numPages

for i in range(pages1):
    
    #extract the page
    page1 = pdfReader1.getPage(i)
    
    #print the page text content along with page number
    # print("Page no:",i)
    # print(page1.extractText())

for j in range(pages2):
    
    #extract the page
    page2 = pdfReader2.getPage(j)
    
    #print the page text content along with page number
    # print("Page no:",j)
    # print(page2.extractText())

data1 = page1.extractText()
data2 = page2.extractText()
# print(data1)
# print(data2)

res1 = data1.split()
res2 = data2.split()
print(res1)
print(res2)
if(res1 == res2):
    print('Same PDF')
else:
    print('Different PDF')
        
#Remove Duplicates
final = []











# list1 = res1
# list2 = res2
# list3 = []
# for l1 in list1:
#     for l2 in list2:
#         if l2 == l1:
#             list3.append(l2)
# print(list3) 