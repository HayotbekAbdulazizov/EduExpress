import time
import schedule
import requests


def telegram_bot_sendtext(bot_message):
    
    bot_token = '5172024450:AAEOAQZwyEW1a_05ncUgZXhYtiGVDGlW6w4'
    bot_chatID = '-780196226'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

def telegram_bot_sendphoto(bot_message, image):
    
    bot_token = '5243600813:AAHWy1-dOYnlhkfPvRpmIjqCSd3YgvDpXKc'
    bot_chatID = '@padding_pack'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendPhoto?chat_id=' + bot_chatID + '&parse_mode=Markdown&caption=' + bot_message+'&photo='+ image

    response = requests.get(send_text)

    return response.json()

