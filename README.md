# nflrushdb

## Overview
A Python project for working with denormalized Next Gen Stats NFL data and deriving new metrics.

## Getting Started
```
$ python3 -m venv ENV
$ source ENV/bin/activate # For Unix machines
$ \path\to\ENV\Scripts\activate # For Windows machines
$ pip3 install -r requirements.txt
```

## To Do:
- [ ] Build out Game class
- [ ] Derive play-level metrics, e.g. snap to handoff time, defenders in play direction 
- [ ] Derive positional metrics, both across inter and intra players, e.g. distance between each player, closest defender
- [ ] Clean Offense Personnel and Defense Personnel data
- [ ] Spread defensive lines vs. pinched defensive lines classifications
- [ ] Run blocking assignments, or number of offensive personnel involved in run blocking
