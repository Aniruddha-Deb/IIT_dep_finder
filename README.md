# IIT dep finder
Script + Data to determine optimal IIT department

Note that this is based on JoSAA 2019 round 1 seat allocation and that too ONLY for general gender-neutral seats (the others have it easy anyway :)

---------------

## Installation:
```
git clone https://github.com/Aniruddha-Deb/IIT_dep_finder.git
```

## Usage:
```
python3 iit_dep_finder.py <rank>
```
This lists the departments sorted in increasing order of closing rank, with opening rank > your rank and closing rank < your rank, and closing rank < 1200 (tweak this in the `criteria_satisfied` method if needed)
Here's an example:
```
python3 iit_dep_finder.py 300
Kharagpur Computer Science and Engineering(BTech) 204 283
Bombay Electrical Engineering(BTech) 71 292
Delhi Mathematics and Computing(BTech) 97 314
Madras Electrical Engineering(BTech) 182 717
Bombay Mechanical Engineering(BTech) 196 998
Bombay BS in Mathematics(BS) 98 1041
```

Lot of scope for flexibility: just change the `data.txt` file with different data from JoSAA (eg 2018, 2017 or 2016) to see a different analysis.
