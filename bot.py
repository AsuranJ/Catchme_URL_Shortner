# DO NOT REMOVE CREDITS
# Copyright (c) 2021 dakshy/droplink-bot with JAsuran
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from os import environ
import aiohttp
from pyrogram import Client, filters

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')

API_KEY = environ.get('API_KEY', 'e3eddb3e7c5513eee187120fce788ddc4a1a643b')
API_KEY1 = environ.get('API_KEY1', 'e3eddb3e7c5513eee187120fce788ddc4a1a643b')
API_KEY2 = environ.get('API_KEY2', 'e3eddb3e7c5513eee187120fce788ddc4a1a643b')
API_KEY3 = environ.get('API_KEY3', 'e3eddb3e7c5513eee187120fce788ddc4a1a643b')
API_KEY4 = environ.get('API_KEY4', 'e3eddb3e7c5513eee187120fce788ddc4a1a643b')
API_KEY5 = environ.get('API_KEY5', 'e3eddb3e7c5513eee187120fce788ddc4a1a643b')


bot = Client('droplink bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)


@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\n"
        "I'm a specialised bot for shortening Droplink, EarnClick, Pdiskshortner, adrinolinks, short2url, indianshortner links which can help you earn money by just sharing links. Made by <a href=\"https://t.me/JAsuranBots\">JAsuran Bots</a>.")


@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    links = message.text
    links = links.split("\n")
    for num in range(len(links)):
      try:
        short_link = await get_shortlink(links[num])
        short_link1 = await get_shortlink1(links[num])
        short_link2 = await get_shortlink2(links[num])
        short_link3 = await get_shortlink3(links[num])
        short_link4 = await get_shortlink4(links[num])
        short_link5 = await get_shortlink5(links[num])
        await message.reply(f'**Shortened URLs:**\n\n{short_link}\n\n{short_link1}\n\n{short_link2}\n\n{short_link3}\n\n{short_link4}\n\n{short_link5}', quote=True, disable_web_page_preview=True)
      except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


async def get_shortlink(link):
    url = 'https://droplink.co/api'
    params = {'api': API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]
          
async def get_shortlink1(link):
    url1 = 'https://earnforclick.online/api'
    params = {'api': API_KEY1, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url1, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]

async def get_shortlink2(link):
    url2 = 'https://pdiskshortener.in/api'
    params = {'api': API_KEY2, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url2, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]

async def get_shortlink3(link):
    url3 = 'https://adrinolinks.in/api'
    params = {'api': API_KEY3, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url3, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]

async def get_shortlink4(link):
    url4 = 'https://short2url.in/api'
    params = {'api': API_KEY4, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url4, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]

async def get_shortlink5(link):
    url5 = 'https://indianshortner.com/api'
    params = {'api': API_KEY5, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url5, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]


bot.run()
