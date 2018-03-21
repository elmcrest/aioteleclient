from setuptools import setup

setup(
    name='async-telegram-client',
    version='0.0.1',
    url='https://github.com/elmcrest/async-telegram-client',
    license='MIT',
    description='An fast and heavily tested async telegram messenger client.',
    long_description="An fast and heavily tested async telegram messenger client",
    author='Marius Räsener',
    author_email='m.raesener@gmail.com',
    keywords='python telegram-client telegram-client-api asyncio async-telegram-client bot bot-framework telegram',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Communications :: Chat'
    ],
    install_requires=[
        'aiohttp'
    ],

)
