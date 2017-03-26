import re
import re

REPEATER = re.compile(r"(.+?)\1+$")

def repeated(s):
    match = REPEATER.match(s)
    return match.group(1) if match else None

#examples = [
 #   'abab',
#	'abababababababarrtttbabab',
#	'abababahhbabab',
#	'abcdef',
#	'aaaaaa',
#	'aabaabbaabaabbaabaabbaabaab',
#]

def getPattern(gtIn):
    if(len(gtIn)==0):
        print (0)
        return gtIn
    endHolder =0
    for j in range(endHolder+1,len(gtIn)):
        compHolder = j%(endHolder+1)
        if(gtIn[compHolder] != gtIn[j]):
            endHolder = j;
            continue
        if(j == len(gtIn)-1):
            print (endHolder+1)
            return gtIn[0:endHolder+1];
    print (endHolder+1)
    return gtIn;

for e in range(int(input())):
    x=input()
    sub = repeated(x)
    if sub:
        print(len(sub))
    else:
        getPattern(x)
