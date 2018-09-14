"""将srt_en转换为Unicode编码，生成srt_cn文件
"""


import os


for dir, _, filenames in os.walk('srt_en'):
    for filename in filenames:
        # 将srt_en转换为Unicode编码
        srt_en_file = os.path.join('srt_en', filename)
        with open(srt_en_file, 'r', encoding="utf-8") as file_en:
            file_tr = file_en.readlines()
        with open(srt_en_file, 'w', encoding="utf-8") as file_en:
            file_en.truncate()
            for line in file_tr:
                file_en.write(line)
        # 生成srt_cn文件
        srt_cn_file = os.path.join('srt_cn', filename)
        with open(srt_cn_file, 'w+', encoding='utf-8') as file_cn:
            pass
