
from translate import Translator


translator = Translator(to_lang='ja')

try:
  with open(r'C:\Users\osk-t-00704y\Desktop\sample.txt', mode = 'r',encoding="utf-8") as my_file:
    text = my_file.read()
    tarnslation = translator.translate(text)
    with open(r'.\sample-ja.txt',mode = 'w') as ja_samplefile:
      ja_samplefile.write(tarnslation)
      print("Completed!")
    
except FileNotFoundError as error:
  print('please check file path')