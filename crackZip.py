# coding=utf-8
__author__ = 'cortexm333'

import os 
import zlib
import zipfile

""" compress tyep:
ZIP_STORED = 0
ZIP_DEFLATED = 8
ZIP_BZIP2 = 12
ZIP_LZMA = 14
"""
tplType = (0,8,12,14)

while True:
    #input path and file
    #input like  D:\XXX\AA.zip
    strFileName= input("Please input file and path:\n")

    #check directory
    if not os.path.isfile(strFileName):
        print("Please enter the correct file directory:")
        continue
    
    #check zip file 
    elif 'zip' != strFileName[-3:] :
        print("Please enter the .zip file:")
        continue

    else:
        pass
    
    # open zip file
    try:
        fp=zipfile.ZipFile(strFileName)
        break
    except  Exception as e: 
        print ("Open zip file error:",e)
        continue

#get dictionary file
strDicFile = os.path.abspath('.') + '\\passwd.txt'
if not os.path.isfile(strDicFile):
    print ("Dictionary file do not exist.")
    print ("Dictionary file must be named as passwd.txt,and in the same directory with python file.")
    exit()

zipinfo = fp.infolist()
iType = zipinfo[0].compress_type

if iType not in tplType:
    print ("Do not support this zip format,This file maybe compressed by special tools, like 7zip.")
    exit()


with open(strDicFile,'r') as file:

    while True:
        
        strPasword = file.readline()
        
        if not strPasword:
            break
        
        strPasword=strPasword.strip('\n')
        
        try:
            fp.extractall(strFileName[:-4],pwd=strPasword.encode())
            print ("Crack finished.The Password is %s" % strPasword)
            exit()
        except  Exception as e:
            pass
    print ('Password did not found!')