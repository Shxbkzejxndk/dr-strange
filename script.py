class Script(object):
    START_TXT = """ππ·π΄π»πΎ {},

πΌπ π½π°πΌπ΄ πΈπ <a href=https://t.me/{}>{}</a>!


πΈπ'π ππ΄ππ π΄π°ππ. πΉπππ π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ π°π½π³ πΌπ°πΊπ΄ πΌπ΄ π°π³πΌπΈπ½, ππ·π°ππ π°π»π», πΈ'π»π» πΏππΎππΈπ³π΄ πΌπΎππΈπ΄π ππ·π΄ππ΄ π€"""

    HELP_TXT = """Hey {}

<b>Here Is The Help For My Commands.</b>"""

    ABOUT_TXT ="""β― πΌπ π½π°πΌπ΄: {}
β― π²ππ΄π°ππΎπ: <a href=https://t.me/Shamilmalik_10>SHAMIL MALIK</a>
β― π»πΈπ±ππ°ππ: πΏπππΎπΆππ°πΌ
β― π»π°π½πΆππ°πΆπ΄: πΏπππ·πΎπ½ πΉ
β― π³π°ππ° π±π°ππ΄: πΌπΎπ½πΆπΎ π³π±
β― π±πΎπ ππ΄πππ΄π: π·π΄ππΎπΊπ
β― π±ππΈπ»π³ πππ°πππ: v1.0.1 [ π±π΄ππ° ]"""
    SOURCE_TXT = """<b>Source:</b>
DΡ SΡΡΞ±ΠΈgeπ is a Open source project.
Source: <a href='https://github.com/Shxbkzejxndk/dr-strange'>GitHub - Click here π</a>"""

    MANUALFILTER_TXT =  """Help: <b>Filters</b>
- Filter is the feature were users can set automated replies for a particular keyword and DΡ SΡΡΞ±ΠΈgeπ will respond whenever a keyword is found the message
<b>NOTE:</b>
1. DΡ SΡΡΞ±ΠΈgeπ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.
<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>

- DΡ SΡΡΞ±ΠΈgeπ support both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. DΡ SΡΡΞ±ΠΈgeπ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/CLMRG)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1.  Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - connect a particular chat to your PM.
β’ /disconnect  - disconnect from a chat.
β’ /connections - list all your connections."""

    AUTO_MANUAL_TXT = """Help: <b>Filters</b>

<b>Select a filters type Below:</b>"""

    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>
β’ /paste [text] - paste the given text on Pasty
β’ /paste [reply] - paste the replied text on Pasty

<b>NOTE:</b>
β’ DΡ SΡΡΞ±ΠΈgeπ should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    TGRAPH_TXT = """Help: <b>TGraph & Paste</b>

Do as you wish with telegra.ph module!

<b>Commands and Usage:</b>
β’ /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

<b>NOTE:</b>
β’ DΡ SΡΡΞ±ΠΈgeπ should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    INFO_TXT = """Help: <b>Information</b>

Get information about something!

<b>Commands and Usage:</b>
β’ /id - get id of a specifed user.
β’ /info  - get information about a user.
β’ /json - get the json details of a message.

<b>NOTE:</b>
β’ DΡ SΡΡΞ±ΠΈgeπ should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    GTRANS_TXT = """Help: <b>Google Translator</b>

Translate texts to a specific language!

<b>Commands and Usage:</b>
β’ /tr [language code][reply] - translate replied message to specific language.

<b>NOTE:</b>
β’ DΡ SΡΡΞ±ΠΈgeπ should have admin privillage.
β’ These commands works on both pm and group.
β’ DΡ SΡΡΞ±ΠΈgeπ can translate texts to 200+ languages."""

    SEARCH_TXT = """Help: <b>IMDb</b>

Search many things without leaving telegram!

<b>Commands and Usage:</b>
β’ /imdb  - get the film information from IMDb source.
β’ /search  - get the film information from various sources.

<b>NOTE:</b>
β’ DΡ SΡΡΞ±ΠΈgeπ should have admin privillage.
β’ More search tools can be found on inline.
β’ Those commands works on both pm and group."""

    PURGE_TXT = """Help: <b>Purge</b>

Need to delete lots of messages? That's what purges are for!

<b>Commands and Usage:</b>
β’ /purge - delete all messages from the replied to message, to the current message.

<b>NOTE:</b>
β’ DΡ SΡΡΞ±ΠΈgeπ should have admin privillage.
β’ These commands works on group.
β’ These commands can be used by Only admin."""

    RESTRIC_TXT = """Help: <b>Restrictions</b>

Some people need to be publicly banned; spammers, annoyances, or just trolls.

This module allows you to do that easily, by exposing some common actions, so everyone will see!

<b>Commands and Usage:</b>
β’ /ban - ban a user.
β’ /tban - temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
β’ /mute - mute a user.
β’ /tmute - temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
β’ /unban or /unmute - unmute a user & unban a user.

<b>Examples:</b>
- Mute a user for two hours.
-> <code>/tmute @username 2h</code>

<b>NOTE:</b>
β’ DΡ SΡΡΞ±ΠΈgeπ should have admin privillage.
β’ These commands works on group.
β’ These commands can be used by Only admin."""

    PIN_MESSAGE_TXT = """Help: <b>Pin Message</b>

All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!

<b>Commands and Usage:</b>
β’ /pin: Pin the message you replied to. Add 'loud' or 'notify' to send a notification to group members.
β’ /unpin: Unpin the current pinned message. If used as a reply, unpins the replied to message.

<b>NOTE:</b>
β’ DΡ SΡΡΞ±ΠΈgeπ should have admin privillage.
β’ These commands works only group.
β’ These commands can be used by Only admin."""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - to get the rescent errors.
β’ /stats - to get status of files in db.
β’ /delete - to delete a specific file from db.
β’ /users - to get list of my users and ids.
β’ /chats - to get list of the my chats and ids.
β’ /leave - to leave from a chat.
β’ /disable - do disable a chat.
β’ /ban_users - to ban a user.
β’ /unban_users - to unban a user.
β’ /channel - to get list of total connected channels.
β’ /broadcast - to broadcast a message to all users."""

    STATUS_TXT = """<b>Total Files:</b> <code>{}</code>
