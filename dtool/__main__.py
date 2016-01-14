#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Initially Generated By:
    python -m utool --tf setup_repo --repo=dtool --codedir=~/code --modname=dtool
"""
from __future__ import absolute_import, division, print_function, unicode_literals


def dtool_main():
    ignore_prefix = []
    ignore_suffix = []
    import utool as ut
    # allows for --tf
    ut.main_function_tester('dtool', ignore_prefix, ignore_suffix)

if __name__ == '__main__':
    """
    Usage:
        python -m dtool --tf <funcname>
    """
    print('Running dtool main')
    dtool_main()