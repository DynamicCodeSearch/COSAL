#!/usr/bin/env bash

#SBATCH --job-name arg_generation
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

if [ -z "$2" ]
then
  echo 'Args: <Input Key> <Num Args>'
  exit 1
fi
java -Xmx8g -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar argument_engine "$1" "$2"

