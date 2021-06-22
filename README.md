# VideoClips

Веб-сервис сохранения ссылок на понравившиеся фрагменты из видео (YouTube)

## how to run the app

- powershell run:

```sh
($env:FLASK_APP="webapp.server") -and ($env:FLASK_ENV="development") -and ($env:FLASK_DEBUG=1) -and (flask run)
```

- cmd run:

```sh
set FLASK_APP=webapp.server&& set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
```
