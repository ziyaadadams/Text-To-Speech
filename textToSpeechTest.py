from gtts import gTTS

import os

myText = 'May everyone named michael please stand...  That concludes the mike check'

language = 'en'

myobj = gTTS(text = myText, lang=language, slow=False)

myobj.save("welcome.mp3")

os.system("mpg321 welcome.mp3")
