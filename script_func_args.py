from xform import *
from dataflow import *

import script_preserveds

def apply(cfg):
    script_preserveds.apply(cfg)
    collect_params(cfg)
