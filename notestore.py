#!/usr/bin/python

import uuid
from optparse import OptionParser
from get_content import get_op
from post_content import post_op
from helpers import set_v


if __name__ == "__main__":
    guid = str(uuid.uuid1())
    guid = guid.replace("-","")
    parser = OptionParser()
    parser.add_option("-d", "--dest", dest="dest", default=guid, help="name of the file on notepad.cc")
    parser.add_option("-g", "--get", dest="get", action="store_true",\
        default=False, help="get destination instead of uploading")
    parser.add_option("-v", "--verbose", dest="verbose", action="store_true",\
        default=False, help="set verbose output")
    parser.add_option("-f", "--file", dest="file", default=None, help="file to upload binary data via uuencode")
    parser.add_option("-i", "--input", dest="input", default=False, \
        help="input gathered from arg instead of std input")
    (options, args) = parser.parse_args()
    dest = options.dest
    set_v(options.verbose)
    print("Using pad name {}".format(options.dest))
    if not options.get:
        post_op(dest, options)
    else:
        get_op(dest, options)
