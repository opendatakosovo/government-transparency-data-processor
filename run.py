# -*- coding: utf-8 -*-
import os
import json
import pandas as pd
from pymongo import MongoClient
from slugify import slugify

# Const
ARBK_DATASET_DIR = './data/datasets/arbk/'
AKK_DATASET_DIR = './data/datasets/akk/'
PROCUREMENT_DATASET_DIR = './data/datasets/open-procurement'

# TODO: Processing and importing