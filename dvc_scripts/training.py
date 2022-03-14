import os
os.system('python3 /app/scripts/loadModelFromS3.py')
os.system('python3 /app/scripts/loadQueryFromS3.py')
os.system('python3 /app/scripts/createModelcard.py')
os.system('sh /app/scripts/dvc-push.sh')