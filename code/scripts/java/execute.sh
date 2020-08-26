#!/usr/bin/env bash

#SBATCH --job-name execute
#SBATCH -N 1
#SBATCH -p opteron
# Use modules to set the software environment

if [ -z "$1" ]
then
    java -Xmx16g -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar execute
else
    java -Xmx16g -jar target/code-1.0-SNAPSHOT-jar-with-dependencies.jar execute "$1"
fi


## Codejam
#sbatch scripts/java/execute.sh CodeJam
#--- OR ---
#sbatch scripts/java/execute.sh CodeJam Y11R5P1
#sbatch scripts/java/execute.sh CodeJam Y12R5P1
#sbatch scripts/java/execute.sh CodeJam Y13R5P1
#sbatch scripts/java/execute.sh CodeJam Y14R5P1

## IntroClassJava
#sbatch scripts/java/execute.sh IntroClassJava
#--- OR ---
#sbatch scripts/java/execute.sh IntroClassJava checksum
#sbatch scripts/java/execute.sh IntroClassJava digits
#sbatch scripts/java/execute.sh IntroClassJava grade
#sbatch scripts/java/execute.sh IntroClassJava median
#sbatch scripts/java/execute.sh IntroClassJava smallest
#sbatch scripts/java/execute.sh IntroClassJava syllables

``