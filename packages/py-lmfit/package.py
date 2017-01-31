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
#     spack install py-lmfit
#
# You can edit this file again by typing:
#
#     spack edit py-lmfit
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PyLmfit(Package):
    """
       Non-Linear Least Squares Minimization, with flexible Parameter settings,
       based on scipy.optimize.leastsq, and with many additional classes and 
       methods for curve fitting.
    """

    homepage = "http://lmfit.github.io/lmfit-py/"
    url      = "https://github.com/lmfit/lmfit-py/archive/0.9.5.tar.gz"

    version('0.9.5'   , 'b9d26257f67d0b569e12473a210e4882')
    version('0.9.4rc1', 'df97987bbb5081f84556cb063d30d1cc')
    version('0.9.4'   , '0dd8f6bc2b6ac9fb0672cd08f2ad1c34')
    version('0.9.3rc2', '82c97e969f8737b0d985a10a08af1cb4')
    version('0.9.3rc1', '929f6b3b5f52eab4b4b0801e5d57e58b')

    extends('python')

    depends_on('py-numpy', type='build')
    depends_on('py-scipy', type='build')

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
