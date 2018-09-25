all: utils

install: utils

	mkdir -p module
	mkdir -p module/doc
	mkdir -p module/doc/img
	mkdir -p module/doc/src
	mkdir -p hw

	apt install python-qrcode python3-qrcode python3-pip python-jinja2 enchant
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
	rm -R /usr/share/mlabgen -f
	mkdir -p /usr/share/mlabgen
	cp -r module              /usr/share/mlabgen/
	cp -r templates              /usr/share/mlabgen/
	cp style.css              /usr/share/mlabgen/

develop: utils

	mkdir -p module
	mkdir -p module/doc
	mkdir -p module/doc/img
	mkdir -p module/doc/src
	mkdir -p  hw
	
	apt install python-qrcode python3-qrcode python3-pip python-jinja2 enchant
	pip3 install pygments pyenchant markdown markdown_checklist pyqrcode
	cd utils; make install
	ln -f mlabgen-module-check   /usr/bin/
	ln -f mlabgen-module-html    /usr/bin/
	ln -f mlabgen-module-init    /usr/bin/
	ln -f mlabgen-module-md      /usr/bin/
	ln -f mlabgen-module-prjinfo /usr/bin/
	ln -f mlabgen-module-readme-update   /usr/bin/
	ln -f mlabgen-module-prepare-doc   /usr/bin/
	ln -f mlabgen-module-make-production /usr/bin/
	ln -f mlabgen-module-init-guide /usr/bin/
	ln -f mlabgen-dir-html       /usr/bin/
	ln -f mlabgen                /usr/bin/
	ln -f mlabgen.py             /usr/lib/python3/dist-packages/
	ln -f mlabgen.py             /usr/lib/python2.7/dist-packages/
	ln -f markdown_sch.py        /usr/lib/python3/dist-packages/
	ln -f mlabgen.mk             /usr/include/
	rm -R /usr/share/mlabgen -f
	mkdir -p /usr/share/mlabgen
	cp -r module              /usr/share/mlabgen/
	cp -r templates              /usr/share/mlabgen/
	cp style.css              /usr/share/mlabgen/


utils:
	git clone https://github.com/MLAB-project/utils.git

uninstall:
	rm -f /usr/bin/mlabgen*
	rm -rf /usr/lib/python3/dist-packages/mlabgen.py
	rm -rf /usr/lib/python3/dist-packages/markdown_sch.py
	rm -rf /usr/include/mlabgen.mk
	rm -rf /usr/share/mlabgen*

.PHONY: install uninstall
