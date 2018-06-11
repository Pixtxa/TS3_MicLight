# TS3_StripeControl
Use a cheap MagigHome WiFi-RGBW-Stripe-Controller and the pyTSon plugin for TeamSpeak3 to monitor the Audio-Status of your microphone or of your current channel. <br />
Based on https://github.com/pathmann/pyTSon_repository/blob/master/eventlog.py

## TS3_MicLight
You can define colors to show the state of your microphone (sending/muted/idle)

## TS3_StatusLight
Changed Version of TS3_MicLight, uses the LED-Stripe-Channels for the events: <br />
RED    = mic and/or speakers are muted <br />
GREEN  = you are speaking <br />
BLUE   = someone else is speaking <br />
WHITE  = nobody is speaking, nothing is muted <br />

So, tere are also possible mixed Colors: <br />
CYAN    = BLUE + GREEN = someone else is speaking and you are speaking <br />
MAGENTA = BLUE + RED   = someone else is speaking and your mic is muted <br />
YELLOW  = RED + GREEN  = Something went really wrong, you can't speak in TeamsPeak while your Mic is muted
