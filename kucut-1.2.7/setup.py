from distutils.core import setup
setup(name='kucut',
      version='1.2.7',
      scripts=['scripts/kucut'],
      description='Word segmentation tool from Kasetsart University',
      author='Sutee Sudprasert',
      author_email='sutee.s@gmail.com',
      url='http://naist.cpe.ku.ac.th/',
      packages=['kucut', 'kucut/AIMA'],
      package_data={'kucut': ['train.skip.cut.db', 'dict/*.txt']})
