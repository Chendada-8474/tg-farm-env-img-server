from telegram.ext import Updater, ExtBot, MessageHandler, Filters, CallbackQueryHandler, CommandHandler, ConversationHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import os
from closest_site import closest_site
from datetime import datetime
from pykml import parser
from easygui import fileopenbox

dirs = os.listdir("./")

if "token.txt" not in dirs:
    TOKEN = input("請輸入 token")

else:
    f = open('./token.txt')
    TOKEN = f.read() # Token of Cane Toad Reporting
    f.close

if "chat_id.txt" not in dirs:
    CHAT_ID = input("請輸入 chat_id")
else:
    f = open('./chat_id.txt')
    CHAT_ID = str(f.read()) # Token of Cane Toad Reporting
    f.close

if "route.kml" not in dirs:
    route_path = fileopenbox()

    with open(route_path , encoding='utf-8') as kml_route:
        route = parser.parse(kml_route).getroot().Document.Folder

else:
    with open("./route.kml" , encoding='utf-8') as kml_route:
        route = parser.parse(kml_route).getroot().Document.Folder


bot = ExtBot(TOKEN)

current_site = None

def start(update, context):
    user_id = str(update.message.chat.id)
    if user_id != CHAT_ID:
        return

    bot.send_message(CHAT_ID, '請先確認好四個方位角，並建議依序拍下\n"東->南->西->北" 四張環境照\n準備好照片後\n請分享你目前的點位')

    return 1

def location(update, context):
    global current_site, all_sites, dir_name

    year = str(datetime.now().year)
    if len(str(datetime.now().month)) == 1 :
        month = "0" + str(datetime.now().month)
    else:
        month = str(datetime.now().month)
    dir_name = year + month + "照片"

    if dir_name not in os.listdir("./"):
        os.mkdir(dir_name)

    x = update.message.location.longitude
    y = update.message.location.latitude
    current_site, all_sites = closest_site(x, y, route)

    yn = {
        "是": "yes",
        "不是": "no",
        "取消": "cancel",
    }

    bot.send_message(CHAT_ID, "請問 %s 是目前的樣線嗎？" % current_site, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(i, callback_data = yn[i]) for i in yn.keys()]]))


    return 2

def site_yn(update, context):
    yn = update.callback_query.data

    if yn == "yes":
        bot.send_message(CHAT_ID, "你選擇了 %s" % current_site)
        bot.send_message(CHAT_ID, "請上傳向東的照片")
        return 4

    elif yn == "no":
        bot.send_message(CHAT_ID, "請手動輸入樣線名稱：")
        return 3

    elif yn == "cancel":
        bot.send_message(CHAT_ID, "已取消")
        return ConversationHandler.END


def site_name(update, context):
    global current_site
    user_mes = update.message.text

    if user_mes in all_sites:
        current_site = user_mes
        bot.send_message(CHAT_ID, "你選擇了 %s" % user_mes)
        bot.send_message(CHAT_ID, "請上傳向東的照片")
        return 4

imgs = []

def get_photo_e(update, context):
    imgs.append(bot.getFile(update.message.photo[-1].file_id))
    bot.send_message(CHAT_ID, "請上傳向南的照片")
    return 5


def get_photo_s(update, context):
    imgs.append(bot.getFile(update.message.photo[-1].file_id))
    bot.send_message(CHAT_ID, "請上傳向西的照片")
    return 6


def get_photo_w(update, context):
    imgs.append(bot.getFile(update.message.photo[-1].file_id))
    bot.send_message(CHAT_ID, "請上傳向北的照片")
    return 7


def get_photo_n(update, context):
    imgs.append(bot.getFile(update.message.photo[-1].file_id))
    yn = {
        "上傳": "yes",
        "取消": "no",
    }

    bot.send_message(CHAT_ID, "確認上傳？", reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(i, callback_data = yn[i]) for i in yn.keys()]]))
    return 8


def up_load(update, context):
    yn = update.callback_query.data

    if yn == "yes":
        bot.send_message(CHAT_ID, "上傳中...")
        for ewsn, img in zip(("東", "南", "西", "北"), imgs):
            img.download('./%s/%s_%s.jpg' % (dir_name, current_site, ewsn))
        bot.send_message(CHAT_ID, "已成功上傳")
        return ConversationHandler.END

    elif yn == "no":

        bot.send_message(CHAT_ID, "已取消上傳")
        return ConversationHandler.END


def cancel(update, context):
    return ConversationHandler.END


updater = Updater(TOKEN)
updater.dispatcher.add_handler(ConversationHandler(
    [CommandHandler('start', start)], {
        1: [MessageHandler(Filters.location, location)],
        2: [CallbackQueryHandler(site_yn)],
        3: [MessageHandler(Filters.text, site_name)],
        4: [MessageHandler(Filters.photo ,get_photo_e)],
        5: [MessageHandler(Filters.photo ,get_photo_s)],
        6: [MessageHandler(Filters.photo ,get_photo_w)],
        7: [MessageHandler(Filters.photo ,get_photo_n)],
        8: [CallbackQueryHandler(up_load)],
        },
        [CommandHandler('cancel', cancel)]
        ))

updater.start_polling()
updater.idle()
