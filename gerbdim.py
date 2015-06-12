#!/usr/bin/env python
# Gerber query script
# Usage: ./gerber_query.py board_edges.gbr
# Written by Matthew Beckler for Wayne and Layne, LLC
# Based on a script from @laen
# Released into the Public Domain. Have fun

def main():
    import sys
    if len(sys.argv) < 2:
        print "Usage: %s gerberfile" % sys.argv[0]
        sys.exit()

    import re
    filename = sys.argv[1]
    xmin = None
    xmax = None
    ymin = None
    ymax = None
    for line in file(filename):
        results = re.search("^X([\d-]+)Y([\d-]+)", line.strip())
        if results:
            x = int(results.group(1))
            y = int(results.group(2))
            print x, y
            xmin = min(xmin, x) if xmin else x
            xmax = max(xmax, x) if xmax else x
            ymin = min(ymin, y) if ymin else y
            ymax = max(ymax, y) if ymax else y

    print "Board dimensions:"
    w = xmax - xmin
    h = ymax - ymin
    w_mm = w / 1000000.0
    h_mm = h / 1000000.0
    print "  (%d, %d) original units" % (w, h)
    print "  (%.4f, %.4f) mm" % (w_mm, h_mm)

if __name__ == "__main__":
    main()
