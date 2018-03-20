# IoT-Telegram

## Description

An Internet of Things (IoT) light control using [Telgram Bot](https://telegram.org/blog/bot-revolution), an [ESPino](http://www.espino.io/en/) (esp8266 devolopment board) and [Orangepi One](http://www.orangepi.org/orangepizero/).
This project is divided in three parts:

|    Part       | Running on    | Developed on |
| ------------- |:-------------:| ------------:|
| Server        | Orangepi      | Python       |
| Bot           | Orangepi      | Python       |
| Light Control | ESPino        | Arduino      |


## How works?

1. Bot change ligth status on local database.
2. Every five minutes ESPino wake-up and do a request to Server to get light status and update pin out, then sleep again.