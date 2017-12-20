# -*- coding: utf-8 -*-

from os import uname
from socket import gethostname
import subprocess
import locale
import re


def parse_output(pattern, default, args):
    try:
        out_str = subprocess.check_output(args)
        if isinstance(out_str, bytes):
            out_str = out_str.decode()
    except Exception:
        out_str = ''

    match = re.search(pattern, out_str)
    if match:
        result = match.group(1)
    else:
        result = default
    return result


def cpu_temp():
    t_str = parse_output(r'temp=(\S*)\'C', '0', ['vcgencmd', 'measure_temp'])
    return locale.atof(t_str)


def ip_address():
    return parse_output(r'(\S*)', '?', ['hostname', '-I'])


def host_name():
    return gethostname()


def os_name():
    return " ".join(uname())
