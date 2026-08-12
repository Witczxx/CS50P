"""
.jpg / .jpeg = image/jpeg
.gif = image/gif
.png = image/png
.txt = text/plain
.pdf = application/pdf
.zip = application/zip
others = application/octet-stream
"""

def get_format(s):
    if s[-5:] == ".jpeg":
        s = s[-5:]
    else:
        s = s[-4:]
    return s

file_format = get_format(input("File name: "))

match file_format:
    case ".png" | ".gif" | ".jpeg":
        print("image/" + file_format[1:])
    case ".pdf" | ".zip":
        print("application/" + file_format[1:])
    case ".jpg":
        print("image/jpeg")
    case ".txt":
        print("text/plain")
    case _:
        print("application/octet-stream")