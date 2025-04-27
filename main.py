from input import select_file_via_explorer
from pdf_to_docx import convert_pdf_to_docx
from jpg_to_pdf import jpg_to_pdf
from image_background_remover import remove_background

def main():

    choice = int(input('Which service do you want to use \n 1--> PDF to WORD\n 2-->JPG to PDF\n 3--> Background Remover\nEnter the number according to corresponding service of your choice :'))
    if choice == 1:
        # pdf to word
        pdf_file = select_file_via_explorer('PDF files (*.pdf)|*.pdf')
        if pdf_file:
            print("Selected file:", pdf_file)
            convert_pdf_to_docx(pdf_file)
        else:
            print('select a pdf file !!!')
    elif choice == 2:
        #jpg to pdf
        jpg_file = select_file_via_explorer('JPG files (*.jpg)|*.jpg')
        if jpg_file:
            print(jpg_file)
            jpg_to_pdf(jpg_file)
        else:
            print('Select a valid jpg file')
    elif choice == 3:
        #background remover
        image_file = select_file_via_explorer('Images files (*.jpg;*.jpeg;*.png)|*.jpg;*.jpeg;*.png')
        if image_file:
            remove_background(image_file)
        else:
            print('select valid image file')
    else:
        print('Invalid input , choice out of bound')

main()