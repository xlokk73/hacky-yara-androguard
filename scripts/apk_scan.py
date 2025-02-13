import os
import sys
import re

def listfiles(folder):
    for root, folders, files in os.walk(folder):
        for filename in folders + files:
            yield os.path.join(root, filename)

if not os.path.isdir(sys.argv[1]):
    print('Give me report folder argv[1]')
    sys.exit()
reports = [f for f in listfiles(sys.argv[1])]

if not os.path.isdir(sys.argv[2]):
    print('Give me rules folder argv[2]')
    sys.exit()

rule_count = 0
for filename in listfiles('./' + sys.argv[2]):
    match = re.search("\.yar$", filename)

    # if match is found
    if match:
        rule_count+=1
        fileextensions = ('.apk', '.dex', '.elf', 'AndroidManifest.xml', '.tar')
        for report in listfiles('./' + sys.argv[1]):
            if report.endswith(fileextensions):
                os.system('yara --no-warnings '+ filename + ' ' + report)


print("Num of rules scanned: " + str(rule_count))
