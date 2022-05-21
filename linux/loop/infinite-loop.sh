#!/bin/bash

for item in $(ls)
do
  if [[-f $item]]
  then
    continue
  fi
  sudo mv "./$item" "../folder-3/"
  echo $item
done
