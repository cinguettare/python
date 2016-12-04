#!/usr/bin/python3

import easygui as g
import urllib.request

def main():
    msg = "Please fill in the size of the meow"
    title = "Cats Download"
    fieldNames = ['width:','height:']
    fielValues = []
    size = width, height = 400, 600
    fielValues = g.multenterbox(msg, title, fieldNames, size)               # Gets the size of the image to be downloaded

    while 1:                                        # The loop is used to determine whether the entered value meets the requirements
        if fielValues == None:
            break
        errmsg = ""

        try:
            width = int(fielValues[0].strip())
        except:
            errmsg += "The width must be an integer!"

        try:
            height = int(fielValues[1].strip())
        except:
            errmsg += "Height must be an integer!"

        if errmsg == "":
            break

        fielValues = g.multenterbox(errmsg, title, fieldNames, fielValues)   # The required dimensional values

    url = "http://placekitten.com/g/%d/%d" % (width, height)                 # Meow picture site

    response = urllib.request.urlopen(url)
    cat_img = response.read()

    filepath = g.diropenbox("Please select the folder where the pictures are stored")

    if filepath:                                     # Determine whether to set the folder to store, do not set the default local
    filename = '%s/cat_%d_%d.jpg' % (filepath, width, height)            
    else:
        filename = 'cat_%d_%d.jpg' % (width, height)                         

    with open(filename, 'wb') as f:                                          
        f.write(cat_img)

if __name__ == "__main__":
    main()
