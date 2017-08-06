#!/usr/bin/env python
#-*- coding: utf-8 -*-

# One-Line IF-Else
# 'Code' if comparation else 'Code'

# To-Do
# Multiple subtitle convert

# echo $a | sed -e "s/ð/ğ/g"

'''
ð - ğ
þ - ş
ý - ı
Ý - İ
Þ - Ş
Ð - Ğ
ž
'''

import sys, io

req_version = (3,6)
cur_version = sys.version_info

def readFile(_file):
  encodings = ['utf-8', 'utf-16', 'windows-1254', 'windows-1252', 'latin-1', 'iso-8859-1']
  for encode in encodings:
    try:
      reader = io.open(_file, 'r', encoding=encode)
      text = reader.read()
      #a = io.open(_file, 'r', encoding=encode)
      #b = a.read()
      #b = b.replace('\x00', '').decode('utf-8', 'replace').encode('utf-8')
      reader.close()
      print(encode, " on for-try")
      return text
    except UnicodeDecodeError:
      print("UnicodeDecodeError")

def fixIt(_text): # Change Char Method
  characters = [
    ['ð', 'ğ'],
    ['þ', 'ş'],
    ['ý', 'ı'],
    ['Ý', 'İ'],
    ['Þ', 'Ş'],
    ['Ð', 'Ğ']
    #['', ''],
    #['', ''],
    #['# ', ''],
    #[' #', ''],
    #['ž', '']
  ]
  for char in characters:
    #char1 = char[0].decode('utf-8')
    #char2 = char[1].decode('utf-8')
    text = _text.replace(char[0], char[1])
  return text

def openFile(_file):
  text = readFile(_file)
  correct(text, _file)

def correct(_text, _file):
  text = fixIt(_text)
  save(text, _file)

def save(_text, _file):
  writeToFile = io.open(_file, 'w', encoding='utf-8')
  writeToFile.write(_text)
  writeToFile.close()

def arguments(_arg):
  usage = '''usage: charsFixer.py -f <subtitle-file>
    \r  -f : File, subtitle file for fix.
    \r  -h or --help : Show this help messages.'''
  if len(_arg) > 1:
    if _arg[1] == '-f':
      _arg.remove(_arg[0])
      _arg.remove(_arg[0])
      for x in _arg:
        openFile(x)
   #  print(x)
    elif _arg[1] == '--help' or _arg[1] == '-h':
      print(usage)
    else:
      print('Invalid argument. ' + _arg[1])
  else:
    print(usage)

if cur_version >= req_version:
   arguments(sys.argv)
else:
   print("Your Python interpreter is too old. Please consider upgrading.")
