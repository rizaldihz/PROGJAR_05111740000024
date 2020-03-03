import logging
import requests
import os
import threading
import datetime

def worker(url=None):
    download_gambar(url)
    print("Downloaded {}\n" . format(url))
    return

def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        namafile1 = namafile.split('?')
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(namafile1[0]+'.'+ekstensi,"wb+")
        fp.write(ff.content)
        fp.close()
    else:
        return False




if __name__=='__main__':
    imgs = [
        'https://images.unsplash.com/photo-1583142499515-db3e66a57bdc?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
        'https://images.unsplash.com/photo-1520699894975-334692f3a636?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60',
        'https://images.unsplash.com/photo-1453904061941-02ada96e1f4a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60',
    ]
    threads = []
    for im in imgs:
        t = threading.Thread(target=download_gambar,args=(im,))
        threads.append(t)
        t.start()

