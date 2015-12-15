
from setuptools import setup

setup(name='pyfun',
      version='0.1.3',
      description='The pyfun joke in the world',
      url='http://github.com/storborg/pyfun',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['pyfun'],
      install_requires=[
          'markdown',
#          dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0'],
          ],
      zip_safe=False)
