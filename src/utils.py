import json
import numpy as np
import random
import os

def set_seed(seed=42):
    np.random.seed(seed)
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)

def save_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f)