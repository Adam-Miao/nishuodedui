#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import argparse
import api

full = ['game', 'author', 'kind', 'world', 'selector', 'whom', 'award', 'player', 'power', 'colleague', 'friend',
        'enemy', 'lost', 'truth']
arg = {}
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--command", help="Use only command line.", action="store_true")
parser.add_argument("-t", "--template", help="Update on an existing template.")
parser.add_argument("-g", "--game")
parser.add_argument("-a", "--author")
parser.add_argument("-k", "--kind")
parser.add_argument("-w", "--world")
parser.add_argument("-s", "--selector")
parser.add_argument("-W", "--whom")
parser.add_argument("-A", "--award")
parser.add_argument("-p", "--player")
parser.add_argument("-P", "--power")
parser.add_argument("-C", "--colleague")
parser.add_argument("-f", "--friend")
parser.add_argument("-e", "--enemy")
parser.add_argument("-l", "--lost")
parser.add_argument("-T", "--truth")
args = parser.parse_args()

if args.template:
    count = json.load(open('templates/count.json'))
    try:
        t = json.load(open('templates/' + count[args.template]['Filename']))
    except KeyError:
        print(f'E: Unable to find template `{args.template}`')
        exit(1)
    except FileNotFoundError:
        print(f'E: File `{count[args.template]["Filename"]}` not found, maybe it has been deleted?')
        exit(1)
else:
    if not args.command:
        for x in full:
            if eval('args.' + x):
                arg[x] = eval('args.' + x)
            else:
                tmp = input(x.title() + '> ')
                if tmp:
                    arg[x] = tmp
for x in full:
    if eval('args.' + x):
        arg[x] = eval('args.' + x)

if args.template:
    t.update(arg)
    arg = t

print(api.rightGen(arg))
