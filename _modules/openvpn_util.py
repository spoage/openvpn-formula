#!/usr/bin/env python
import salt.utils.systemd


def uses_systemd():
    return salt.utils.systemd.booted(__context__)
