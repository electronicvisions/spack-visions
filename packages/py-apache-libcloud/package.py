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
#     spack install py-apache-libcloud
#
# You can edit this file again by typing:
#
#     spack edit py-apache-libcloud
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PyApacheLibcloud(Package):
    """
        Python library for interacting with many of the popular cloud service
        providers using a unified API. 
    """

    homepage = "https://libcloud.apache.org/"
    url      = "http://apache.mirror.digionline.de/libcloud/apache-libcloud-1.2.1.tar.gz"

    version('1.2.1' , '912e6fb1f2d13f7d3b58ee982b9f9d1f')
    version('1.2.0' , 'b2fd88f6c188d61f02bb64887bfc2f1e')
    version('1.1.0' , '19188d59547c8bd834075ace0fafab41')
    version('1.0.0' , '7fd1c9ee6b73a2a8cf0b9eaf199cb871')
    version('0.20.1', 'd12ef4f96878a940321c73f4e0821237')

    extends('python')

    # TODO: Needs at least python 3.2 if using python 3, otherwise
    # another requirement backports.ssl_match_hostname 
    depends_on("python@2.7.9:")

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))

