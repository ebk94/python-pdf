import pytest
import pdfquery

@pytest.fixture
def get_word_dictionary():
    def _get_word_dictionary(pdf_file_name):
        pdf = pdfquery.PDFQuery(pdf_file_name)
        pdf.load()

        word_dict = {}

        text_elements = pdf.pq('LTTextBoxHorizontal')

        # Convert the pdf to XML intentionally commented out, can be useful for testing manually
        # pdf.tree.write('test_task.xml', pretty_print = True)

        # It returns a list of words
        text = [t.text.strip() for t in text_elements]

        # Adding words to word dictionary
        for i in range(0, len(text)):
            word_dict[i] = text[i].strip()

        # Loops through the word_dict to add individual word coordinates 
        for i in range(0, len(word_dict)):
            word = word_dict[i]
            word_coordinates = pdf.pq(f'LTTextLineHorizontal:contains("{word}")').attr('bbox')
            if word_coordinates:
                word_dict[word_coordinates] = word_dict[i]
                del word_dict[i]
            else:
                print('Something went wrong')

        return word_dict
    # In output we will get a dictionary with coordinates and
    return _get_word_dictionary
    