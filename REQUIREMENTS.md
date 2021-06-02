### Hardware
* COSAL requires atleast 4GB of memory to function on smaller programs. Storage and number of processors vary based on the size of the targe code for clone detection.
* For the CodeJam dataset used in the paper, we used a 16 node cluster 4-core AMD opteron processor and 32GB DDR3 1333 ECCDRAM. This took around 2 hours for COSAL to identify clusters in the dataset.

### Java
* COSAL requires [JDK version 1.8](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html). After downloading this version configure the environment variable **$JAVA_HOME** to the path where Java is installed.
* We also use [maven version 3.3+](https://maven.apache.org/download.cgi). Make sure you can access the maven command `mvn` form a command line window.
* We would recommend a GUI like [Intellij Idea](https://www.jetbrains.com/idea/) or [Eclipse](https://www.eclipse.org/downloads/) if you plan on editing the source code.
* The additional java dependencies can be installed by running `mvn clean install` in `COSAL/code` folder.

```
> cd COSAL/code
> mvn clean install
```

### Python
* We use python [3.6+](https://www.python.org/downloads/). Make sure you can access `python` from the command line after installing python.
* For managing python packages we use [pip 9.0+](https://pip.pypa.io/en/stable/installing/). Make sure you can access `pip` from the command line after installing pip.
* To install required python libraries 
```
> cd COSAL/code
> pip install -r requirements.txt
```
