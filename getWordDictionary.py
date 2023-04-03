import pdfquery
def getWordDictionary(pdfFileName):
    pdf = pdfquery.PDFQuery(pdfFileName)
    pdf.load()

    word_dict = {}

    text_elements = pdf.pq('LTTextBoxHorizontal')

    text = [t.text.strip() for t in text_elements]

    for i in range(0, len(text)):
        word_dict[i] = text[i]
    
    for i in range(0, len(word_dict)):
        word = word_dict[i]
        word_coordinates = pdf.pq(f'LTTextLineHorizontal:contains("{word}")').attr('bbox')
        if word_coordinates:
            word_dict[word_coordinates] = word_dict[i]
            del word_dict[i]
        else:
            print('Something went wrong')
    return word_dict

if __name__ == '__main__':
    ethalonFile = input("Введите свой эталонный файл: ")
    print(getWordDictionary(f'{ethalonFile}.pdf'))
    dict1=getWordDictionary(f'{ethalonFile}.pdf')
    fileName = input("Введите название файла: ")
    print(getWordDictionary(f'{fileName}.pdf'))
    dict2=getWordDictionary(f'{fileName}.pdf')
    print(dict1==dict2)
