TARGETS := resources.py Ui_etrimain.py Ui_refsdialog.py

all: $(TARGETS) 

resources.py: resources.qrc
	pyrcc4 -o resources.py resources.qrc

Ui_refsdialog.py: refsdialog.ui
	pyuic4 -o $@ $<

Ui_etrimain.py: etrimain.ui
	pyuic4 -o $@ $<

clean: 
	rm -f *.pyc

mrproper: clean
	rm -f $(TARGETS)

.PHONY: all clean mrproper
