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
sudo apt-get install python3 python3-pip make wkhtmltopdf python3-qrcode
sudo pip install kicad_netlist_reader
sudo make install
```

For develop version run ```sh sudo make devolp``` instend of ```sh sudo make install```


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
