# -*- coding: utf-8 -*-

import misc

def main(bot, args):
    """show <url>\nShow img by url."""

    if len(args) == 1:
        return args[0], misc.getImgXML(args[0], args[0])

def info(bot):
    return ((u"show", u"ырщц"), 10, main)
