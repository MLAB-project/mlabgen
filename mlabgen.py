from bs4 import BeautifulSoup
from string import Template
from os import walk
from os.path import join
import io
import re

wordlist = ["MLAB", "LABoratory", "argv", "argc", "printf", "sqrt", "mA", "svg", "Descr", "bom", "sw", "ama",
            "Pcb", "pcb", "heatsink", "heatsinks", "microcontroler", "microcontroler's", "Tindie", "HumanName",
            "Mlab", "www", "nTwo", "cz", "mlab", "utf"]

PRJINFORE = re.compile('\[(?P<Key>[a-z,A-Z,0-9,\-\_\.]+)\]'
                       + '\s*(?P<Value>.*?)\s*'
                       + '(?=\[(?:[a-z,A-Z,0-9,\-\_\.]+)\])', flags=re.S|re.U)

def sch2descr(sch):
    return sch[sch.find("Descr"):sch.find("EndDescr")].split("\n")[1:-1]

def descr2dict(descr_lines):
    outdict = {}

    for line in descr_lines:
        val = ""
        for item in line.split(" ")[1:]:
            if item == line.split(" ")[1:][-1]:
                val += item
            else:
                val += item + " "
        outdict[line.split(" ")[0]] = val

    return outdict

def dict_str_replace(replace, replacement, dictionary):
    for key in list(dictionary.keys()):
        dictionary[key] = dictionary[key].replace(replace, replacement)

    return dictionary

def dict_str_rm(rm, dictionary):
    return dict_str_replace(rm, "", dictionary)

def dict2prjinfo(dictionary):
    outstr = ""

    for key in list(dictionary.keys()):
        outstr += "[" + key + "]\n"
        outstr += dictionary[key] + "\n"
    
    outstr += "[End]"
    return outstr

def prjinfo2dict(path):
    content = io.open(path, encoding='utf-8-sig').read()
    content = '\n'.join([x for x in content.split('\n') if not x.strip().startswith('//')]).strip()
    return dict(re.findall(PRJINFORE, content))

def lspath(directory="./"):
    for root, dirs, files in walk(directory):
        for item in dirs + files:
            yield(join(root, item))
