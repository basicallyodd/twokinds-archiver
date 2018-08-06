#!/usr/bin/env python

import requests, os, shutil
from clint.textui import progress

baseurl = 'http://twokinds.keenspot.com/comic/'  # n/ for page number

def find_comic_img(page):
    s = page.find('<article class="comic">')
    s = page.find('src="', s) + len('src="')
    e = page.find('"',s)
    return page[s:e]

def get_page(url):
    return requests.get(url).text

def find_number_of_pages_published():
    page = get_page('http://twokinds.keenspot.com/archive/')
    latest_page_ptr = page.find('<span>1</span>')
    latest_page_ptr_end = page.find('<',latest_page_ptr+1)
    latest_page_num = page[latest_page_ptr+len('<span>'):latest_page_ptr_end]
    latest_page_num_maybe = latest_page_num
    while True:
        # print('[!] Debug: Discovered ' + str(latest_page_num) + ' pages.')
        latest_page_ptr = page.find('<span>',latest_page_ptr_end)
        latest_page_ptr_end = page.find('<',latest_page_ptr+1)
        latest_page_num_maybe = page[latest_page_ptr+len('<span>'):latest_page_ptr_end]
        if(latest_page_num_maybe.isdigit()):
            latest_page_num = latest_page_num_maybe
        else:
            break
    return latest_page_num

def init_save_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir

def save_image(urltoimage,path,name):
    if not os.path.isfile(path+name):
        r = requests.get(urltoimage, stream=True)
        if r.status_code == 200:
            with open(path+name, 'wb') as f:
                total_length = int(r.headers.get('content-length'))
                for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                    if chunk:
                        f.write(chunk)
                        f.flush()
    else:
        print(name + " exists! Skipping...")

def exists(path,name):
    if not os.path.isfile(path+name):
        return False
    else:
        print(name + " exists! Skipping...")
        return True

def find_date_in_url(url):
    s = url.find("comics/") + len("comics/")
    e = url.find(".",s)
    return url[s:e]

def find_start_page(path):
    dir = os.listdir(path)
    lastpage = 1
    for item in dir:
        endchr = str(item).find("_")
        lastpage = item[:endchr]
    return int(lastpage)

def main():
    print(".: TwoKinds Backup/Archive Creator :.")

    pagecount = find_number_of_pages_published()

    print("About to download " + str(pagecount) + " pages...")

    path = init_save_dir("twokinds/")

    start = find_start_page(path)

    if start != 1:
        print("Previous backup detected, resuming from last downloaded page...")

    for i in range (start,int(pagecount)):
        f = get_page(baseurl+str(i))
        print("Saving page " + str(i) + " / " + str(pagecount) + " ...")
        url = find_comic_img(f)
        save_image(url,path,str(i).zfill(4)+"_" + 
            str(find_date_in_url(url)) + "_.jpg")
   

if(__name__=="__main__"):
    main()