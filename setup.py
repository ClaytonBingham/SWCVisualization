from distutils.core import setup

DESCRIPTION = "Provides visualization tools to manipulate SWC formatted neural morphologies."
LONG_DESCRIPTION = "Provides tools for visualization of SWC formatted neural morphologies."
NAME = "swcVisualization"
AUTHOR = "Clayton Bingham"
AUTHOR_EMAIL = "clayton.bingham@gmail.com"
MAINTAINER = "Clayton Bingham"
MAINTAINER_EMAIL = "clayton.bingham@gmail.com"
LICENSE = 'BSD'
REQUIREMENTS = [
		'numpy',
		'pandas',
		'pickle',
		'copy',
		'scipy',
		'mayavi',
		]
VERSION = '0.1'

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      download_url=DOWNLOAD_URL,
      license=LICENSE,
      packages=['swcVisualization'],
      install_requires=REQUIREMENTS,
      package_data={}
     )
