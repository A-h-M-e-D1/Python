# Creating and modifying PDF Files
# Extract Text From Pdf

from PyPDF2 import PdfReader,PdfWriter,PageObject

# open pdf

# pdf_file=open("Sheet 4.pdf",'rb')

# pdf_reader=PdfReader(pdf_file)

# عدد الصفحات

# numbers_page=len(pdf_reader.pages)

# print(f"Numbers of Pages is => {numbers_page}")

# لقراءه النصوص في الصفحات

# for page in pdf_reader.pages:
#     text=page.extract_text()
#     print(f"\n{text} ")

# pdf_file.close()

# my_pdf=PdfWriter()

# page1=PageObject.create_blank_page(None,612,792)

# my_pdf.add_page(page1)

# output_file=open("new_file.pdf",'wb')
# my_pdf.write(output_file)
# output_file.close()


# Encryption and Decryption of PDFs

# file_reader=PdfReader("new_file.pdf")
# file_writer=PdfWriter()

# # add all pages to the file_writer
# for page in file_reader.pages:
#      file_writer.add_page(page)

# #Add a password to the new PDF
# file_writer.encrypt("Ahmed0")

# # Save the new PDF to a file

# with open("new_file.pdf","wb") as f:
#      file_writer.write(f)

# genertate password
# import random
# import string

# def generate_password(length=30):
#     char=string.ascii_letters + string.digits + string.punctuation
#     password=''.join(random.choice(char) for _ in range(length))
#     return password
# print(generate_password())