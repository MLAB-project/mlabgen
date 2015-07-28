all: install

install:
	pip3 install pygments pyenchant markdown markdown_checklist
	cp mlabgen-module-check   /usr/bin/
	cp mlabgen-module-html    /usr/bin/
	cp mlabgen-module-init    /usr/bin/
	cp mlabgen-module-md      /usr/bin/
	cp mlabgen-module-prjinfo /usr/bin/
	cp mlabgen.py             /usr/lib/python3/dist-packages/
	cp mlabgen.mk             /usr/include/
	mkdir -p /usr/share/mlabgen
	cp -r module              /usr/share/mlabgen/
	cp style.css              /usr/share/mlabgen/

uninstall:
	rm -f /usr/bin/mlabgen*
	rm -rf /usr/lib/python3/dist-packages/mlabgen.py
	rm -rf /usr/include/mlabgen.mk
	rm -rf /usr/share/mlabgen

.PHONY: install uninstall
