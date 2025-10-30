.ONESHELL:
SHELL = /bin/bash

.SILENT: clean
.PHONY : clean
clean : 
	rm -f figures/* audio/*
	rm -rf _build/*