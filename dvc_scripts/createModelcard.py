#!/usr/bin/env python

# run using: python createModelcard.py name_arg overview_arg usecase_arg description_arg

# import sys
import model_card_toolkit as mctlib
import tempfile
import os
from datetime import datetime

name_arg = "Model card Test Name"
overview_arg = "Model card Test Overview"
usecase_arg = "Model card Test Use Cases"
description_arg = "Model card Test Limitations Description"

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
  mctlib.Owner(name='DigitalHHZ', contact='digitalhhz@gmail.com')
]
model_card.model_details.version = mctlib.Version(name='v1.0', date=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
model_card.model_details.references = [
    mctlib.Reference(reference='https://www.tensorflow.org/guide/keras/transfer_learning'),
    mctlib.Reference(reference='https://arxiv.org/abs/1801.04381'),
]
model_card.model_details.licenses = [mctlib.License(identifier='Apache-2.0')]
model_card.model_details.citations = [mctlib.Citation(citation='https://github.com/tensorflow/model-card-toolkit/blob/master/model_card_toolkit/documentation/examples/Standalone_Model_Card_Toolkit_Demo.ipynb')]


model_card.considerations.use_cases = [
    mctlib.UseCase(description=usecase_arg)
]
model_card.considerations.limitations = [
    mctlib.Limitation(description=description_arg)
]
model_card.considerations.ethical_considerations = [mctlib.Risk(
    name=
        'Ethical considerartions'
        'risk name',
    mitigation_strategy=
        'Ethical considerations risk mitigation strategy'
)]

mct.update_model_card(model_card)

# Generate a model card document in HTML (default)
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