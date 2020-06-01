

def colors(txt, color=None, background=None, font=0):
    
    clr_prefix = '\033[' + str(font)
    if color is not None:
        clr_prefix += ';3' + str(color)
    if background is not None:
        clr_prefix += ';4' + str(background)
    clr_prefix += 'm'
    
    return clr_prefix + str(txt) + '\033[m'


def greeting():
    print('\n' + '-='*30 + '\n' + '-='*30)
    print(f'{"GEDI Utils - Find, Download and Pre-process!":^60}')
    print('-='*30 + '\n' + '-='*30 + '\n')

