#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def rightGen(arg):
    # Generate: You're right, but...
    default = {
        'game': '',
        'author': '',
        'kind': '',
        'world': '',
        'selector': '',
        'whom': '',
        'award': '',
        'power': '',
        'player': '',
        'colleague': '',
        'friend': '',
        'enemy': '',
        'lost': '',
        'truth': ''
    }
    default.update(arg)
    s = (f'你说的对，但是《{default["game"]}》是由{default["author"]}自主研发的一款{default["kind"]}游戏。'
         f'故事发生在一个被称作「{default["world"]}」的世界，在这里被{default["selector"]}选中的{default["whom"]}'
         f'将被授予「{default["award"]}」，引导{default["power"]}之力。你将扮演一位名为「{default["player"]}」的神秘角色，'
         f'在自由的旅行中邂逅{default["friend"]}，和{default["colleague"]}一起击败{default["enemy"]}，'
         f'寻找失散的{default["lost"]}， 同时，逐步发掘「{default["truth"]}」的真相。')

    return s
