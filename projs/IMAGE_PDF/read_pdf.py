import PyPDF2
 
pdfFileObj = open('sample.pdf', 'rb')# creating a pdf file object
 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)# creating a pdf reader object
 
print(pdfReader.numPages)# printing number of pages in pdf file
 
pageObj = pdfReader.getPage(0)# creating a page object
 
print(pageObj.extractText())# extracting text from page
 
pdfFileObj.close()# closing the pdf file object

pdfFileObj1 = open('file.pdf', 'rb')
 
pdfReader1 = PyPDF2.PdfFileReader(pdfFileObj1)
 
print(pdfReader1.numPages)
 
pageObj1 = pdfReader1.getPage(0)

print(pageObj1.extractText())
 
pdfFileObj.close()