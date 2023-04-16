#!/bin/bash

function create {
	python main.py $1 $2 $3 $4 $5
	cd
	cd $4
	cd $1
	echo "# $1" > README.md
        echo "$2" > README.md
	git init
	git add README.md
	git commit -m "initial commit"
	git branch -M master
	git remote add origin git@github.com:$6/$1.git
	git push -u origin master
	code .	
}
