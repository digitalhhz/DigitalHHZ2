#!/bin/bash

cd /app/cogitat

#
# Commit dvc then push to remote
#
dvc status

echo "Adding cogitat/data to dvc"
dvc add data --to-remote

echo "Committing cogitat/data to dvc"
dvc commit

echo "Pushing data to remote"
dvc push --remote kilab-remote
echo "Push to remote successful."

#
# Commit git then push to master
#
git status

echo "Staging data.dvc ./modelcard and ./query"
git add -f ./data.dvc
git add modelcard
git add query

echo "Committing all changes."
git commit -m "Update Model"

echo "Pushing to git."
git push origin HEAD:master --force
echo "Push to git repo successful."

echo "EOF"

exit