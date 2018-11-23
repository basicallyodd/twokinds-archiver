# TwoKinds Archive Backup Creator


A Python script to download all pages of TwoKinds to date. 

## Motivation
I wanted to read Tom Fischbach's comic TwoKinds while offline.  


## Prerequisites

Python dependencies: 

```bash
pip install -r requirements.txt
```


## Running the script
```bash
python .\2kinds.py -h
usage: python 2kinds.py [-h] [-d] [-p {single,chapters}]

Archiving TwoKinds Comic

optional arguments:
  -h, --help            show this help message and exit
  -d, --download        Download all pages
  -p {single,chapters}, --pdf {single,chapters}
                        Combine pages into PDF(s); Single PDF or Multiple
                        PDFs, grouped by chapter: default is 'single' if no
                        mode is provided
```


## Next Steps
Now tracked in [Project Board](https://github.com/basicallyodd/twokinds-archiver/projects/1)
Have a feature request or bug? [Submit an Issue](https://github.com/basicallyodd/twokinds-archiver/issues/new/choose).