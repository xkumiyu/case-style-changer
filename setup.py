from setuptools import find_packages, setup

setup(name='case-style-changer',
      description='Case Style Changer - a CLI.',
      author='xkumiyu',
      author_email='xkumiyu@gmail.com',
      url='https://github.com/xkumiyu/case-changer',
      entry_points={'console_scripts': ['csc = case_style_changer.cli:main']},
      packages=find_packages(exclude=('tests', 'docs')))
