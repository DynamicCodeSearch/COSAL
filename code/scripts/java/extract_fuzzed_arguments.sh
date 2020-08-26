#!/usr/bin/env bash

#SBATCH --job-name extract_fuzzed_args
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

if [ -z "$1" ]
then
    echo "Run: sh scripts/java/extract_fuzzed_arguments.sh <do_delete_old> ... "
    exit 1
else
    java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar extract_fuzzed_args "$1"
fi
