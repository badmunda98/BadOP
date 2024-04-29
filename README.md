``` python

import asyncio, os, time, aiohttp
import aiohttp
from pyrogram import filters
from BadOP import BadOP as BADMUNDA
from PBXMUSIC import app

@app.on_message(filters.command("BadOP"))
async def BadOP(_, message):
    text = message.text[len("/BadOP") :]
    BADMUNDA(f"{text}").save(f"BadOP_{message.from_user.id}.png")
    await message.reply_photo(f"BadOP_{message.from_user.id}.png")
    os.remove(f"BadOP_{message.from_user.id}.png")

```
``` python
 pip install BadOP

```




# BadOP 


![Project Image](https://github.com/badmunda98/BadOP/blob/main/out.png)

