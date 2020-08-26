#!/usr/bin/env bash

#SBATCH --job-name permutate
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment


if [ -z "$1" ]
then
    echo "Run: sh scripts/java/initialize.sh 'dataset'/'project' ... "
    exit 1
fi

java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar initialize "$1"
