#!/usr/bin/python
# -*- encoding: utf-8 -*-

import os

model_list = os.listdir('dm_models/')
model_list = [a[:-3] for a in model_list if ('.py' in a)]
model_list.remove('__init__')

__all__ = model_list
