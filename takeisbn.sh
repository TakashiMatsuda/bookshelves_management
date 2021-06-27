#!/bin/bash

for photo in $(find $1 -name '*.JPG'); do
  zbarimg --raw -q "$photo" | grep "^978";
done
