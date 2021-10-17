import os
from pdf2image import convert_from_path


def read_files():
    basePath = 'pdf-files'  # pdf file folder
    pdfFiles = os.listdir(basePath)  # [] with every pdf file in files/
    for file in pdfFiles:
        images = convert_from_path(f"pdf-files\\{file}",        #put your pdfs in the 'file folder'
                                   500,                     #dpi
                                   jpegopt={
                                       "quality": 100,
                                       "progressive": True,
                                       "optimize": True
                                   },
                                   single_file=True,
                                   output_file=file[:-4],    #name of the pdf, -4 removes the '.pdf' in name
                                   fmt='jpeg',               #jpeg, png, ppm, tiff
                                   output_folder=r'C:\Users\AL\PycharmProjects\Pdf 2 Jpeg\IMAGES',
                                   poppler_path=r'C:\Program Files\poppler-21.10.0\Library\bin')    #just put poppler in program files
        print(f"### End of file {file}")
    print("### Done")

if __name__ == '__main__':
    read_files()
