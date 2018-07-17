from string import Template
from os import walk
from os.path import join
import os
import json
import csv
import io
import re
import qrcode

wordlist = ["MLAB", "LABoratory", "argv", "argc", "printf", "sqrt", "mA", "svg", "Descr", "bom", "sw", "ama",
            "Pcb", "pcb", "heatsink", "heatsinks", "microcontroler", "microcontroler's", "Tindie", "HumanName",
            "Mlab", "www", "nTwo", "cz", "mlab", "utf"]

index_dirs_line  = "<li><table><tr>\n"
index_dirs_line += "    <td class=\"icon\"><a href=\"${Module}\"><img src=\"${Module}/DOC/IMG/${Module}_200x200.png\"></a></td>\n"
index_dirs_line += "    <td class=\"descr\"><h2><a href=\"${Module}\">$HumanName</a></h2> <p>$Descr<br><a href=\"${Module}\">More...</a></p></td>\n"
index_dirs_line += "<tr></table></li>\n"

index_line_sep = "<li><hr></li>\n"

index_modules_line  = "<li><table><tr>\n"
index_modules_line += "     <td class=\"icon\"><a href=\"${Module}/DOC/${Module}.html\"><img src=\"${Module}/DOC/IMG/${Module}_200x200.png\"></a></td>\n"
index_modules_line += "     <td class=\"descr\"><h2><a href=\"${Module}/DOC/${Module}.html\">$HumanName</a></h2> <p>$Descr<br><a href=\"${Module}/DOC/${Module}.html\">More...</a></p></td>\n"
index_modules_line += "     <td class=\"purchase\"><a href=\"$BuyLink\">Purhcase</a></td>\n"
index_modules_line += "</tr></table></li>\n"

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


def getModuleInfo(path = None):
    if not path:
        path = os.path.realpath('.')
    #print("Nastavena cesta je", path)
    module = os.path.basename(os.path.normpath(path))
    data = json.load(open(os.path.join(path, module+'.json')))
    return data

def QRpermalink(module, path=None):
    if not path:
        path = 'doc/img/%s_QRcode.png'%module
    try:
        qr = qrcode.QRCode( version=4, error_correction=qrcode.constants.ERROR_CORRECT_Q, box_size=15, border=4)
        qr.add_data('https://www.mlab.cz/PermaLink/'+module)
        qr.make(fit=True)
        qr.make_image().save(path)
    except Exception as e: raise(e)


def BOM_ust(scheme, out = None):
    sch = open(scheme, 'r').read()
    sch_parts = sch.split("$")
    ust_bom = []
    
    '''
    Comp
    L power:VCC #PWR0101
    U 1 1 5A9A7508
    P 6300 2900
    F 0 "#PWR0101" H 6300 2750 50  0001 C CNN       # Reference
    F 1 "VCC" H 6317 3073 50  0000 C CNN            # Hodnota (Value)
    F 2 "" H 6300 2900 50  0001 C CNN               # Pouzdro
    F 3 "" H 6300 2900 50  0001 C CNN               # dokumentace
        1    6300 2900
        1    0    0    -1  
    '''

    for area in sch_parts:    
        lines = area.split('\n')
        component = list(csv.reader(lines, delimiter=' ', quotechar='"'))

        if component[0][0] == 'Comp':
            param = {}
            for comp in component:
                try:
                    if comp[0] == 'L':
                        param['Name'] = comp[1]
                        param['Ref'] = comp[2]

                    elif comp[0] == 'U':
                        param['Tstamp'] = comp[3]

                    elif comp[0] == 'F':
                        fn = int(comp[1])
                        if fn == 0:
                            pass
                        elif fn == 1:
                            param['Value'] = comp[2]    
                        elif fn == 2:
                            param['Package'] = comp[2]
                        elif fn == 3:
                            param['Datasheet'] = comp[2]
                        elif fn == 4:
                            param[comp[11]] = comp[2]

                except Exception as e:
                    pass
            if not '#' in param['Ref']:
                ust_bom += [param]
    if out:
        with open(out, 'w') as f:
            json.dump(ust_bom, f, sort_keys = True, indent = 4)
    
    return(ust_bom)