from asyncio import sleep


@icssbot.on(admin_cmd(pattern="sdm (\d*) (.*)", outgoing=True))
@icssbot.on(sudo_cmd(pattern="sdm (\d*) (.*)", allow_sudo=True))
async def selfdestruct(destroy):
    ics = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = ics[1]
    ttl = int(ics[0])
    try:
        await destroy.delete()
    except Exception as e:
        LOGS.info(str(e))
    smsg = await destroy.client.send_message(destroy.chat_id, message)
    await sleep(ttl)
    await smsg.delete()


@icssbot.on(admin_cmd(pattern="selfdm (\d*) (.*)", outgoing=True))
@icssbot.on(sudo_cmd(pattern="selfdm (\d*) (.*)", allow_sudo=True))
async def selfdestruct(destroy):
    ics = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = icss[1]
    ttl = int(icss[0])
    text = (
        message + f"\n\n`This message shall be self-destructed in {str(ttl)} seconds`"
    )
    try:
        await destroy.delete()
    except Exception as e:
        LOGS.info(str(e))
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(ttl)
    await smsg.delete()


CMD_HELP.update(
    {
        "selfdestruct": "**Plugin : **`selfdestruct`\
        \n\n**Syntax : **`.sdm [number] [text]`\
        \n**Function : **__self destruct this message in number seconds__\
        \n\n**Syntax : **`.selfdm [number] [text]`\
        \n**Function : **__self destruct this message in number seconds with showing that it will destruct. __\
"
    }
)