<b>Total Users:</b> <code>{}</code>
<b>Total Chats:</b> <code>{}</code>
<b>Used Storage:</b> <code>{}</code> MiB
<b>Free Storage:</b> <code>{}</code> MiB"""

    FORCESUB_TXT = """**β¦οΈ READ THIS INSTRUCTION β¦οΈ**

__π£ In Order To Get The Movie Requested By You in Our Groups, You Will Have To Join Our main Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately π__

**π JOIN THIS CHANNEL & TRY AGAIN π**"""

    MEMES_TXT = """Help: <b>Memes</b>

Some dank memes for fun or whatever!

<b>Commands and Usage:</b>
β’ /throw or /dart - tπ mπΊππΎ drat 
β’ /roll or /dice - roll the dice 
β’ /goal or /shoot - to make a goal or shoot
β’ /luck or /cownd - Spin the Lucky
β’ /runs strings

<b>NOTE:</b>
β’ DΡ SΡΡΞ±ΠΈgeπ should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    URL_SHORTNER_TXT = """Help: <b>URL Shortner</b>

Some URLs is Shortner

<b>Commands and Usage:</b>
β’ /short <code>(link)</code> - I will send the shorted links.

<b>Example:</b>
<code>/short https://t.me/CLMRG</code>

<b>NOTE:</b>
β’ DΡ SΡΡΞ±ΠΈgeπ should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    TTS_TXT = """Help: <b>Text to Speech</b>

A module to convert text to voice with language support.

<b>Commands and Usage:</b>
β’ /tts - Reply to any text message with language code to convert as audio.

<b>NOTE:</b>
β’ DΡ SΡΡΞ±ΠΈgeπ should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    MUSIC_TXT = """Help: <b>Music</b>

Music download modules, for those who love music.

<b>Commands and Usage:</b>
β’ /song or /mp3 (songname) - download song from yt servers.
β’ /video or /mp4 (songname) - download video from yt servers.

<b>YouTube Thumbnail Download</b>
β’ /ytthumb (youtube link)
<b>Example:</b> <code>/ytthumb https://youtu.be/c9zr6aWbH0c</code>

<b>NOTE:</b>
β’ DΡ SΡΡΞ±ΠΈgeπ should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    PASSWORD_GEN_TXT = """Help: <b>Password Generator</b>

There Is Nothing To Know More. Send Me The Limit Of Your Password.
- I Will Give The Password Of That Limit.

<b>Commands and Usage:</b>
β’ /genpassword or /genpw <code>20</code>

<b>NOTE:</b>
β’ Only Digits Are Allowed
β’ Maximum Allowed Digits Till 84 
(I Can't Generate Passwords Above The Length 84)
β’ DΡ SΡΡΞ±ΠΈgeπ should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    ZOMBIES_TXT = """Help: <b>Zombies</b>

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
β’ /inkick - command with required arguments and i will kick members from group.
β’ /instatus - to check current status of chat member from group.
β’ /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
β’ /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
β’ /dkick - to kick deleted accounts."""

    CREATOR_REQUIRED = """βYou have to be the group creator to do that."""
      
    INPUT_REQUIRED = "β **Arguments Required**"
      
    KICKED = """βοΈ Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """π? Removing inactive members this may take a while..."""
      
    ADMIN_REQUIRED = """βI am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""
      
    DKICK = """βοΈ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""
