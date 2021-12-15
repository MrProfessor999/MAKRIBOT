# This Repo was not fully owned by me. Some codes are scraped from respected DEVOLEPERS whom where mine friends. 
# check Readme.md For More. 

import logging
logger = logging.getLogger(__name__)
import os, re, time, math, json, string, random, traceback, wget, asyncio, datetime, aiofiles, aiofiles.os, requests, youtube_dl, lyricsgenius
from config import Config
from random import choice 
import y_dl
from pyrogram import Client, filters
from youtube_search import YoutubeSearch
from youtubesearchpython import VideosSearch
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid


Bot = Client(
    "Song Downloader Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)



START_TEXT = """ Hai {}, 
Iam a song download Bot 🙂
"""

CMDS_TEXT = """
Hey {} This are this bots power🌠
"""

ABOUT_TEXT = """
✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵
╔════❰ 𝐀𝐁𝐎𝐔𝐓 ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣ 
║ 𝙈𝙔𝙉𝘼𝙈𝙀-𝐌𝐀𝐊𝐑𝐈_𝐒𝐎𝐍𝐆𝐁𝐎𝐓 
║┣⪼𝓓𝓮𝓿𝓸𝓵𝓸𝓹𝓮𝓻 -[𝐌𝐀𝐊𝐑𝐈](https://t.me/blesson_3)
║┣⪼ 𝓛𝓲𝓫𝓻𝓪𝓻𝓻𝔂 - [𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼](https://pyrogram.org)
║┣⪼ 𝓛𝓪𝓷𝓰𝓾𝓪𝓰𝓮 - [𝙿𝚈𝚃𝙷𝙾𝙽 𝟹](https://python.org)
║┣⪼ 𝓑𝓸𝓽 𝓼𝓮𝓻𝓿𝓮𝓻 -  [𝙷𝙴𝚁𝙾𝙺𝚄](https://heroku.com)
║┣⪼ 𝓑𝓾𝓲𝓵𝓭 𝓢𝓽𝓪𝓽𝓾𝓼 - v1.0.1 [ 𝙱𝙴𝚃𝙰 ]
║╰━━━━━━━━━━━━━━━➣ ╚══════════════════❍⊱❁۪۪
"""
MUSIC = """Help: <b>🎧MUSIC🎧</b>
➩ /music <songname artist(optional)>: uploads the song in it's best quality available
"""
 
VSONG = """Help: <b>📀VSONG📀</b>
➩ /vsong <songname artist(optional)>: uploads the video song in it's best quality available
"""
  
LYRICS = """Help: <b>🎶LYRICS🎶</b>
➩ /lyrics <songname>: uploads the lyrics of song
"""

YOUTUBE = """Help: <b>📽️YOUTUBE📽️</b>
➩ /ytaudio <youtubelink>: uploads the audio of song in it's best quality available
➩ /ytvideo <youtubelink>: uploads the video of song in it's best quality available
"""


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Support📕', url=f"https://telegram.me/{Config.SUPPORT}"), 
        InlineKeyboardButton(text="SEARCH🔎", switch_inline_query_current_chat="")
        ],[
        InlineKeyboardButton('HELPℹ️', callback_data ='cmds'),        
        InlineKeyboardButton('ABOUT😁', callback_data='about')        
        ]]
    )
CMDS_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🎧MUSIC🎧', callback_data='song'),
        InlineKeyboardButton('📀VSONG📀', callback_data='video')
        ],[
        InlineKeyboardButton('🎶LYRICS🎶', callback_data='lyrics'),
        InlineKeyboardButton('📽️YOUTUBE📽️', callback_data='youtube')
        ],[
        InlineKeyboardButton('🏠 Home', callback_data='home'),            
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('HOME🏡', callback_data='home'),
        InlineKeyboardButton('CLOSE🔐', callback_data='close')
        ]]
    )

@Bot.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "cmds":
        await update.message.edit_text(
            text=CMDS_TEXT.format(update.from_user.mention),
            reply_markup=CMDS_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "song":
        await update.message.edit_text(
            text=MUSIC,
            reply_markup=MUSIC_BUTTON,
            disable_web_page_preview=True
        )
    elif update.data == "video":
        await update.message.edit_text(
            text=VSONG,
            reply_markup=VSONG_BUTTON,
            disable_web_page_preview=True
        )
    elif update.data == "lyrics":
        await update.message.edit_text(
            text=LYRICS,
            reply_markup=LYRICS_BUTTON,
            disable_web_page_preview=True
        )
    elif update.data == "youtube":
        await update.message.edit_text(
            text=YOUTUBE,
            reply_markup=YOUTUBE_BUTTON,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()

        
@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):    
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),        
        reply_markup=START_BUTTONS,
        disable_web_page_preview=True	
    )

@Bot.on_message(filters.private & filters.command(["about"]))
async def about(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT,
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )



