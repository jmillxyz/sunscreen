from setuptools import setup


setup(
    name="sunscreen",
    version="0.0.1",
    description="What's the UV forecast?",
    author="Jon Miller",
    py_modules=["sunscreen"],
    author_email="jondelmil@gmail.com",
    install_requires=["appdirs", "arrow", "colored", "click", "requests"],
    entry_points="""
        [console_scripts]
        sunscreen=sunscreen:main
    """,
)
