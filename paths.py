import os


def template_dir():
    return os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'templates')
