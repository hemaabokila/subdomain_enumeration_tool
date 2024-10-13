from setuptools import setup, find_packages

setup(
    name="subdomain_enumeration_tool",
    version="1.0.0",
    author="Ibrahem abo kila",
    author_email="ibrahemabokila@gmail.com",
    description="subdomain enumrition tool.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hemaabokila/subdomain_enumeration_tool",
    packages=find_packages(),
    package_data={
        '': ['wordlists/wordlist.txt'], 
        },
    install_requires=[
	    'dnspython',
        'colorama',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'sub=subdomain.main:main', 
        ],
    },
)

