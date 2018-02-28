all: utils

install: utils
	apt install python-qrcode python3-pip python-jinja2
	pip3 install pygments pyenchant markdown markdown_checklist pyqrcode
	cd utils; make install
	cp mlabgen-module-check   /usr/bin/
	cp mlabgen-module-html    /usr/bin/
	cp mlabgen-module-init    /usr/bin/
	cp mlabgen-module-md      /usr/bin/
	cp mlabgen-module-prjinfo /usr/bin/
	cp mlabgen-module-readme-update   /usr/bin/
	cp mlabgen-module-make-production /usr/bin/
	cp mlabgen-dir-html       /usr/bin/
	cp mlabgen                /usr/bin/
	cp mlabgen.py             /usr/lib/python3/dist-packages/
	cp markdown_sch.py        /usr/lib/python3/dist-packages/
	cp mlabgen.mk             /usr/include/
	mkdir -p /usr/share/mlabgen
	cp -r module              /usr/share/mlabgen/
	cp -r templates              /usr/share/mlabgen/
	cp style.css              /usr/share/mlabgen/

develop: utils
	apt install python-qrcode python3-pip python-jinja2
	pip3 install pygments pyenchant markdown markdown_checklist pyqrcode
	cd utils; make install
	ln mlabgen-module-check   /usr/bin/
	ln mlabgen-module-html    /usr/bin/
	ln mlabgen-module-init    /usr/bin/
	ln mlabgen-module-md      /usr/bin/
	ln mlabgen-module-prjinfo /usr/bin/
	ln mlabgen-module-readme-update   /usr/bin/
	ln mlabgen-module-prepare-doc   /usr/bin/
	ln mlabgen-module-make-production /usr/bin/
	ln mlabgen-dir-html       /usr/bin/
	ln mlabgen                /usr/bin/
	ln mlabgen.py             /usr/lib/python3/dist-packages/
	ln markdown_sch.py        /usr/lib/python3/dist-packages/
	ln mlabgen.mk             /usr/include/
	mkdir -p /usr/share/mlabgen
	cp -r module/              /usr/share/mlabgen/
	cp -r templates/           /usr/share/mlabgen/
	ln style.css              /usr/share/mlabgen/


utils:
	git clone https://github.com/MLAB-project/utils.git

uninstall:
	rm -f /usr/bin/mlabgen*
	rm -rf /usr/lib/python3/dist-packages/mlabgen.py
	rm -rf /usr/lib/python3/dist-packages/markdown_sch.py
	rm -rf /usr/include/mlabgen.mk
	rm -rf /usr/share/mlabgen*

.PHONY: install uninstall
