from PyPDF2 import PdfMerger

pdfs = ["Group-D Assignment.pdf", "Assignment(Roll-011).pdf"]

mymerger = PdfMerger(pdfs)

for newpdf in pdfs:
    mymerger.append(newpdf)

mymerger.write("assignmentsss.pdf")

mymerger.close()