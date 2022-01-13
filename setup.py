from distutils.core import setup
setup(
    name="prettylog",
    packages=["prettylog"],
    version="0.1",
    license="MIT",
    description="Pretty looking logging library that's also extremely functional.",
    author="Philippe Mathew",
    author_email="philmattdev@gmail.com",
    url="",
    download_url="",
    keywords=["logger", "logging"],
    install_requires=[
        "termcolor"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ]
)