async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : blocked the bot\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))




	
@Bot.on_inline_query()
async def inline(client: Client, query: InlineQuery):
    answers = []
    search_query = query.query.lower().strip().rstrip()

    if search_query == "":
        await client.answer_inline_query(
            query.id,
            results=answers,
            switch_pm_text="Search your query here...🔎",
            switch_pm_parameter="help",
            cache_time=0
        )
    else:
        search = VideosSearch(search_query, limit=50)

        for result in search.result()["result"]:
            answers.append(
                InlineQueryResultArticle(
                    title=result["title"],
                    description="{}, {} views.".format(
                        result["duration"],
                        result["viewCount"]["short"]
                    ),
                    input_message_content=InputTextMessageContent(
                        "https://www.youtube.com/watch?v={}".format(
                            result["id"]
                        )
                    ),
                    thumb_url=result["thumbnails"][0]["url"]
                )
            )

        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text="Error: Search timed out",
                switch_pm_parameter="",
            )
        

@Bot.on_message(filters.command("lyrics"))
async def lrsearch(_, message: Message):  
    m = await message.reply_text("Searching Lyrics")
    query = message.text.split(None, 1)[1]
    x = "OXaVabSRKQLqwpiYOn-E4Y7k3wj-TNdL5RfDPXlnXhCErbcqVvdCF-WnMR5TBctI"
    y = lyricsgenius.Genius(x)
    y.verbose = False
    S = y.search_song(query, get_full_info=False)
    if S is None:
        return await m.edit("Lyrics not found..")
    xxx = f"""
**Lyrics Search Powered By Music Bot**
**Searched Song:-** __{query}__
**Found Lyrics For:-** __{S.title}__
**Artist:-** {S.artist}
**__Lyrics:__**
{S.lyrics}"""
    await m.edit(xxx)


def get_file_extension_from_url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    return basename.split(".")[-1]


def download_youtube_audio(url: str):
    global is_downloading
    with yt_dlp.YoutubeDL(
        {
            "format": "bestaudio",
            "writethumbnail": True,
            "quiet": True,
        }
    ) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        if int(float(info_dict["duration"])) > 180:
            is_downloading = False
            return []
        ydl.process_info(info_dict)
        audio_file = ydl.prepare_filename(info_dict)
        basename = audio_file.rsplit(".", 1)[-2]
        if info_dict["ext"] == "webm":
            audio_file_opus = basename + ".opus"
            ffmpeg.input(audio_file).output(
                audio_file_opus, codec="copy", loglevel="error"
            ).overwrite_output().run()
            os.remove(audio_file)
            audio_file = audio_file_opus
        thumbnail_url = info_dict["thumbnail"]
        thumbnail_file = (
            basename + "." + get_file_extension_from_url(thumbnail_url)
        )
        title = info_dict["title"]
        performer = info_dict["uploader"]
        duration = int(float(info_dict["duration"]))
    return [title, performer, duration, audio_file, thumbnail_file]


@pbot.on_message(filters.command(["vsong", "video"]))
async def ytmusic(client, message: Message):
    urlissed = get_text(message)

    pablo = await client.send_message(
        message.chat.id, f"`Getting {urlissed} From Youtube Servers. Please Wait.`"
    )
    if not urlissed:
        await pablo.edit("Invalid Command Syntax, Please Check Help Menu To Know More!")
        return

    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    thums = mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            infoo = ytdl.extract_info(url, False)
            duration = round(infoo["duration"] / 60)
            LIMIT = "180"          
 
            if duration > LIMIT:
                await pablo.edit(
                    f"❌ **durasinya kelamaan gabisa tot:v**"
                )
                is_downloading = False
                return
            ytdl_data = ytdl.extract_info(url, download=True)

    except Exception as e:
        await pablo.edit(f"**Failed To Download** \n**Error :** `{str(e)}`")
        return
    c_time = time.time()
    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"**Video Name ➠** [{thum}]({mo}) \n**Requested For :** `{urlissed}` \n**Channel :** `{thums}` "
    await client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        supports_streaming=True,
        progress=progress,
        progress_args=(
            pablo,
            c_time,
            f"`Uploading {urlissed} Song From YouTube Music!`",
            file_stark,
        ),
    )
    await pablo.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)


@pbot.on_message(filters.command(["music", "song"]))
async def ytmusic(client, message: Message):
    urlissed = get_text(message)
    if not urlissed:
        await client.send_message(
            message.chat.id,
            "Invalid Command Syntax, Please Check Help Menu To Know More!",
        )
        return
    pablo = await client.send_message(
        message.chat.id, f"`Getting {urlissed} From Youtube Servers. Please Wait.`"
    )
    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    mio[0]["duration"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    thums = mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    sedlyf = wget.download(kekme)
    opts = {
        "format": "bestaudio",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "writethumbnail": True,
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "720",
            }
        ],
        "outtmpl": "%(id)s.mp3",
        "quiet": True,
        "logtostderr": False,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(mo, download=True)
    except Exception as e:
        await pablo.edit(f"**Failed To Download** \n**Error :** `{str(e)}`")
        return
    c_time = time.time()
    capy = f"**Song Name :** [{thum}]({mo}) \n**Requested For :** `{urlissed}` \n**Channel :** `{thums}` "
    file_stark = f"{ytdl_data['id']}.mp3"
    await client.send_audio(
        message.chat.id,
        audio=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        title=str(ytdl_data["title"]),
        performer=str(ytdl_data["uploader"]),
        thumb=sedlyf,
        caption=capy,
        progress=progress,
        progress_args=(
            pablo,
            c_time,
            f"`Uploading {urlissed} Song From YouTube Music!`",
            file_stark,
        ),
    )
    await pablo.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)




Bot.run()
