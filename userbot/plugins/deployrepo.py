from userbot.Config import Config
from userbot import bot 

O = Config.OWNER_ID
Name = bot.me.first_name
M = f"[{Name}](tg://user?id={O})"

A = "https://t.me/JAI6H"

B = "**⌔∮ اهلا عزيزي - {} \n⌔∮ مطور الملفات - [اضغط هنا]({})**"

@icssbot.on(icss_cmd(pattern="مطور السورس"))
async def _(e):
    await eor(e, B.format(M, A))
