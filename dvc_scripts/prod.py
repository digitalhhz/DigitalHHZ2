import os
os.system('sh /app/scripts/dvc-pull.sh')
os.system('python3 /app/scripts/uploadModelAndQueryToS3.py')
os.system('sh /app/scripts/git-checkout-master.sh')