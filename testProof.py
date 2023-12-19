
from jillskerning import *
W, H = 595, 842
M = 30 # Margins
FSIZE = 18
LEADING = 1.4
FONT_NAME = 'Upgrade-UltraBlack'
txt = JILLS_KERNING

fs = FormattedString(txt, font=FONT_NAME, fontSize=FSIZE, lineHeight=FSIZE * LEADING)

while fs:
    newPage(W, H)
    fs = textBox(fs, (M, M, W-2*M, H-2*M))
    
