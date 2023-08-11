#!/bin/bash

REQUIREMENTS=./requirements.txt

if [ -f $REQUIREMENTS ]; then
  rm $REQUIREMENTS
fi

pip3 freeze >> $REQUIREMENTS