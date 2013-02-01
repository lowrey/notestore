from pyquery import PyQuery as pq
from base64 import decode
import requests, StringIO
from helpers import print_v, NOTEPAD_CC_URL

def get_file(pad_name, outfile):
    f = open(outfile, 'w+b')
    to_decode = StringIO.StringIO()
    to_decode.write(get_content(pad_name))
    to_decode.seek(0)
    decode(to_decode, f)
    f.close()

def get_content(pad_name):
    url = NOTEPAD_CC_URL + pad_name
    r = requests.get(url)
    d = pq(r.text)
    contents = d('#contents')
    print_v("Get successful")
    return contents.text()

def get_op(dest, opts):
    if opts.file:
        get_file(dest, opts.file)
    else:
        print(get_content(dest))
