#!/usr/bin/env python

from distutils.core import setup
from distutils.command.install_data import install_data
import glob


class simple_install_data(install_data):
    def finalize_options(self):
        self.set_undefined_options('install',
                                   ('install_lib', 'install_dir'),
                                   ('root', 'root'),
                                   ('force', 'force') )


pilfontsList = glob.glob('src/piddle/pilfonts/*')

setup(name='piddle',
      version= '1.0.15',
      description = "Piddle:Plug In Drawing, Does Little Else. A cross-platform drawing library",
      url = "http://piddle.sourceforge.net",
      package_dir = {'': 'src'}, # root package is in src
      cmdclass = {'install_data' : simple_install_data},
      data_files = [ ('piddle/pilfonts', pilfontsList),
                     ('piddle', ['src/piddle/python.gif']),
                     ('', ['src/piddle.pth']) ],
      #packages = ['piddle'] )
      packages = ['piddle', 'piddle.piddleGTK', 'piddle.piddleSVG', 'piddle.piddleTK2'] )
