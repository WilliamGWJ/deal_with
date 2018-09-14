import urllib.request
import sys
import re


typ = sys.getfilesystemencoding()


def translate(querystr, to_l="zh", from_l="en"):
    '''for google tranlate by doom
    '''
    C_agent = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.165063 Safari/537.36 AppEngine-Google."}
    flag = 'class="t0">'
    tarurl = "http://translate.google.com/m?hl=%s&sl=%s&q=%s \
        " % (to_l, from_l, querystr.replace(" ", "+"))
    request = urllib.request.Request(tarurl, headers=C_agent)
    page = str(urllib.request.urlopen(request).read().decode(typ))
    target = page[page.find(flag) + len(flag):]
    target = target.split("<")[0]
    return target


with open('test.txt') as file_ens:
    file_en = file_ens.read()


a = re.subn('\n', '', file_en)
a = translate(file_en)
c = re.subn(',', '\n', a)
print(a)
print(b)
print(c)

# print(translate(""))
