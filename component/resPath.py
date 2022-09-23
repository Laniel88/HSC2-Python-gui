import os

# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     # modify path for PyInstaller
#     for folder in ['fonts', 'img', 'layouts']:
#         if folder in relative_path:
#             relative_path = relative_path[len(folder) + 1:]
#         else:
#             print('Path ERROR')
#     # make path
#     base_path = getattr(sys, '_MEIPASS', os.path.dirname(
#         os.path.abspath(__file__)))
#     return os.path.join(base_path, relative_path)


def resource_path(relative_path):
    """ Used for developing"""
    return os.path.dirname(os.path.abspath(os.path.dirname(__file__))) + '/res/' + relative_path
