"""此脚本用于合并中英文字幕
"""


import os
import sys
import urllib.request


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


for dir, _, filenames in os.walk('srt_en'):
    f_n = 0
    for filename in filenames:
        # 将srt_en转换为Unicode编码
        srt_en_file = os.path.join('srt_en', filename)
        with open(srt_en_file, 'r', encoding="utf-8") as file_ens:
            file_en = file_ens.readlines()

        srt_file = os.path.join('srt_done', filename)
        n = len(file_en)
        with open(srt_file, 'w+', encoding="utf-8") as file_end:
            for i in range(n):
                file_end.write(file_en[i])
                if i % 4 == 2:
                    file_end.write(translate(file_en[i]))
                    print('Done line({})'.format(i//4))
        print('Done file {}'.format(f_n))
        f_n += 1


# with open("./How to accelerate your neural net inference with TensorRT_en.srt",
#           encoding='utf-8') as file_1:
#     file_en = file_1.readlines()

# with open("./How to accelerate your neural net inference with TensorRT_cn.srt",
#           encoding='utf-8') as file_2:
#     file_cn = file_2.readlines()

# n = len(file_en)
# with open('How to accelerate your neural net inference with TensorRT.srt', "w",
#           encoding='utf-8') as file_3:
#     for i in range(n):
#         file_3.write(file_en[i])
#         if i % 4 == 2:
#             file_3.write(file_cn[i])
