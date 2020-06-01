
import sys
from utils import strings

def readOption(txt, numOptions):
   
    while True:
        try:
            option = int(input(txt).strip())
        except KeyboardInterrupt:
            sys.exit('\n\n' + strings.colors('Goodbye, see you!', 1) + '\n')
        except:
            print(strings.colors('[ERROR] Enter a valid option!', 1))
        else:
            if 0 < option < numOptions + 1:
                return option
            print(strings.colors('[ERROR] Enter a valid option!', 1))

def readFloat(txt='Enter a real (float) number: '):
    while True:
        try:
            n = float(input(txt).strip())
        except KeyboardInterrupt:
            sys.exit('\n\n' + strings.colors('Saindo, tchau!', 1) + '\n')
        except:
            print(strings.colors('[ERROR] Enter a valid option!', 1))
        else:
            return n


def colors(txt, color=None, background=None, font=0):
    
    clr_prefix = '\033[' + str(font)
    if color is not None:
        clr_prefix += ';3' + str(color)
    if background is not None:
        clr_prefix += ';4' + str(background)
    clr_prefix += 'm'
    
    return clr_prefix + str(txt) + '\033[m'
