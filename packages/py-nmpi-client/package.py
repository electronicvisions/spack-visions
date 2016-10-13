from spack import *

class PyNmpiClient(Package):
    """Neuromorphic Platform Interface"""

    homepage = "https://github.com/HumanBrainProject"
    url      = "https://github.com/HumanBrainProject/hbp-neuromorphic-client/archive/0.2.0.tar.gz"

    version('0.4.2', '189b4fbe017d6500f3480d0031745976')
    version('0.4.1', '08645ff62d050e99f9bb57bb7d6b9138')
    version('0.4.0', '595b40a8d7f2ec7b68e0198cf764ea72')
    version('0.3.0', '1a2dc04ea0e00f2b56a862720705dd6c')
    version('0.2.0', '6864997bb0fea58dc3a41a466b32aaf4')

    depends_on("py-requests@2.3.0:")
    depends_on("py-apache-libcloud@0.14.1:")
    depends_on("py-colorama@0.3.1:")
    depends_on("py-radical-utils@0.7.4:")
    depends_on("py-saga-python@0.15.0:")
    depends_on("py-sh@1.09:")

    extends("python")

    def install(self, spec, prefix):
        setup_py("install", "--prefix={0}".format(prefix))
