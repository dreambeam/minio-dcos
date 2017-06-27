#!/usr/bin/env python
import os

marathon_app_id = os.environ["MARATHON_APP_ID"]
app_id = marathon_app_id[1:]
ids=app_id.split('/')
print('-'.join(ids[::-1]) + ".marathon.containerip.dcos.thisdcos.directory")
