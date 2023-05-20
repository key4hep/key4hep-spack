from spack.pkg.k4.key4hep_stack import Key4hepPackage


class K4lcioreader(CMakePackage, Key4hepPackage):
    """LCIO reader based on PODIO and EDM4hep"""

    homepage = "https://github.com/key4hep/k4LCIOReader"
    url = "https://github.com/key4hep/k4LCIOReader/archive/v0.1.0.tar.gz"
    git = "https://github.com/key4hep/k4LCIOReader.git"

    maintainers = ["mirguest"]

    version("master", branch="master")
    version(
        "0.5",
        sha256="bdd97befeba4caa3ee2fcaea99a1f3b8cc2cb53dedf8e11f3c23a0b9f012b7f7",
        url="https://github.com/key4hep/k4LCIOReader/archive/refs/tags/v00.05.tar.gz",
    )
    version(
        "0.4.3",
        sha256="58e7cf2f47b71e0645ff90b24b6746561a6993377ef752901cd901a6cf8fe643",
        url="https://github.com/key4hep/k4LCIOReader/archive/refs/tags/v00.04.03.tar.gz",
    )
    version(
        "0.4.2",
        sha256="2bb8383d95b973676b87b4c8af00fdbd8bb84c2d4e45cacf98490d1946f909b0",
        url="https://github.com/key4hep/k4LCIOReader/archive/refs/tags/v00.04.02.tar.gz",
    )
    version(
        "0.4.1",
        sha256="bb93892bb38d4bb3176706f1fc55da8a21742a6fe7d5571914e9cfbc3478a847",
        url="https://github.com/key4hep/k4LCIOReader/archive/refs/tags/v00.04.01.tar.gz",
    )
    version(
        "0.4.0",
        sha256="aa1f2bcfabc5b5e3a09cab5408af1402b8a4ddf0927f2f69e62084f568306174",
    )

    patch(
        "https://github.com/key4hep/k4LCIOReader/commit/81f4f47ecc7ce904189986e08b949d477c0e4f08.patch",
        sha256="5c88414128ccc9af6b53669f79ac5e4a61c4841d7de5b00a56400c9e92b7d37d",
        when="@0.4.1",
    )

    depends_on("lcio")
    depends_on("podio@0.12:")
    depends_on("edm4hep")
    depends_on("edm4hep@0.5:", when="@0.4.2:")
    depends_on("edm4hep@0.8:", when="@0.5:")
    depends_on("k4fwcore@0.3.0:", when="@0.4:")
    depends_on("root")

    def cmake_args(self):
        args = []
        args.append(
            "-DCMAKE_CXX_STANDARD=%s" % self.spec["root"].variants["cxxstd"].value
        )
        return args
