from setuptools import setup

setup(name='pyactr',
      version='0.1.4',
      description='ACT-R in Python',
      url='https://github.com/jakdot/pyactr',
      author='jakdot',
      author_email='j.dotlacil@gmail.com',
      packages=['pyactr'],
      install_requires=['numpy', 'simpy', 'pyparsing'],
      classifiers=['Programming Language :: Python :: 3', 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)', 'Operating System :: OS Independent', 'Development Status :: 3 - Alpha', 'Topic :: Scientific/Engineering'],
      zip_safe=False)
