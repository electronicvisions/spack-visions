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

class PyDeepLoop(Package):
    """Meta Package"""

    homepage = None
    url = "https://localhost/123"
    version('0.1')

    depends_on("py-elephant")
    depends_on("py-ipython")
    depends_on("py-matplotlib+tk+ipython")
    depends_on("py-numpy")
    depends_on("py-pandas @0.19.0:")
    depends_on("py-pil")
    depends_on("py-pynn @0.7.5")
    depends_on("py-pytables @3.3.0:")
    depends_on("py-scipy")
    depends_on("py-cython")
    # depends_on("py-notebook")
    depends_on("python")
    depends_on("tensorflow")

    def install(self, spec, prefix):
        pass
