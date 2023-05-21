import telebot
import requests, json
from telebot import types 
import random,string,time,os,sys
##################################################
headerss = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Host': 'api.telegram.org',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
#########################
own = 58648607388 #id owner
sown = "5864860738" # id owner
ch = "@l_e_a_r_n" #channel
tokenn="" #token
bot = telebot. TeleBot(tokenn)
#########################
Kdm = types.InlineKeyboardButton(text = "~ KDMTEAM .", url="t.me/L_e_a_r_n")    
PRO = types.InlineKeyboardButton(text ="~ ᏇᏲᎨᏡᏋᎮᖇᎧ ᴀʟᴏɴᴇ ‌...↻.", url="t.me/PPRRO0")
mc = types.InlineKeyboardMarkup()
mc.row_width = 1
mc.add(Kdm,PRO)
##############
#################################################################
@bot.message_handler(commands=['start'])
def start(message):
  if message.chat.type == 'private':
    if message.from_user.id != own: #whitepro
        id = message.from_user.id
        req = requests.get(f'https://api.telegram.org/bot{tokenn}/getChatMember?chat_id={ch}&user_id={id}', headers=headerss) #whitepro 
        re=req.text
        try:
          if str(req.json()['result']['status']) == 'left' :
            chane = types.InlineKeyboardButton(text ="~ KDMTEAM .", url="t.me/L_e_a_r_n")
            goch = types.InlineKeyboardMarkup()
            goch.add(chane)
            bot.send_message(message.chat.id, text=f'◍ You should join in channel for bot 🔰\n◍ {ch} .', reply_markup = goch)
          elif "creator" in re or "member" in re or "administrator" in re:
            idu = str(message.from_user.id)
            Hb = json.load(open('data.json', 'r')) #whitepro
            Hb["members"] 
            if idu not in Hb["members"] :
                Hb["total"] = Hb["total"] + 1
                Hb["members"].append(idu)
                with open("data.json", "w") as f:
                    json.dump(Hb, f,indent=4)
                idu = message.from_user.id
                use = message.from_user.username #whitepro 
                fr = message.from_user.first_name
                Hb = json.load(open('data.json', 'r'))
                bot.send_message(f"{sown}" ,f"""< [{fr}](tg://user?id={idu}) >
𖡋 ID : `{idu}` ✈️
𖡋 User : `@{use}` 🛩️
𖡋 Count : {Hb["total"]}👤""",parse_mode ="Markdown")#whitepro
            f2 = message.from_user.first_name
            t2 = message.from_user.id
            bot.send_message(message.chat.id,'''𖡋 Wellcome sir,، [{}](tg://user?id={}).
⚡The bot uses the same model as the ChatGPT : GPT 3.5🖇️
◍ Language bot : Python🐍.'''.format(f2,t2),parse_mode="markdown",reply_to_message_id=message.message_id,reply_markup=mc)
        except:
            chane = types.InlineKeyboardButton(text ="~ KDMTEAM .", url="t.me/L_e_a_r_n")
            goch = types.InlineKeyboardMarkup() #whitepro 
            goch.add(chane)
            bot.send_message(message.chat.id, text='◍ عليك الاشتراك في قناه البوت لتتمكن من استخدامه🔰\n@l_e_a_r_n .', reply_markup = goch)
    if message.from_user.id == own:
        bot.reply_to(message,"wellcome whitepro.")
@bot.message_handler(func=lambda m:True)
def Messages(message):
    if message.chat.type == 'private':
        ms=message.text
        if ms in ["ماذا قولت", "قولت اي", "قولت اي من شويه", "what did you say?"] :
            data = json.load(open('logs.json', 'r'))
            user=str(message.from_user.id)
            if user in data["logs"]: #whitepro 
                say=data["logs"][user]
                bot.reply_to(message,f"""*◍ Last write recently.*
*◍ You say :* `{say}`""", parse_mode = "Markdown")
                pass
            else:
                bot.reply_to(message,"""*◍ You didn't say anything. *""", parse_mode = "Markdown")
                pass
        ms= message.text
        if ms not in ["ماذا قولت", "قولت اي", "قولت اي من شويه", "what did me say?"] :
            try:
                data = json.load(open('logs.json', 'r'))
                user=str(message.from_user.id)
                data["logs"][user] = ms
                json.dump(data, open('logs.json', 'w'))
                res = gpt(ms) #whitepro 
                bot.reply_to(message,"""*◍ Response : * \n"""+res, parse_mode = "Markdown")
            except:
                print('error')
                
def gpt(ms) -> str: #whitepro 
	url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'
	headers = {
	    'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
	    'Connection': 'keep-alive',
	    'If-None-Match': 'W/"1c3-Up2QpuBs2+QUjJl/C9nteIBUa00"',
	    'Accept': '*/*',
	    'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/15.6.1 hw/iPhone8_2',
	    'Content-Type': 'application/json',
	    'Accept-Language': 'en-GB,en;q=0.9'
	}
	
	data = {
	    'data': {
	        'message':ms,
	    }
	}
	
	response = requests.post(url, headers=headers, data=json.dumps(data)) #whitepro 
	try:
		result = response.json()["result"]["choices"][0]["text"]
		return result
	except:
		return None
bot.infinity_polling() #whitepro 