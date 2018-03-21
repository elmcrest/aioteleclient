from setuptools import setup, find_packages

setup(
    name='aioteleclient',
    version='0.0.1',
    url='https://github.com/elmcrest/aioteleclient',
    license='MIT',
    description='An fast and heavily tested async telegram messenger client.',
    long_description="An fast and heavily tested async telegram messenger client",
    author='Marius Räsener',
    author_email='m.raesener@gmail.com',
    keywords='python telegram-client telegram-client-api asyncio async-telegram-client'
             'bot bot-framework telegram aioteleclient',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Communications :: Chat'
    ],
    packages=find_packages(),
    install_requires=[
        'aiohttp'
    ],
)
