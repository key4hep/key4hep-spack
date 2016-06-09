# HEP version of graphviz

from spack import *

class Graphviz(Package):
    """Graph Visualization Software"""
    homepage = "http://www.graphviz.org"
    url = "http://pkgs.fedoraproject.org/repo/pkgs/graphviz/graphviz-2.38.0.tar.gz/5b6a829b2ac94efcd5fa3c223ed6d3ae/graphviz-2.38.0.tar.gz"
    version('2.38.0', '5b6a829b2ac94efcd5fa3c223ed6d3ae')

    parallel = False

    depends_on("swig")
    depends_on("python")
    depends_on("ghostscript")

    def install(self, spec, prefix):
        configure("--prefix=%s" %prefix, '--disable-perl', '--disable-java', '--without-x','--enable-tcl=no')

        make()
        make("install")

