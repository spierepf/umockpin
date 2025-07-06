import os
import sys

libpath = 'lib'
sys.path.insert(0, libpath)
if libpath not in os.listdir():
    os.mkdir(libpath)

if 'upatterns' not in os.listdir(libpath):
    import mip

    mip.install('github:spierepf/mip_packages/upatterns', target=libpath)
