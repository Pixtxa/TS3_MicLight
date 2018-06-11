# TS3_StripeControl
Use a cheap MagigHome WiFi-RGBW-stripe-controller and the pyTSon plugin for TeamSpeak3 to monitor the audio-status of your microphone or of your current channel. <br />
Based on https://github.com/pathmann/pyTSon_repository/blob/master/eventlog.py

## TS3_MicLight
You can define colors to show the state of your microphone (sending/muted/idle)

## TS3_StatusLight
Changed Version of TS3_MicLight, uses the LED-Stripe-Channels for the events

Color | Meaning
 --- | ---
![#ff0000](https://placehold.it/15/ff0000/000000?text=+) RED    | Mic and/or speakers are muted
![#00ff00](https://placehold.it/15/00ff00/000000?text=+) GREEN  | You are speaking
![#0000ff](https://placehold.it/15/0000ff/000000?text=+) BLUE   | Someone else is speaking
![#fffacd](https://placehold.it/15/fffacd/000000?text=+) WHITE  | Nobody is speaking and nothing is muted

So, tere are also possible mixed colors

Color | Mixed | Meaning
 --- | --- | ---
![#00ffff](https://placehold.it/15/00ffff/000000?text=+) CYAN    | BLUE + GREEN | Someone else is speaking and you are speaking <br />
![#ff00ff](https://placehold.it/15/ff00ff/000000?text=+) MAGENTA | BLUE + RED   | Someone else is speaking and your mic is muted <br />
![#ffff00](https://placehold.it/15/ffff00/000000?text=+) YELLOW  | RED + GREEN  | Something went really wrong, you can't speak in TeamSpeak while your mic is muted
![#ffffff](https://placehold.it/15/ffffff/000000?text=+) RGB-White | RED + GREEN + BLUE | Same as YELLOW, but also someone is speaking
