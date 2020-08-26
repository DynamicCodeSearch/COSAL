#!/usr/bin/env bash

#SBATCH --job-name filter
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment


java -Xmx8g -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar filter
