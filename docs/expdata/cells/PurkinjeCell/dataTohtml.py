# ~/docs/expdata/cells/PurkinjeCell/dataTOhtml.py
##############################################################################
#                        HOW TO USE THIS SCRIPT
# python dataTohtml.py "desired_data.json" "Some dummy title"
##############################################################################
#from pdb import set_trace as breakpoint
import os
from sys import argv
import json
from json2html import json2html
from bs4 import BeautifulSoup as bs

thispythonfile, filename, title_content = argv

pwd = os.getcwd() # ~/cerebunitdata/docs/expdata/cells/PurkinjeCell

######################### LOAD DATA, i.e., JSON FILE ##########################
os.chdir("../../../..") # this moves you to ~/cerebunitdata
filepath = os.getcwd()+ os.sep + "expdata" + os.sep + "cells" + os.sep + \
           "PurkinjeCell" + os.sep + filename #"Llinas_Sugimori_1980_soma_restVm.json"
rawdata = open(filepath, "r", encoding="utf-8")
jsondata = json.load(rawdata) # <- THIS WILL BE PASSED DOWN
rawdata.close()
os.chdir(pwd) # return to ~/cerebunitdata/docs/expdata/cells/PurkinjeCell

######################### CREATE THE HTML CONTAINER  ##########################
structure = """
            <html>
            <head><title>Llinas and Sugimori 1980 Data for Resting Membrane Voltage</title>
            <body></body>
            </html>
            """
soup = bs(structure, features="lxml")
title = soup.find("title")
body = soup.find("body")

###################### INSERT TITLE INTO HTML CONTAINER #######################
title.insert(0, title_content)

######################### CONVERT JSON DATA TO HTML  ##########################
htmltable = json2html.convert(json = jsondata)
extrasoup = bs(htmltable, "html.parser")

###################### INSERT TABLE INTO HTML CONTAINER #######################
body.insert(0, extrasoup)

####################### FINALLY WRITE INTO HTML FILE  #########################
savefile = pwd + os.sep + "rawhtmls" + os.sep + filename.replace(".json",".html")
html = open( savefile, "w", encoding="utf-8" )
html.write( str(soup) )

