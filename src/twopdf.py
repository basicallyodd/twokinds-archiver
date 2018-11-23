from PIL import Image
import argparse
from src.twokinds import find_number_of_pages_published, find_start_page
import os

def singlepdf():
    print("Combining pages...")
    pages = []
    for page in os.listdir(os.getcwd()+"\\twokinds"):
        if page.endswith(".jpg"):
            p = Image.open(os.getcwd()+"\\twokinds\\"+page)
            if p.mode == 'RGBA':
                p = p.convert('RGB')
            pages.append(p)
    
    output_filename = os.getcwd()+"\\twokinds-pdfs\\TwoKinds.pdf"

    #logo = Image.open(os.getcwd()+"\\src\\Twokindslogo.png").convert("RGB")

    pages[0].save(output_filename, "PDF", resolution=100.0, save_all=True, append_images=pages[1:])

    print("Done!")

def chapterspdf():
    print("NOT YET IMPLEMENTED: https://github.com/basicallyodd/twokinds-archiver/issues/4")
    pass

def pdf(mode):

    pub = find_number_of_pages_published()
    have = find_start_page('twokinds/')

    try:
        if(int(pub)==(have)):
            print("all pages downloaded! continuing to merge")
            pass
        else:
            print("not all pages downloaded! Please run twokinds.py to get the latest pages")
            print("Found online: " + str(pub))
            print("Found in folder twokinds/: " + str(have))
    except FileNotFoundError as e:
        print("Please run the regular twokinds downloader (twokinds.py) first!")
        exit()

    if(mode=='single'):
        print("SINGLE PDF MODE")
        singlepdf()
    else: #(mode=='chapters')
        print("CHAPTERS MODE")
        chapterspdf()   

def main():
    parser = argparse.ArgumentParser(prog="python 2pdf.py",
        description='Create TwoKinds PDFs')
    parser.add_argument("-m","--mode", 
        help="Single PDF or Multiple PDFs, grouped by chapter: "\
        "default is 'single' if no mode is provided", 
        choices=['single','chapters'],required=True)
    args = parser.parse_args()

    print(".: TwoKinds Backup/Archive Creator :.")
    print("PDF Creater Mode          ")

    pub = find_number_of_pages_published()
    have = find_start_page('twokinds/')

    try:
        if(int(pub)==(have)):
            print("all pages downloaded! continuing to merge")
            pass
        else:
            print("not all pages downloaded! Please run twokinds.py to get the latest pages")
            print("Found online: " + str(pub))
            print("Found in folder twokinds/: " + str(have))
    except FileNotFoundError as e:
        print("Please run the regular twokinds downloader (twokinds.py) first!")
        exit()

    if(args.mode=='single'):
        print("SINGLE PDF MODE")
        singlepdf()
    else: #(args.mode=='chapters')
        print("CHAPTERS MODE")
        chapterspdf()   

#if __name__ == "__main__":
#    main()