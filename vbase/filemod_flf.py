# keep track if ssl import succeeded
try:
    from pyfiglet import Figlet
    LOADPIFIGLET = True
except:
    LOADPIFIGLET = False
    pass

def load_desc(filename, filepath):

    if LOADPIFIGLET == False:
        return ['Could not load pyFiglet']

    try:
        f = Figlet(font=filepath+filename[0:-4],width=40,justify="left") 
        #      #text = f.renderText(items[selbar]['name'][0:-4]).encode('ascii') #must encode to ascii to avoid unicode errors
        if filename == "tmplr":
            text = f.renderText('0123456789') #must encode to ascii to avoid unicode errors
        else:
            text = f.renderText(filename[0:-4]) #must encode to ascii to avoid unicode errors

    except Exception:

        return 'Could not load font'

    return text.split('\n')