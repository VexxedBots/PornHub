from telethon import events

import asyncio

@borg.on(outgoing=True, pattern="^.shoot$")
async def killing (killed):
    """ Dont Kill Too much -_-"""
    if not killed.text[0].isalpha() and killed.text[0] not in ("/", "#", "@", "!"):
        if await killed.get_reply_message():
            await killed.edit(
                "Targeted user killed by Headshot 😈......\n"
  "#Sad_Reacts_Onli\n"
            )
