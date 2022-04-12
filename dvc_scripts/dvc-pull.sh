#!/bin/bash
gitcommithash=$1

cd /app/cogitat

echo "Checking out $gitcommithash."
git clean -f
git checkout $gitcommithash

echo "Pulling data from dvc remote."
dvc pull --remote kilab-remote

echo "EOF"
exit
