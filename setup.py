import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'pyramid',
    'pyramid_zodbconn',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'ZODB3',
    'pyOpenSSL',
    ]

setup(name='PyCraft',
      version='0.0',
      description='PyCraft',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Gaming :: Minecraft",
        ],
      author='Mark McGuire',
      author_email='mark.b.mcg@gmail.com',
      url='',
      keywords='web pylons pyramid minecraft',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires = requires,
      tests_require= requires,
      test_suite="pycraft",
      entry_points = """\
      [paste.app_factory]
      main = pycraft:main
      """,
      paster_plugins=['pyramid'],
      )

