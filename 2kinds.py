from src.twokinds import dl
from src.twopdf import pdf
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(prog="python 2kinds.py",
        description='Archiving TwoKinds Comic')
    parser.add_argument("-d","--download", 
        help="Download all pages", action='store_true')
    parser.add_argument("-p","--pdf", 
        help="Combine pages into PDF(s); Single PDF or Multiple PDFs, grouped by chapter: "\
        "default is 'single' if no mode is provided", 
        choices=['single','chapters'])
    args = parser.parse_args()

    if(len(sys.argv)<2):
        parser.parse_args(['-h'])

    if(args.download):
        print("Downloading pages...")
        dl()
    elif(args.pdf):
        print("Combining into PDF... " + args.pdf)
        pdf(args.pdf)
    else:
        parser.parse_args(['-h'])

if __name__ == "__main__":
    main()