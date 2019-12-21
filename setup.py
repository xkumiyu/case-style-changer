from setuptools import find_packages, setup

import case_style_changer

setup(
    name='case-style-changer',
    version=case_style_changer.__version__,
    description=case_style_changer.__doc__.strip(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author=case_style_changer.__author__,
    author_email='xkumiyu@gmail.com',
    url='https://github.com/xkumiyu/case-style-changer',
    license=case_style_changer.__licence__,
    entry_points={
        'console_scripts': [
            'csc = case_style_changer.cli:main',
            'case_style_changer = case_style_changer.cli:main'
        ]
    },
    packages=find_packages(exclude=('tests', 'docs')),
    setup_requires=['wheel'],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License'
    ],
)
