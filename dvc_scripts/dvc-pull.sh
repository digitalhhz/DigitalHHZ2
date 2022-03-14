#!/bin/bash
gitcommithash=$1

if [ -z ${gitcommithash+x} ]; then echo $gitcommithash='master -f'; else echo "gitcommithash is set to '$var'"; fi

cd /app/cogitat

echo "Checking out $gitcommithash."
git clean -f
git checkout $gitcommithash

echo "Pulling data from dvc remote."
dvc pull --remote kilab-remote

echo "EOF"
exit