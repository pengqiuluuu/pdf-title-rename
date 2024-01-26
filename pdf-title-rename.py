import os
import re
from PyPDF2 import PdfReader

def get_pdf_title(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            metadata = pdf_reader.metadata
            title = metadata.get('/Title', None)
            return title
    except Exception as e:
        print(f"Error reading title for {pdf_path}: {e}")
        return None


def rename_pdfs_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory_path, filename)
            title = get_pdf_title(pdf_path)

            if title:
                # Replace invalid characters in the title with underscores
                # title = re.sub(r'[\/:*?"<>|]', '_', title)

                new_filename = f"{title}.pdf"
                new_filepath = os.path.join(directory_path, new_filename)

                try:
                    os.rename(pdf_path, new_filepath)
                    print(f"Renamed: {filename} -> {new_filename}")
                except Exception as e:
                    print(f"Error renaming {filename}: {e}")


if __name__ == "__main__":
    # directory_path = input("Enter the path to the directory containing PDF files: ")
    rename_pdfs_in_directory('.\paper')
