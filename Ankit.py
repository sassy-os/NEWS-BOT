import requests
from telethon import TelegramClient
from telethon import events
import os
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
APP_ID = os.environ.get("APP_ID", default=None)
API_HASH = os.environ.get("API_HASH", default=None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", default=None)


bot = TelegramClient("NEWS-BOT", APP_ID, API_HASH)
start = ankit.start(bot_token=BOT_TOKEN) 



@ankit.on(events.NewMessage(pattern="^/start"))
async def _(event):
    await event.reply('''нεү,ι'м үσυя ηεωsραρρεя вσт ρεσρℓε cαη υsε мε тσ яεα∂ ∂αιℓү υρ∂αтε∂ ηεωs.נυsт вү нιттιηg cσммαη∂ - /news \n \n мα∂ε ωιтн ℓσvε вү - @AbOuT_xNKIT 💙 ''')



@ankit.on(events.NewMessage(pattern="^/news ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    infintyvar = event.pattern_match.group(1)
    main_url = f"https://inshortsapi.vercel.app/news?category={infintyvar}"
    stuber = await event.reply(
        f"Ok ! ғεcтcнιηg {infintyvar} ғяσм ιηsнσятsαρι sεяvεя αη∂ sεη∂ιηg тσ ηεωs cнαηηεℓ",
    )
    await stuber.edit("αℓℓ ηεωs нαs вεεη sυccεssғυℓℓү ғεтcнε∂, sεη∂ιηg тσ үσυ.")
    starknews = requests.get(main_url).json()
    for item in starknews["data"]:
        sedlyf = item["content"]
        img = item["imageUrl"]
        writter = item["author"]
        dateis = item["date"]
        readthis = item["readMoreUrl"]
        titles = item["title"]
        sed1 = img
        sedm = f"**Title : {titles}** \n{sedlyf} \nDate : {dateis} \nAuthor : {writter} \nReadMore : {readthis}"
        await bot.send_file(event.chat_id, sed1, caption=sedm)





print ("sυccεssғυℓℓү sтαятε∂")
start.run_until_disconnected()
