import jieba

with open(r'E:/OCR/symbol.txt', "r", encoding='utf8') as f:
    content = f.readlines()

with open(r'E:/OCR/medicine123.txt', "r", encoding='utf8') as m:
    medicine = m.readlines()

with open(r'E:/OCR/message.txt', "r", encoding='utf8') as s:
    msg = s.readlines()

jieba.load_userdict('E:/OCR/medicine123.txt')

content = [x.strip() for x in content]
# medicine123 = [x.strip() for x in medicine]
msg = [x.strip() for x in msg]
msg = ''.join(msg)
msg = msg.replace(' ', "")
for i in content:
    msg = msg.replace(i, "")
    
# print(msg)
# print('=' * 20)

# s = msg.find('娃名') + 2
# ocr_name = msg[s:s + 3]
# print("姓名:" + ocr_name)

# s = msg.find('目期') + 2
# ocr_date = msg[s:s + 7]
# print("看診日期:" + ocr_date)

# s = msg.find('院所名稱') + 4
# ocr_h_name = msg[s:s + 7]
# print("院所名稱:" + ocr_h_name)

# print("===========================")
# new_msg = filter(lambda ch: ch in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',msg)
# print(''.join(list(new_msg)))


# 精确模式
seg_list = jieba.cut(msg, cut_all=False)
# msg_list = jieba.cut(new_msg, cut_all=False)

print("Default Mode: " + "/ ".join(seg_list))
print('=' * 20)
# print("Default Mode: " + "/ ".join(msg_list))
# print('=' * 20)