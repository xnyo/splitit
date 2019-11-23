# splitit
> Telegram wrapper for Deezer's Spleeter
Live demo available [@splititbot](https://t.me/splititbot)

## Requirements
- Python 3

## Installing
```bash
$ git clone ...
$ virtualenv -p $(which python3.7) .pyenv
$ source .pyenv/bin/activate
(.pyenv)$ TELEGRAM_API_TOKEN=... python splitit.py
```

## TODO
- [ ] Limit number of concurrent tasks
- [ ] Support for other stem modes rather than just stems 2
- [ ] Output audio metadata
- [ ] Automatically clear 'temp' folder
- [ ] Check if the audio was already separated before converting it

## Licence
MIT