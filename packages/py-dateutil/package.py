from spack import *

class PyDateutil(Package):
    """
    The dateutil module provides powerful extensions to the 
    standard datetime module, available in Python.
    """
    homepage = "https://dateutil.readthedocs.io/en/stable/"
    url      = "https://pypi.python.org/packages/3e/f5/aad82824b369332a676a90a8c0d1e608b17e740bbb6aeeebca726f17b902/python-dateutil-2.5.3.tar.gz"

    version('2.5.3', '05ffc6d2cc85a7fd93bb245807f715ef')

    extends("python")
    depends_on("py-setuptools")
    depends_on("py-six")

    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix=%s' % prefix)

