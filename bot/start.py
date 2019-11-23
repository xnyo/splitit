from aiogram import types

from singletons.bot import Bot

bot = Bot()


@bot.dispatcher.message_handler(commands=["start"])
async def start_command(message: types.Message) -> None:
    await message.reply(
        "✂️🎶 **Welcome to Splitit Bot!**\n"
        "I can separate vocals from instrumental for any song you send me using machine learning.\n\n"
        "🤖 Uses [Spleeter](https://github.com/deezer/spleeter) by Deezer\n"
        "🐍 Bot made by [Nyo](t.me/bibbobebe). [Source code here](https://github.com/xnyo/splitit).\n",
        parse_mode="markdown",
        disable_web_page_preview=True,
        reply=False
    )
