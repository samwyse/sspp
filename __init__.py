from glob import glob
from os.path import dirname, join, split, splitext

basedir = dirname(__file__)

__all__ = []
for name in glob(join(basedir, '*.py')):
    module = splitext(split(name)[-1])[0]
    if not module.startswith('_') and module.isidentifier():
        __import__(__name__+'.'+module)
        __all__.append(module)
__all__.sort()
