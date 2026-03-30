import PyPDF2

pdf_path = r'c:\Users\Venti\Desktop\bishe\论文\核心内容\《AI智能运动动作矫正系统的设计与实现》.pdf'

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ''
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        page_text = page.extract_text()
        if page_text:
            text += page_text + '\n\n'

print(text)