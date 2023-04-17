#!/bin/bash

function create {
	EXPECTED_ARGS=6 # Update with the expected number of arguments
	if [ $# -lt $EXPECTED_ARGS ]; then
	 echo "Usage: $0 repo_name description Token main_directory private Username" # Update with your help message or usage instructions
  	 return 1 # Exit with an error code
	fi
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
