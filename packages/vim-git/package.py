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


class VimGit(Package):
    """Vim is a highly configurable text editor built to enable efficient text
    editing. It is an improved version of the vi editor distributed with most
    UNIX systems.  Vim is often called a "programmer's editor," and so useful
    for programming that many consider it an entire IDE. It's not just for
    programmers, though. Vim is perfect for all kinds of text editing, from
    composing email to editing configuration files.
    """

    homepage = "http://www.vim.org"
    url      = "ftp://ftp.vim.org/pub/vim/unix/vim-7.4.tar.bz2"
    list_url = "http://ftp.vim.org/pub/vim/unix/"

    version("7.4.2199", git="https://github.com/vim/vim", tag="v7.4.2199")

    feature_sets = ('huge', 'big', 'normal', 'small', 'tiny')
    for fs in feature_sets:
        variant(fs, default=False, description="Use '%s' feature set" % fs)

    variant('python', default=False, description="build with Python")
    depends_on('python', when='+python')

    variant('ruby', default=False, description="build with Ruby")
    depends_on('ruby', when='+ruby')

    variant('cscope', default=False, description="build with cscope support")
    depends_on('cscope', when='+cscope', type='run')

    variant('gui', default=False, description="build with gui (gvim)")
    # virtual dependency?

    def install(self, spec, prefix):
        feature_set = None
        for fs in self.feature_sets:
            if "+" + fs in spec:
                if feature_set is not None:
                    tty.error(
                        "Only one feature set allowed, specified %s and %s"
                        % (feature_set, fs))
                feature_set = fs
        if '+gui' in spec:
            if feature_set is not None:
                if feature_set is not 'huge':
                    tty.error(
                        "+gui variant requires 'huge' feature set, "
                        "%s was specified" % feature_set)
            feature_set = 'huge'
        if feature_set is None:
            feature_set = 'normal'

        configure_args = []
        configure_args.append("--with-features=" + feature_set)

        if '+python' in spec:
            configure_args.append("--enable-pythoninterp=yes")
        else:
            configure_args.append("--enable-pythoninterp=dynamic")

        if '+ruby' in spec:
            configure_args.append("--enable-rubyinterp=yes")
        else:
            configure_args.append("--enable-rubyinterp=dynamic")

        if '+gui' in spec:
            configure_args.append("--enable-gui=auto")

        if '+cscope' in spec:
            configure_args.append("--enable-cscope")

        configure("--prefix=%s" % prefix, *configure_args)

        make()
        make("install")
