Mlabgen
=======

Software for generating documentation of Mlab modules.


Dependecies
-----------

 * python3
 * python3-pip
 * make
 * wkhtmltopdf

Installation
------------

```sh
sudo apt-get install python3 python3-pip make wkhtmltopdf
sudo make install
```

How to initialize new module
----------------------------

```sh
mlabgen-module-init NAMEVERREV
```

How to generate documentation
-----------------------------

In the module's directory execute:

```sh
make
```
