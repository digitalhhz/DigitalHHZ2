#!/usr/bin/env python

# import sys
import model_card_toolkit as mctlib
import tempfile
import os
from datetime import datetime

name_arg = "Cogitat AI - Occupancy"
overview_arg = '''This a decision tree classification model auto-generated using mljar. 
It aims to classify whether a room is occupied or not based on the features light intensity and 
temperature. The model is trained on a dataset consisting of sensor values obtained by the 
digitalhhz infrastructure's database. The respective query is documented in the Documentation 
section of this Model Card.'''
usecase_arg = '''The infrastructure that provides the data used to train this model was 
created by the authors as part of the semester project in the Master degree course Digital Business 
Engineering at the Herman-Hollerith-Center of Reutlingen University in Boeblingen, Germany. 
As the second semester project the authors implemented the pipeline which trains, validates, 
versions, and uses this model. 

The model itself can be used to predict the occupancy of room 026/027 at HHZ.'''

# https://github.com/tensorflow/model-card-toolkit/blob/master/model_card_toolkit/model_card_toolkit.py
model_card_dir = tempfile.mkdtemp()
print(model_card_dir)

mct = mctlib.ModelCardToolkit(model_card_dir)

# https://github.com/tensorflow/model-card-toolkit/blob/master/model_card_toolkit/model_card.py
model_card = mct.scaffold_assets()

with open('/app/cogitat/query/influxQueryLast30Days.sql', 'r') as file:
    query = file.read().replace('\n', '')
print (query)

model_card.model_details.name = name_arg
model_card.model_details.overview = overview_arg
model_card.model_details.documentation = query
model_card.model_details.owners = [
  mctlib.Owner(name='DigitalHHZ', contact='digitalhhz@gmail.com'),
  mctlib.Owner(name='Andreas Greiss', contact='https://github.com/angrit06'),
  mctlib.Owner(name='Jonathan Maier', contact='https://github.com/eGGenius'),
  mctlib.Owner(name='Tilman Welsch', contact='https://github.com/TilmanWelsch'),
  mctlib.Owner(name='Sedat Yasar', contact='https://github.com/SedatYasar')
]
model_card.model_details.version = mctlib.Version(name='Cogitat AI v1.0', date=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
model_card.model_details.references = [
    mctlib.Reference(reference='https://github.com/digitalhhz/DigitalHHZ2'),
    mctlib.Reference(reference='https://github.com/digitalhhz/cogitat'),
    mctlib.Reference(reference='https://arxiv.org/pdf/1810.03993.pdf'),
]
model_card.model_details.licenses = [mctlib.License(identifier='Apache-2.0')]


model_card.considerations.use_cases = [
    mctlib.UseCase(description=usecase_arg)
]
model_card.considerations.user = [
    mctlib.user(description="Professors of HHZ"),
    mctlib.user(description="Students of HHZ"),
    mctlib.user(description="Guests and visitors of HHZ"),
]

mct.update_model_card(model_card)

# Generate a model card document in HTML
html_path = os.path.join(model_card_dir, 'template/html/default_template.md.jinja')
html_doc = mct.export_format(template_path=html_path)
file = open("model_card.html","w")
file.write(html_doc)
file.close()

# Generate a model card document in Markdown
md_path = os.path.join(model_card_dir, 'template/md/default_template.md.jinja')
md_doc = mct.export_format(template_path=md_path)
file = open("model_card.md","w")
file.write(md_doc)
file.close()

# move files to repo dir
if not os.path.exists('/app/cogitat/modelcard/'):
    os.makedirs('/app/cogitat/modelcard/')

os.replace("./model_card.html","/app/cogitat/modelcard/model_card.html")
os.replace("./model_card.md","/app/cogitat/modelcard/model_card.md")
