#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string
import random
import argparse


def parse_dice_set(dice_set):
    # check dice validation
    pos_char = string.find(dice_set, 'd')
    pos_plus = string.find(dice_set, '+')

    num_dice = 0
    num_face = 0
    offset = 0

    if pos_char != -1:
        num_dice = int(dice_set[0:pos_char])
        if pos_plus != -1:
            num_face = int(dice_set[pos_char+1:pos_plus])
            offset = int(dice_set[pos_plus:])
        else:
            num_face = int(dice_set[pos_char+1:])
    else:
        print "[ERROR] '%s' is not a valid dice set."
        sys.exit()

    return num_dice, num_face, offset


def update_frequency_table(d, l):
    r = {}
    for i in l:
        new_keys = [x + i for x in d.keys()]
        new_dict = dict(zip(new_keys, d.values()))
        for k in new_dict:
            r[k] = r[k] + new_dict[k] if k in r else new_dict[k]
                
    return r


def roll_dice(dice_set):
    num_dice, num_face, offset = parse_dice_set(dice_set)
    rolllist = []

    for i in range(num_dice):
        rolllist.append(random.randint(1, num_face))

    print "rolling dice[%s]..." % dice_set
    print "You've got %s from %s" % (sum(rolllist) + offset, rolllist),
    print "(+%d)" % (offset) if offset != 0 else ""


def calc_stats(dice_set):
    num_dice, num_face, offset = parse_dice_set(dice_set)
    amin = 1 * num_dice + offset
    amax = num_face * num_dice + offset
    avg = (amin + amax) / 2.0
    combination = num_face ** num_dice

    ftable = {} # frequency table
    for i in range(num_dice):
        if i == 0:
            ftable = dict(zip(range(1, num_face+1), [1] * num_face))
        else:
            ftable = update_frequency_table(ftable, range(1, num_face+1))

    # probability list
    plist = [100.0 * x / combination for x in ftable.values()]

    # generate accumulated list
    incr_list = []
    decr_list = []
    for i in range(len(plist)):
        if i == 0:
            incr_list.append(0)
            decr_list.append(100 - plist[0])
        else:
            incr_list.append(incr_list[i-1] + plist[i-1])
            decr_list.append(decr_list[i-1] - plist[i])

    # standard deviation
    squre_sum = sum(map(lambda x,y:(x+offset) ** 2 * y, ftable.keys(),
        ftable.values()))
    sd = ((1.0 * squre_sum / combination) - (avg ** 2)) ** 0.5

    print
    print "dice set: [%s]" % dice_set
    print "range [%d...%d]    avg: %.1f    stdev: %.2f" % (amin, amax, avg, sd)
    print "%d different value in %d combinations" % (amax-amin-1, combination)
    print
    print "----val:combo (     p%, [    '<' |     '>'])------"
    for i in range(len(ftable)):
        print "    % 3d:% 5d (%6.3f%%, [%6.3f%% | %6.3f%%])" % (
                ftable.keys()[i]+offset, ftable.values()[i], plist[i], 
                    incr_list[i], decr_list[i])
    print "-" * 50
    print


def main():
    parser = argparse.ArgumentParser(description='Dice utility for gamers.')
    parser.add_argument('dice', nargs='?', default='1d20',
            help='Dice setting. A valid dice is like "1d8", "4d6" or \
                    "2d4+2". The default value is "1d20"')
    parser.add_argument('--stats', action='store_true',
            help='Instead of rolling the dice, this option will list \
                    the statistics of the dice.')
    args = parser.parse_args()

    if args.stats:
        calc_stats(args.dice)
        sys.exit()

    roll_dice(args.dice)


if __name__ == "__main__":
    main()

