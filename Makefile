.ONESHELL:
SHELL = /bin/bash

.PHONY : env html clean

env:
	conda env update -f environment.yml --prune

html :
	myst build --html

.SILENT: clean
clean : 
	rm -f figures/* audio/*
	rm -rf _build/*

