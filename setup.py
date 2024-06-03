from setuptools import setup, find_packages

setup(
    name='Crawler',
    version='1.0',
    author='Hesam Aghajani',
    author_email='hesamz3090@gmail.com',
    python_requires='>=3',
    install_requires=['requests', 'bs4'],
    packages=find_packages() + ['.'],
    include_package_data=True,
    description='A Python web crawler that follows links up to a specified depth',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hesamz3090/Crawler',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Security',
    ],
    keywords='crawler url',
    entry_points={
        'console_scripts': [
            'crawler = crawler:main',
        ],
    },
)
