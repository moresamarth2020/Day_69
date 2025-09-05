#!/usr/bin/env python
# coding: utf-8

# # Exercise 8 - Merge the Pdf Solution in Python 
# - Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.

# In[5]:


pip install PyPDF2


# In[10]:


from PyPDF2 import PdfWriter
import os

merge = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]


for pdf in files:
    merge.append(pdf)
    
merge.write("merged-pdf.pdf")
merge.close()


# Print only file location
print(os.path.abspath(output_file))


# In[ ]:




