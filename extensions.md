Markdown extensions
===================

Abbreviation
------------

The MLAB project is truly awesome!

*[MLAB]: Modular LABoratory


Code
----

```python3
import markdown
while True:
    print(input("Hello>"))
```

Inline code `is also cool`

```c
#include <stdio.h>

int main(argv**, argc**) {
    printf("Hello World\n\r");
    return 0
}
```

Sprites
-------

!begx;begy;endx;endy;!(path_to_img)

begx, begy - top left corner of the selection in millimeters
endx, endy - bottom right corner of the selection in millimeters

It's always cool to have equations in docs
------------------------------------------

AsciiMath is realy neat format.
When $Ma != 0M$, there are two solutions to $M ax^2 + bx + c = 0 M$ and they are 

$M x = (-b +- sqrt(b^2-4ac))/(2a) . M$

Table
-----

First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell

Checklist
---------

* [ ] Task1
* [x] Task2
* [ ] Task3

Newline 2 break
---------------

This is first line
This is second line
