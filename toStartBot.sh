#!/usr/bin/env python

`python3 mainFile.py`

while [ $? -ne 0 ]
do
	echo 'Restarting Bot...'
	`python3 mainFile.py`
done
