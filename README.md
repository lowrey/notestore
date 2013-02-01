notestore
=========

Notestore is a command line interface to the notepad.cc service. Input can be taken but stdin, argument, or a file.  If a file is given, it is stored on notepad.cc as base64 encoded data.  Output is by default written to stdout but can be written to a file.  Content is base64 decoded if written to a file.

## Examples
* ./notestore.py -i "A piece of paper in the cloud."
* ./notestore.py -g -d NotestoreTest
* ./notestore.py -d NotestoreTest -f rykr.jpeg
