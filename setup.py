from setuptools import setup

setup(name="azlyrics",
      version="0.0.1",
      url="https://github.com/dragonGR/azlyrics",
      author="Marcos Ferreira",
      author_email="merkkp@gmail.com",
      description="'API' and CLI program to fetch lyrics from azlyrics",
      install_requires=["beautifulsoup4"],
      packages=["azlyrics"],
      license="GPL",
      entry_points = {
          'console_scripts': [
              'azlyrics = azlyrics:run'
          ]
      })
