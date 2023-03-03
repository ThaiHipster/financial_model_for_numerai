import time
start = time.time()

import pandas as pd
from lightgbm import LGBMRegressor
import gc
import json

from numerapi import NumerAPI
from halo import Halo
from utils import (
    save_model,
    load_model,
    neutralize,
    get_biggest_change_features,
    validation_metrics,
    ERA_COL,
    DATA_TYPE_COL,
    TARGET_COL,
    EXAMPLE_PREDS_COL
)


napi = NumerAPI()
spinner = Halo(text='', spinner='dots')