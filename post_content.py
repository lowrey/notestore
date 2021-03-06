from base64 import encode
import urllib, requests, StringIO, sys
from helpers import print_v, write_v, NOTEPAD_CC_URL

def b64encode_tos(infile):
    f = open(infile, 'rb')
    outfile = StringIO.StringIO()
    encode(f, outfile)
    f.close()
    return outfile.getvalue()

def post_file(pad_name, infile):
    instr = b64encode_tos(infile)
    post_content(pad_name, instr)

def post_content(pad_name, content):
    ajax_url = 'ajax/update_contents/' + pad_name
    parameters = {
            'contents': content,
            'caret_position': len(content),
            'scroll_position': 0
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = urllib.urlencode(parameters)
    url = NOTEPAD_CC_URL + ajax_url
    print_v("Sending data to {}".format(url))
    write_v('...')
    r = requests.post(url, data=payload, headers=headers)
    r.raise_for_status()
    print_v("Request successful")

def post_op(dest, opts):
    if opts.file:
        post_file(dest, opts.file)
    else:
        data = ""
        if not opts.input:
            data = sys.stdin.read()
        else:
            data = opts.input
        post_content(dest, data)
