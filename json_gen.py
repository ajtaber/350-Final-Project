import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import urllib
import boto3
import string
from io import StringIO

client = boto3.client('textract')
s3 = boto3.resource('s3')
bucket = s3.Bucket('project-350-warner')

obj_list = [i.key for i in bucket.objects.all()]
woz_list = [i for i in obj_list if 'pWOZ' in i]
london_list = [i for i in obj_list if 'pLND' in i]
phrase_list = [i for i in obj_list if 'pPHR' in i]

all_imgs = obj_list[1:-21]

file_dict = {}
count = 0
for i in all_imgs:
    resp = client.detect_document_text(Document={'S3Object':
                                                 {'Bucket': 'project-350-warner','Name': f'{i}'}})
    file_dict.update({i.split('/')[-1][:-4]:resp})
    count += 1
    print(f'Finished file {count}/{len(all_imgs)}')
    
with open("responses.json", "w") as outfile:
    json.dump(file_dict, outfile)