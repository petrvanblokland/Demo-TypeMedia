#
#    RoboFont version of the FontGoggles Assistant.
#    Open FontGoggles and drag the fonts on the window that you want to show samples of.
#    Run this script in RoboFont, notice that a small window pops at the topleft of your screen
#    that holds the sample string. 
#    Open a font and select a glyph.
#    Select the sample (top-right button) in the directory of the current font 
#    named "FontGoggles-RF-Sync.txt"
#    Changing the current selection reflects in the showing of another sample in FontGoggles.
#    Note that saving the font in RoboFont will immediately show the changes in FontGoggles as well.
#

import drawBot
from random import choice
from ulcwords import ULCWORDS
from jillskerning import *
from vanilla import FloatingWindow, Window, Button
import codecs
from mojo.events import addObserver, removeObserver
from mojo.roboFont import CurrentGlyph, CurrentFont

# Name of the file that will be synce in the directory of the current font.
PROOF_FILE_PATH = '/'.join(__file__.split('/')[:-1]) + '/Proof.pdf'

class ProofAssistant:
    def __init__(self):
        w, h = 300, 100
        # Create the window. Position is from top-left of the screen. 
        self.w = FloatingWindow((50, 50, w, h), 'FontGoggles Assistant')
        self.w.makeProof = Button((10, 10, -10, h-20), 'Make Proof', self.makeProofCallback)
        # Open the window with the sample text pattern
        self.w.open()
        
    def makeProofCallback(self, sender):
        """Main function to update the FontGoggles sample file. 
    
        """
        f = CurrentFont()
        
        # Running external
        # from fontparts import RFont
        # f = RFont(path)
        #
        if f is None:
            print('Open a font first')
            return 
            
        f.generate("otfcff")
        
        W, H = 595, 842
        M = 30 # Margins
        FSIZE = 18
        LEADING = 1.4
        fontPath = f.path.replace('.ufo', '.otf')
        pdfPath = f.path.replace('.ufo', '.pdf')
        print(fontPath)
        txt = JILLS_KERNING

        fs = drawBot.FormattedString(txt, font=fontPath, fontSize=FSIZE, lineHeight=FSIZE * LEADING)

        while fs:
            print('newPage')
            drawBot.newPage(W, H)
            fs = drawBot.textBox(fs, (M, M, W-2*M, H-2*M))
    
        drawBot.saveImage(pdfPath)
        print('Saved PDF', pdfPath)
        
ProofAssistant()
