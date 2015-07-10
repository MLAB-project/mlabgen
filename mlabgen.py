from bs4 import BeautifulSoup
from string import Template

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

def sch2descr(sch):
    return sch[sch.find("Descr"):sch.find("EndDescr")].split("\n")[1:-1]

def dict2prjinfo(dictionary):
    outstr = ""
    
    for key in list(dictionary.keys()):
        outstr += "[" + key + "]\n"
        outstr += dictionary[key] + "\n"
    
    outstr += "[End]"
    return outstr

def count_char_row(char, string):
    for i in range(len(string)):
        if string[i] == char:
            for j in range(len(string[i:])):
                if string[i:][j] != char:
                    return j
    return 0

def html_prettify(html, indent_level=4):
    outstr = ""
    for line in BeautifulSoup(html).prettify().split("\n"):
            outstr += " " * (indent_level - 1) * count_char_row(" ", line) + line + "\n"
    return outstr
