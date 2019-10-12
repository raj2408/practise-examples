

def docprint():
    import docx
    doc = docx.Document('./testdoc.docx')
    for para in doc.paragraphs:
        return(para.text)

