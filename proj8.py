
from gtts import gTTS
import os
# with open ('JayHind.txt', 'r') as f:
#     F = f.read()
mytext = "Shivaji Maharaj is one of the great national heroes of India. He created an independent and sovereign state in Maharashtra which was based on justice, welfare of the people and tolerance to all faiths. The aims, objectives and Rajnitee of the Maratha Swaraj under Chhatrapati Shivaji provided a new direction to contemporary politics of India. In course of time, his movement assumed, the form of an all-India struggle; a struggle which was to change the political map of India."
language = 'en'
myobjj = gTTS(text=mytext, lang=language, slow=False)
myobjj.save("History.mp3")
os.system(" History.mp3")
