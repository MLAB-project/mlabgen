install:
	git submodule update --init --recursive
	cd markdown-checklist; python3 setup.py install; cd ..;
	cd ../Python-Markdown; python3 setup.py install; cd ..;
	cd ../utils; make install; cd ..;
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

.PHONY: install
