#!/usr/bin/env python

import mc


def run(mc):
    print('run')

    mc.set('key', 'abc')
    mc.delete('key')


if __name__ == '__main__':
    mc.run_udp(run)
