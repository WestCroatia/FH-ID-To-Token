import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.MAGENTA + """
  )`-.--. (\   .'(       /(   )\__.__   )\__.__ 
 ) .-._(  ) ) \  )     \  ) ) _  __ ( ) _  __ (
 \ `-._  (  '-' (      ) (  \( |(  )/ \( |(  )/
  ) ._(   ) .-.  )     \  )    ) \       ) \   
 (  \    (  .  ) \      ) \    \ (       \ (   
  )./     )/    )/       )/     )/        )/   

""" + Fore.LIGHTCYAN_EX)
print(banner)
userid = input(" [INPUT] Put the user ID of someone you want : ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n [LOGS] Here is the First Token Part of that user : {encodedStr}')
os.system('pause >nul')
