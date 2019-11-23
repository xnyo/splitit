import asyncio
import os

from aiogram import types
from aiogram.types import ContentType
import spleeter
import spleeter.audio.adapter
import spleeter.utils.configuration
import spleeter.separator

from singletons.bot import Bot
from utils.general import random_string

bot = Bot()


def do_separate(input_file: str):
    def work():
        separator = spleeter.separator.Separator("spleeter:2stems")
        audio_adapter = spleeter.audio.adapter.get_default_audio_adapter()
        waveform, _ = audio_adapter.load(
            input_file,
            offset=0,
            duration=600.,
            sample_rate=separator._sample_rate
        )
        sources = separator.separate(waveform)
        filename = os.path.basename(input_file)
        generated = []
        for instrument, data in sources.items():
            path = os.path.join(
                f"temp/out/{'.'.join(filename.split('.')[:-1])}",
                f"{instrument}.mp3"
            )
            if path in generated:
                raise ValueError(f'Separated source path conflict : {path}, please check your filename format')
            generated.append(path)
            task = separator._pool.apply_async(
                audio_adapter.save, (
                    path,
                    data,
                    separator._sample_rate,
                    "mp3",
                    "128k"
                )
            )
            separator._tasks.append(task)
        separator.join()
        return generated
    return asyncio.get_event_loop().run_in_executor(None, work)


@bot.dispatcher.message_handler(content_types=ContentType.AUDIO)
async def splitit(message: types.Message) -> None:
    wait_message = await message.reply(
        "⚙️ **Separating! This may take a while.**",
        parse_mode="markdown"
    )
    while True:
        file_name = random_string()
        if not os.path.isfile(f"temp/in/{file_name}.mp3"):
            break
    input_file = f"temp/in/{file_name}.mp3"
    await message.audio.download(input_file)
    os.mkdir(f"temp/out/{file_name}")
    try:
        files = await do_separate(input_file)
        for file_path in files:
            with open(file_path, "rb") as f:
                await message.reply_audio(f)
        await wait_message.delete()
    except Exception as e:
        await message.reply(f"⚠️ **An error occurred!**\n{str(e)}", parse_mode="markdown")
