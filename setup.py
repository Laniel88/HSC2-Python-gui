# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
#     return os.path.join(base_path, relative_path)

def resource_path(relative_path):
    """ Used for developing"""
    return 'res/'+relative_path #os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+






