# TS3_StripeControl
Use a cheap MagicHome WiFi-RGBW-stripe-controller and the [pyTSon plugin for TeamSpeak3](https://www.myteamspeak.com/addons/86d2c267-1b43-4a4b-8cfb-06c2d8208bdc) to monitor the audio-status of your microphone or of your current channel. <br />
Based on [eventlog.py of pyTSon_repository](https://github.com/pathmann/pyTSon_repository/blob/master/eventlog.py)

## TS3_MicLight
You can define colors to show the state of your microphone. Default:

Color | Meaning
 --- | ---
![#ff0000](https://placehold.it/15/ff0000/000000?text=+) RED    | Microphone is muted
![#00ff00](https://placehold.it/15/00ff00/000000?text=+) GREEN  | You are speaking
![#fffacd](https://placehold.it/15/fffacd/000000?text=+) WHITE  | You are not speaking and your microphone isn't muted


## TS3_StatusLight
Changed Version of TS3_MicLight, uses the LED-Stripe-Channels for the events

Color | Meaning
 --- | ---
![#00ff00](https://placehold.it/15/00ff00/000000?text=+) GREEN  | You are speaking
![#00ffff](https://placehold.it/15/00ffff/000000?text=+) CYAN    | Someone else is speaking and you are speaking
![#0000ff](https://placehold.it/15/0000ff/000000?text=+) BLUE   | Someone else is speaking
![#ff00ff](https://placehold.it/15/ff00ff/000000?text=+) MAGENTA | Someone else is speaking and your microphone is muted
![#ff0000](https://placehold.it/15/ff0000/000000?text=+) RED    | Your microphone and/or speakers are muted
![#ff0000](https://placehold.it/7x15/ff0000/000000?text=+)![#000000](https://placehold.it/8x15/000000/000000?text=+) RED STROBE | You are trying to speak, but your microphone is muted
![#fffacd](https://placehold.it/15/fffacd/000000?text=+) WHITE  | Nobody is speaking and nothing is muted
