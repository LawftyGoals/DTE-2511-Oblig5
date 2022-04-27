import os

textList = open('/home/lawftyg/Documents/DTE-2511/RPDL/listOfChapters.txt', 'r')
dirList = os.listdir('/home/lawftyg/Documents/DTE-2511/RPDL/')


for name in dirList:
    print(name.replace(".html", "") + '-')
    #for line in textList:
    #    print(name.replace(".html", ""), "-", line.strip())
    #    if name.replace(".html", "") in line.strip():
    #       print(name, "-", line)

#for sline in textList:
#    print('-' + sline.strip()+'-')

textList.close()