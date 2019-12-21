from setuptools import find_packages, setup

import case_style_changer

setup(name='case-style-changer',
      version=case_style_changer.__version__,
      description=case_style_changer.__doc__.strip(),
      author=case_style_changer.__author__,
      author_email='xkumiyu@gmail.com',
      url='https://github.com/xkumiyu/case-changer',
      license=case_style_changer.__licence__,
      entry_points={
          'console_scripts': [
              'csc = case_style_changer.cli:main',
              'case_style_changer = case_style_changer.cli:main'
          ]
      },
      packages=find_packages(exclude=('tests', 'docs')),
      setup_requires=['wheel'])
