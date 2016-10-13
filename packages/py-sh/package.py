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
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-sh
#
# You can edit this file again by typing:
#
#     spack edit py-sh
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PySh(Package):
    """Python process launching"""

    homepage = "http://amoffat.github.com/sh"
    url      = "https://github.com/amoffat/sh/archive/1.11.tar.gz"

    version('1.11', 'ac0ed0d704770bfcb1d348cd07db50d4')
    version('1.10', 'f27fc4ad595d21f9c9e687bcad25f6cc')
    version('1.08', 'a89e4600d9500210b78dbcefad63b443')
    version('1.07', 'f681bace999d5c0dc5b8d9e4d29fb13e')
    version('1.06', '76a28cfd021b39f20506fc54de566c70')

    extends('python')

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
