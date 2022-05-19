from PyPDF2 import PdfFileReader

reader = PdfFileReader("sample.pdf")   # Choose PDF file
page1 = reader.pages[0]
text = page1.extractText()
print(text)

'''
    Можно было найти пдф получше конечно, но главное результат вывел. Если были бы данные по типу баланс имя. Можно было
    бы вычитать с помощью условий.
'''
