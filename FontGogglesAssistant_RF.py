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

from random import choice
from ulwords import ULCWORDS
from vanilla import FloatingWindow, Window, EditText, TextBox
import codecs
from mojo.events import addObserver, removeObserver
from mojo.roboFont import CurrentGlyph, CurrentFont

# Initial template string. The /? gets replaced by the unicode of the current glyph.
SAMPLE = 'A/?AH/?HO/?OV/?Va/?ai/?io/?ov/?v'
# Name of the file that will be synce in the directory of the current font.
SAMPLE_FILE_NAME = 'FontGoggles-RF-Sync.txt'

class FontGogglesAssistant:
    def __init__(self):
        w, h = 300, 60
        # Create the window. Position is from top-left of the screen. 
        self.w = FloatingWindow((50, 50, w, h), 'FontGoggles Assistant')
        # Text box to enter an alternative sample text. /? is replaced by the current glyph unicode
        self.w.sampleTextLabel = TextBox((10, 6, -10, 24), 'Sample text in FontGoggles (replace /?)', sizeStyle="small")
        self.w.sampleText = EditText((10, 24, -10, 24), SAMPLE, callback=self.sampleTextCallback)
        # Get a call from RoboFont if the current selection changed.
        addObserver(self, 'currentGlyphChangedCallback', "currentGlyphChanged")
        # Add binding to remove the obeserver if the window is closed.
        self.w.bind('close', self.windowCloseCallback)
        # Open the window with the sample text pattern
        self.w.open()

    def windowCloseCallback(self, sender):
        """Window is closing, remove the observer"""
        removeObserver(self, "currentGlyphChanged")
        
    def sampleTextCallback(self, sender):
        """The sample was changed, update the file"""
        self.updateGogglesFile()
        
    def currentGlyphChangedCallback(self, notification):
        """Glyph selection changed, update the file"""
        self.updateGogglesFile()
        
    def updateGogglesFile(self):
        """Main function to update the FontGoggles sample file. """
        # Get the current selected glyph. This can be from the EditorWindow or the FontWindow
        glyph = CurrentGlyph()
        if glyph.unicode: # FontGoggles can only show characters with unicode. Stylistic sets will show alternatives.
            char = chr(glyph.unicode) # Get the character of this unicode
            font = glyph.font # Get the font to know where to write the file
            # Get the path of the current font and calculate the output file path local to it.
            path = '/'.join(font.path.split('/')[:-1]) + '/' + SAMPLE_FILE_NAME
            sample = choice(ULCWORDS) + ' ' + self.w.sampleText.get().replace('/?', char) # Get the sample and replace pattern /?
            f = codecs.open(path, 'w', encoding='utf-8') # Open file, for unicode/UTF-8
            f.write(sample) 
            f.close()
 
FontGogglesAssistant()
