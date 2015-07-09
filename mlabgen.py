import io
import re

def descr2dict(descr):
    outdict = {}

    for line in descr:
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

    return outstr

PRJINFORE = re.compile('\[(?P<Key>[a-z,A-Z,0-9,\-\_\.]+)\]'
                       + '\s*(?P<Value>.*?)\s*'
                       + '(?=\[(?:[a-z,A-Z,0-9,\-\_\.]+)\])', flags=re.S|re.U)

def prjinfo2dict(path):
    content = io.open(path, encoding='utf-8-sig').read()
    content = '\n'.join([x for x in content.split('\n') if not x.strip().startswith('//')]).strip()
    return dict(re.findall(PRJINFORE, content))
