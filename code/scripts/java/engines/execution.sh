#!/usr/bin/env bash

#SBATCH --job-name engine_execution
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

if [ -z "$1" ]
then
  echo 'First argument should be file path!'
  exit 1
fi
java -Xmx8g -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar engine_execution "$1"
