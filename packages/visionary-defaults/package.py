##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *

class VisionaryDefaults(Package):
    """Visionary Meta Package"""

    # This is a meta-package.  Instructions:
    # $ cd /tmp
    # $ spack install binutils+plugins+gold
    # $ spack find binutils+plugins+gold
    # -- linux-debian8-x86_64 / gcc@4.X.X -----------------------------
    # qxd4ne6 binutils@2.27
    # $ spack install gcc@6.2.0+binutils+gold ^/qxd4ne6
    # $ spack cd -i "gcc@6.2.0+binutils+gold"
    # $ spack compiler find --scope site .
    # $ spack install visionary-defaults %gcc@6.2.0

    homepage = None
    # some random tarball, to make `spack fetch --dependencies visionary-defaults` work
    url = 'https://github.com/electronicvisions/spack-visions/archive/master.tar.gz'
    version('0.1', git='https://github.com/electronicvisions/spack-visions.git')


    # This does not work, spack will try to reinstall gcc :(((((
    # variant('wheezy', default=False)

    # depends_on('gcc@6.2.0+binutils+gold %gcc@4.7', when="+wheezy")
    # depends_on('gcc@6.2.0+binutils+gold %gcc@4.9.2', when="~wheezy")

    depends_on('vim')
    depends_on('emacs ~X')
    depends_on('tmux')
    depends_on('ncdu')
    depends_on('units')
    depends_on('ranger')

    depends_on('mercurial')
    depends_on('git')
    depends_on('git-review')

    depends_on('cmake')
    depends_on('doxygen')
    depends_on('bear')
    depends_on('rtags@dev')

    depends_on('gdb')
    depends_on('llvm')
    depends_on('nodejs')

    depends_on('boost@1.55.0+graph+icu+mpi+python')
    depends_on('yaml-cpp+shared')
    depends_on('tensorflow')
    depends_on('log4cxx')
    # depends_on('libpsf')
    depends_on('googletest')
    depends_on('gflags')

    depends_on('py-bokeh')
    depends_on('py-pyqt')
    # depends_on('py-pygtk')
    depends_on('py-pyside')

    # depends_on('nest@2.2.2+python')
    depends_on('py-brian')
    depends_on('py-brian2')
    depends_on('py-elephant')
    #depends_on('py-spykeviewer')
    depends_on('py-pynn @0.7.5')

    depends_on('python @2.7:2.7.999')
    depends_on('py-cython')
    depends_on('py-pip')

    depends_on('py-ipython')
    # depends_on('py-ipdb')
    # depends_on('py-jupyter')
    # depends_on('py-notebook')

    depends_on('py-matplotlib+tk+ipython')
    depends_on('py-numpy')
    depends_on('py-pandas @0.19.0:')
    depends_on('py-pytables @3.3.0:')
    depends_on('py-scipy')
    depends_on('py-seaborn')
    depends_on('py-sympy')
    depends_on('py-statsmodels')
    depends_on('py-lmfit')

    depends_on('py-pyyaml')

    depends_on('py-autopep8')
    # depends_on('py-flake8')
    # depends_on('py-pylint')

    depends_on('py-sphinx')
    depends_on('py-doxypypy')
    depends_on('py-nose')
    depends_on('py-junit-xml')

    # depends_on('py-appdirs')
    # depends_on('py-current')
    # depends_on('py-funcsigs')
    # depends_on('py-lazy')

    depends_on('py-tabulate')
    depends_on('py-html')
    # depends_on('py-myhdl')
    depends_on('py-pillow')
    # depends_on('py-pyserial')
    # depends_on('py-shiboken')
    # depends_on('py-xlrd')

    def install(self, spec, prefix):
        mkdirp(prefix.etc)
        # store a copy of this package.
        install(__file__, join_path(prefix.etc, 'visionary-defaults.py'))

        # we could create some filesystem view here?
