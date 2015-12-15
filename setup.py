from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='pyfun',
      version='0.1.4',
      description='The pyfun joke in the world',
      long_description='Really, the funniest around.',
      classifiers=[
                        'Development Status :: 3 - Alpha',
                        'License :: OSI Approved :: MIT License',
                        'Programming Language :: Python :: 2.7',
                        'Topic :: Text Processing :: Linguistic',
                  ],
      test_suite='nose.collector',
      tests_require=['nose'],
      keywords='funniest joke comedy flying circus',
      url='https://github.com/zhaohangbo/pyfun.git',
      author='zhaohangbo',
      author_email='zhaohangbo@example.com',
      license='MIT',
      packages=['pyfun'],
      install_requires=[
          'markdown',
#          dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0'],
          ],
      include_package_data=True,
      zip_safe=False)
