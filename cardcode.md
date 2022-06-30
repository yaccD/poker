# card code scheme

     D: diamonds (♦): 方块
     C: clubs (♣): 草花
     H: hearts (♥): 红桃
     S: spades (♠): 黑桃
     J: joker: JOKER,  
     
### Graphic show
for show in txt enviroment for easy understand.
     ♦ A|2..10|J|Q|K
     ♣ A|2..10|J|Q|K
     ♥ A|2..10|J|Q|K
     ♠ A|2..10|J|Q|K
     🥳   JK|jk
     
### poker representive code
for the easy input the card
     D 1|2..10|11|12|13 as A|2..10|J|Q|K
     C 1|2..10|11|12|13 as A|2..10|J|Q|K
     H 1|2..10|11|12|13 as A|2..10|J|Q|K
     S 1|2..10|11|12|13 as A|2..10|J|Q|K
     J 3|4              # Junier Joker: 3,Senior Joker: 4

### Nick name of the type of the master card
     JK: King
     jk: Queen
     master flower and number: Regent
     other master number: Duke
     master flower 2: Marquess
     other flower 2: Earl


### poker DL code
xxxx 4 digital as a card
first digit x:
     0:方块 diamonds (♦)
     1:草花 clubs (♣)
     2:红桃 hearts (♥)
     3:黑桃 spades (♠)
     4:方块 diamonds (♦)
     5:草花 clubs (♣)
     6:红桃 hearts (♥)
     7:黑桃 spades (♠)
     8:2  permanent master 
     9:Master card and Joker, Senior Joker and Junior Joker  
second&third digit xx:
     00: null
     01: null
     02: null
     03: 3
     04: 4
     ........
     10: 10
     11: J
     12: Q
     13: K     when first digit is 9: Jonier Joker
     14: A     when first digit is 9: Senior Joker
last digit x
      0:ordinary card no use. but for permanent master card, means follow:
      0:方块 diamonds (♦)
      1:草花 clubs (♣)
      2:红桃 hearts (♥)
      3:黑桃 spades (♠)
     10:方块 diamonds (♦)
     11:草花 clubs (♣)
     12:红桃 hearts (♥)
     13:黑桃 spades (♠)
   




