import re
from unidecode import unidecode

#_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},]+')
#_punct_re = re.compile(r'\W+')


def slugify(text, delim=u'-'):
    """Generates an ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        result.extend(unidecode(word).split())
    return unicode(delim.join(result))

def splitter(text, delim=' '):
    """Split string into list, usage {{ string|split }}"""
    return text.split(delim)

def get_first_part(text, delim='-'):
    """Get first part from list of string with - delimiter"""
    return text.split(delim)[0]

def get_last_part(text, delim='-'):
    """Get last part from list of string with - delimiter"""
    return text.split(delim)[-1]

def onlychars(text):
    return " ".join(re.findall("[a-zA-Z0-9]+", text))
