#!/usr/bin/env bash

#SBATCH --job-name snip
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

if [ -z "$1" ]
then
    java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar snip
else
    java -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar snip $1
fi


## Codejam
#sbatch scripts/java/snip.sh CodeJam
#--- OR ---
#sbatch scripts/java/snip.sh CodeJam Y11R5P1
#sbatch scripts/java/snip.sh CodeJam Y12R5P1
#sbatch scripts/java/snip.sh CodeJam Y13R5P1
#sbatch scripts/java/snip.sh CodeJam Y14R5P1

## IntroClassJava
#sbatch scripts/java/snip.sh IntroClassJava
#--- OR ---
#sbatch scripts/java/snip.sh IntroClassJava checksum
#sbatch scripts/java/snip.sh IntroClassJava digits
#sbatch scripts/java/snip.sh IntroClassJava grade
#sbatch scripts/java/snip.sh IntroClassJava median
#sbatch scripts/java/snip.sh IntroClassJava smallest
#sbatch scripts/java/snip.sh IntroClassJava syllables
