#!/usr/bin/env python3
# convert symbolab.com solution to latex
# from the console, on a solution page do:
#   copy(SYSTEPS.stepsArray)
# and put it in a file
# then run this programme:
#   tolatex.py ems_15.1.4.json

import json
import sys

with open(sys.argv[1]) as fp:
    sol_dict = json.load(fp)

def traverse_steps(steps):
    result = ''
    for step in steps:
        result += output_step(step)
    return result

def output_step(step):
    step_latex = ''
    if 'entire_result' in step:
        step_latex = step['entire_result']
    else:
        step_latex = ''
    return '$$' + step_latex + '$$' + '\n'

print(traverse_steps(sol_dict))
