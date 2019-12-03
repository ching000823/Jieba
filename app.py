from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import random
import jieba

import sys
import datetime
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials as SAC
import jieba

app = Flask(__name__)

line_bot_api = LineBotApi('doldQy1bjeGYVejMl7LG+9AW/LIni5rd4QJTdgHmMX3LoZlCdYr6x6yeTBDUukYBPJ4TAMVroHRNrbyCFjmhMAkL25ilgdPZqYQRTcIEEbNrxdslDp4hNZWrH9UQOai0Fa88wfwFR4Lx2iJkM1hb/gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('81f5c89515438946881ef989c33b5667')

prev = {}

#衛福部
def movie():
    target_url = 'https://www.mohw.gov.tw/mp-1.html'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser') 
    content = ""
    for index, data in enumerate(soup.select('div.tabContent a')):
        if index == 6:
           return content
        print("data：")
        print(index)
        print(data)        
        title = data['title']
        link =  data['href']
        content += '{}\n{}\n\n'.format(title, link)
    return content

#新聞
# def apple_news():
#     target_url = 'https://www.commonhealth.com.tw/channel/42'
#     print('Start parsing News ...')
#     rs = requests.session()
#     res = rs.get(target_url, verify=False)
#     res.encoding = 'utf-8'
#     soup = BeautifulSoup(res.text, 'html.parser')   
#     content = []
#     for index, data in enumerate(soup.select('div.tab_target a')):
#         if index == 20:           
#             return content
    
#         title = data.find('title')
#         link =  data['href']
#         link2 = 'https:'+ data.find('img')['src']
#         content.append(title)
#         content.append(link)
#         content.append(link2)
#         print("data：")
#         print(content)   
#     return content
# def apple_news():
#     target_url = 'https://www.commonhealth.com.tw/channel/42'
#     rs = requests.session()
#     res = rs.get(target_url, verify=False)
#     res.encoding = 'utf-8'
#     soup = BeautifulSoup(res.text, 'html.parser')   
#     content = ""
#     for index, data in enumerate(soup.select('div.tab_target a')):
#         if index ==10:           
#             return content
#         print(data)  
#         title = data.find('recommend__text')['title']['a']
#         link =  data['href']
#         link2 = 'https:'+ data.find('img')['src']
#         content+='{}\n{}\n{}\n'.format(title,link,link2)
#     return content



@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route("/", methods=['POST'])   
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print("Request body: " + body, "Signature: " + signature)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
       abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    print(msg)
    #print(type(msg))
    msg = msg.encode('utf-8')  
    a = ""
# def received_text(event):
#     params['events'][0]['message']['text']

    # 字典
    user_id = event.source.user_id
    ans = event.message.text    		
    # global prev
    # prev=dict()
    # prev={user_id:ans}
    # print(prev)

    if event.message.text == "新聞":
        # prev={user_id:ans} 
        a=movie()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=a))

    elif event.message.text == "你好":
        # prev={user_id:ans} 
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))
    elif event.message.text == "貼圖":        
        # prev={user_id:ans} 
        print("貼圖get")
        line_bot_api.reply_message(event.reply_token,StickerSendMessage(package_id=1, sticker_id=2))
    
    # if event.message.text == "News":
    #     a=apple_news()
        # g=[]
        # h=[]
        # n=[]    
        # for i in range(0,len(a),3):   
        #     g.append(a[i])
        #     h.append(a[i+1])
        #     n.append(a[i+2])
        # m=[] 
        # x=['title','link','link2']
        # m.append(g)
        # m.append(h)
        # m.append(n)
        # dictionary = dict(zip(x,m))
        # p=random.sample(range(12),3)
        # Image_Carousel = TemplateSendMessage(
        # alt_text='目錄 template',
        # template=ImageCarouselTemplate(
        # columns=[
        #     ImageCarouselColumn(
        #         image_url=dictionary['link2'][p[0]],
        #         action=URITemplateAction(
        #             uri=dictionary['link'][p[0]],
        #             label=dictionary['title'][p[0]][0:11]
        #         )
        #     ),
        #     ImageCarouselColumn(
        #         image_url=dictionary['link2'][p[2]],
        #         action=URITemplateAction(
        #             uri=dictionary['link'][p[2]],
        #             label=dictionary['title'][p[2]][0:11]
        #         )
        #     ),
        #     ImageCarouselColumn(
        #         image_url=dictionary['link2'][p[1]],
        #         action=URITemplateAction(
        #         uri=dictionary['link'][p[1]],
        #         label=dictionary['title'][p[1]][0:11]
        #         )
        #     )
        #     ]))
        # line_bot_api.reply_message(event.reply_token,Image_Carousel)
        # line_bot_api.reply_message(event.reply_token,TextSendMessage(text=a))
    




    # elif event.message.text == "樣板":
    #     print("TEST1")       
    #     buttons_template = TemplateSendMessage(
    #     alt_text='目錄 template',
    #     template=ButtonsTemplate(
    #         title='Template-樣板介紹',
    #         text='Template分為四種，也就是以下四種：',
    #         thumbnail_image_url='圖片網址',
    #         actions=[
    #             MessageTemplateAction(
    #                 label='Buttons Template',
    #                 text='Buttons Template'
    #             ),
    #             MessageTemplateAction(
    #                 label='Confirm template',
    #                 text='Confirm template'
    #             ),
    #             MessageTemplateAction(
    #                 label='Carousel template',
    #                 text='Carousel template'
    #             ),
    #             MessageTemplateAction(
    #                 label='Image Carousel',
    #                 text='Image Carousel'
    #             )
    #         ]
    #     )
    # )
        # line_bot_api.reply_message(event.reply_token, buttons_template)
    # elif event.message.text == "Buttons Template":
    #     print("TEST")       
    #     buttons_template = TemplateSendMessage(
    #     alt_text='Buttons Template',
    #     template=ButtonsTemplate(
    #         title='這是ButtonsTemplate',
    #         text='ButtonsTemplate可以傳送text,uri',
    #         thumbnail_image_url='https://media.wsls.com/photo/2017/04/24/Whats%20News%20Today_1493062809311_9576980_ver1.0_1280_720.png',
    #         actions=[
    #             MessageTemplateAction(
    #                 label='ButtonsTemplate',
    #                 text='ButtonsTemplate'
    #             ),
    #             URLTemplateAction(
    #                 label='VIDEO1',
    #                 url='網址'
    #             ),
    #             PostbackTemplateAction(
    #             label='postback',
    #             text='postback text',
    #             # data='postback1'
    #             )
    #         ]
    #     )
    # )
    #     line_bot_api.reply_message(event.reply_token, buttons_template)

    elif event.message.text=='說明':
        message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://attach.setn.com/newsimages/2017/02/10/805406-XXL.jpg',
                title='請選擇想要查看的項目~',
                text='Please select',
                actions=[
                    # PostbackTemplateAction(
                    #     label='postback',
                    #     text='postback text',
                    #     data='action=buy&itemid=1'
                    # ),
                    MessageTemplateAction(
                        label='新聞',
                        text='新聞'
                    ),
                    MessageTemplateAction(
                        label='康健雜誌',
                        text='康健雜誌'
                    ),
                    URITemplateAction(
                        label='看更多~~',
                        uri='https://www.commonhealth.com.tw/'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text=='康健雜誌':
        mesg = TemplateSendMessage(
            alt_text='ImageCarousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://as.chdev.tw/web/article/4/f/4/4e6208d3-f726-4b00-9ed8-b7a40ae8d777/A0968004.jpg',
                        action=URIAction(
                            label='40萬人健檢才知高血壓',
                            uri='https://www.commonhealth.com.tw/article/article.action?nid=80116',
                            data='action=buy&itemid=1'
                        )   
                    ),
                    ImageCarouselColumn(
                        image_url='https://as.chdev.tw/web/article/3/5/4/38564707-5b5e-4d20-9c6c-1aa1a54a69b51567406227.jpg',
                        action=URIAction(
                            label='改善腸躁症',
                            uri='https://www.commonhealth.com.tw/article/article.action?nid=80073',
                            data='action=buy&itemid=2'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, mesg)

    elif event.message.text == "OCR":
        prev[event.source.user_id] = "OCR"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='好的~請輸入您的OCR掃描~')
        )

    else:
        if prev[user_id]=="OCR":
            # line_bot_api.reply_message(
            #     event.reply_token,
            #     TextSendMessage("好的~請輸入OCR結果，結束OCR訊息請輸入[確認]")
            # )
            # ans = event.message.text
            # ans = ocr(event, ans)

            ocr(event)

            prev.update({user_id: ''})
           
        # elif prev[user_id]=="確認":
        #     line_bot_api.reply_message(event.reply_token,TextSendMessage(text='結束結巴'))
                           
        else :            
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage("我聽不懂您的意思")
            )

    # prev={user_id:ans}
    print(prev)
    return 'OK2'

   

    # if prev[user_id]=='輸入看診資訊':


    # elif event.message.text == "Carousel template":
    #     print("Carousel template")       
    #     Carousel_template = TemplateSendMessage(
	# 		alt_text='目錄 template',
	# 		template=CarouselTemplate(
	# 			columns=[
	# 				CarouselColumn(
	# 					thumbnail_image_url='網址',
	# 					title='this is menu1',
	# 					text='description1',
	# 					actions=[
	# 						PostbackTemplateAction(
	# 							label='postback1',
	# 							text='postback text1',
	# 							data='action=buy&itemid=1'
	# 						),
	# 						MessageTemplateAction(
	# 							label='message1',
	# 							text='message text1'
	# 						),
	# 						URITemplateAction(
	# 							label='uri1',
	# 							uri='網址'
	# 						)
	# 					]
	# 				),
	# 				CarouselColumn(
	# 					thumbnail_image_url='網址',
	# 					title='this is menu2',
	# 					text='description2',
	# 					actions=[
	# 						PostbackTemplateAction(
	# 							label='postback2',
	# 							text='postback text2',
	# 							data='action=buy&itemid=2'
	# 						),
	# 						MessageTemplateAction(
	# 							label='message2',
	# 							text='message text2'
	# 						),
	# 						URITemplateAction(
	# 							label='連結2',
	# 							uri='網址'
	# 						)
	# 					]
	# 				)
	# 			]
	# 		)
	# 	)
    #     line_bot_api.reply_message(event.reply_token,Carousel_template)
	
