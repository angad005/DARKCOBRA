# By @Danish_00
# Fixed By a NOOB
# Made for DARK COBRA by team Cobra..
# kang with credits do not edit these lines..
from telethon.tl.types import MessageMediaPhoto
import os, urllib, requests, asyncio
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern="toonify$", outgoing=True))
async def detect(event):
    if Config.DEEP_AI is None:
        return await event.edit(
             "Add VAR DEEP_AI get Api Key from https://deepai.org/")
               
    reply = await event.get_reply_message()
    if not reply:#By @Danish_00
#Fixed By a NOOB
        return await event.edit(
           "Reply to any image or non animated sticker !"
        )
    catevent = await event.edit("Downloading the file to check...")
    media = await event.client.download_media(reply)
    if not media.endswith(("png", "jpg", "webp")):
        return await event.edit(
             "Reply to any image or non animated sticker !"
        )#By @Danish_00
#Fixed By a NOOB
    devent = await event.edit("making this cartoon 😂😂😂😂...")
    r = requests.post(
        "https://api.deepai.org/api/toonify",
        files={
            "image": open(media, "rb"),
        },
        headers={"api-key": Config.DEEP_AI},
    )#By @Danish_00
#Fixed By a NOOB
    os.remove(media)
    if "status" in r.json():
        return await devent.edit( r.json()["status"])
    r_json = r.json()["output_url"]
    pic_id = r.json()["id"]
    
    link = f"https://api.deepai.org/job-view-file/{pic_id}/inputs/image.jpg"
    result = f"{r_json}"
    
    await devent.delete()
    await borg.send_message(
        event.chat_id,
        file=result
    )
