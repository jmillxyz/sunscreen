from setuptools import setup


setup(
    name="sunscreen",
    version="0.0.1",
    description="weather report for the sun",
    author="Jon Miller",
    py_modules=["sunscreen"],
    author_email="jondelmil@gmail.com",
    install_requires=["arrow", "colorama", "click", "requests"],
    entry_points="""
        [console_scripts]
        sunscreen=sunscreen:main
    """,
)