#OCR------------------------------------------------------------------------------------    
def ocr(event):
    print("Recieve")
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text="Recieve"))

    with open(r'./symbol.txt', "r", encoding='utf8') as f:
       content = f.readlines()

    with open(r'./medicine123.txt', "r", encoding='utf8') as m:
       medicine = m.readlines()

    # with open(r'./message.txt', "r", encoding='utf8') as s:
    #    msg = s.readlines()
    #    ans = event.message.text
    #    msg = ans

       jieba.load_userdict('medicine123.txt')

       content = [x.strip() for x in content]
# medicine123 = [x.strip() for x in medicine]
    #    global msg
       message = event.message.text
       msg= message

       msg = [x.strip() for x in msg]
       msg = ''.join(msg)

       msg = msg.replace(' ', "")
    
    for i in content:
       msg = msg.replace(i, "")

    s = msg.find('姓名') + 2 
    ocr_name = msg[s:s + 3]
    print("姓名:" + ocr_name)

    s = msg.find('日期') + 2
    ocr_date = msg[s:s + 7] 
    print("看診日期:" + ocr_date)

    s = msg.find('院所名稱') + 4
    ocr_h_name = msg[s:s + 7]
    print("院所名稱:" + ocr_h_name)
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage("姓名:" + ocr_name  + "\n看診日期:" + ocr_date  + "\n院所名稱:" + ocr_h_name)
    )

# 精确模式
    seg_list = jieba.cut(msg, cut_all=False)

    print("Default Mode: " + "/ ".join(seg_list))
    print('=' * 20)
    print("okkkkkkkkkkkkkkk")
#--------------------------------------------------------------------------------------------------


            
@handler.add(PostbackEvent)
def handle_post_message(event):
    print('-'*20)
    print("event =", event)
    print('-'*20)

    user_id = event.source.user_id
    print(user_id)

if __name__ == "__main__":
    app.run(debug=True,port=80)