import pyautogui as gui,time,keyboard as key
while True:
  print("Press Space To Continue... Sup3rSp4m By IG:@ThisIzUnD3ad")
  key.wait("space")
  x = input("Please Enter The Text You Want To Spam:")
  print('''
                    :::!~!!!!!:.
                    .xUHWH!! !!?M88WHX:.
                  .X*#M@$!!  !X!M$$$$$$WWx:.
                :!!!!!!?H! :!$!$$$$$$$$$$8X:
                !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
              :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
              ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
                !:~~~ .:!M"T#$$$$WX??#MRRMMM!
                ~?WuxiW*`   `"#$$$$8!!!!??!!!
              :X- M$$$$       `"T#$T~!8$WUXU~
              :%`  ~#$$$m:        ~!~ ?$$$$$$
            :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
  .....   -~~:<` !    ~?T#$$@@W@*?$$      /`
  W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
  #"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
  :::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
  .~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
  Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
  $R@i.~~ !     :   ~$$$$$B$$en:``
  ?MXT@Wx.~    :     ~"##*$$$$M~
      
    Select Where To Spam And Start By Pressing "F8".
    Options:
    F8 = Start.
    F7 = Stop. 

  THIS IZ UND3AD 

  Spammer Version: 1.0.0    (Baby)
  ''')
  key.wait("f8")
  print("Starting...")

  while True:
    print("Spamming...")
    gui.typewrite(x)
    gui.press("enter")
    if key.is_pressed("f7"):
        print("Stopping...")  
        break