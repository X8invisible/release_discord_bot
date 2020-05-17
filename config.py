from configparser import ConfigParser

parser = ConfigParser()
parser.read('config.ini')

def getToken():
    return parser.get('discord', 'token')

def getGuild():
    return parser.get('discord', 'guild')
def getMusik():
    return parser.get('discord', 'musik')