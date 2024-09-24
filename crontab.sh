#!/bin/bash

cd /home/user/app/seafile/

/usr/bin/dvc add ./data
/usr/bin/dvc push -vvv

/usr/bin/git add ./data.dvc
/usr/bin/git commit -m "$(date)"
/usr/bin/git push origin main
