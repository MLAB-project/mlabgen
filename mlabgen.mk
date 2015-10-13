MODULE = $(notdir $(PWD))

all: $(TARGETS)

clean: 
	@echo "CLEAN"
	@rm -f $(TARGETS)

check: DOC/SRC/$(MODULE).md.in PrjInfo.txt SCH_PCB/$(MODULE).sch
	@echo "CHECK"
	@mlabgen-module-check $^

DOC/%.html: DOC/SRC/%.html.in PrjInfo.txt DOC/SRC/%.md
	@echo "HTML    $@"
	@mlabgen-module-html $^ $@ 

DOC/SRC/%.md: DOC/SRC/%.md.in CAM_PROFI/%-Edge_Cuts.gbr SCH_PCB/%.sch PrjInfo.txt
	@echo "MD      $@"
	@mlabgen-module-md $^ $@

PrjInfo.txt: PrjInfo.txt.in SCH_PCB/$(MODULE).sch
	@echo "PRJINFO $@"
	@mlabgen-module-prjinfo $^ $@

DOC/%.pdf: DOC/%.html
	@echo "PDF     $@"
	@-wkhtmltopdf -q $^ $@

.PHONY: all clean check
