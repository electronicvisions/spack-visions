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
#     spack install py-saga-python
#
# You can edit this file again by typing:
#
#     spack edit py-saga-python
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PySagaPython(Package):
    """
        A Light-Weight Access Layer for Distributed Computing Infrastructure
        and Reference Implementation of the SAGA Python Language Bindings.
    """

    homepage = "http://radical-cybertools.github.io/saga-python/"
    url      = "https://github.com/radical-cybertools/saga-python/archive/v0.41.1.tar.gz"

    version('0.41.2', '2d32b8a49ae391ee59b5c4ae6476eb91')
    version('0.41.1', 'c2c51a6d0dd55c84c7b4af04a27056ae')
    version('0.41'  , 'e133c1334f65d9e45a16f6dfde110fc3')
    version('0.40.2', 'a2c56bd9da4ea9022598ce3924416849')
    version('0.40.1', 'd8bd063481aa6dfbb4314b927c58dc17')

    extends('python')

    depends_on("py-apache-libcloud")
    depends_on("py-radical-utils")

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
