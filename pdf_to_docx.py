from pdf2docx import Converter

def convert_pdf_to_docx(pdf_path):
    if not pdf_path.lower().endswith(".pdf"):
        print("Please select a valid PDF file.")
        return

    docx_path = pdf_path.replace(".pdf", ".docx")

    print(f"Converting '{pdf_path}' to '{docx_path}'...")
    cv = Converter(pdf_path)
    cv.convert(docx_path)
    cv.close()

    print("Conversion completed!")