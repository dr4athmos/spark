## Helm chart
### Prerequisites:
* kubectl configured
* Helm (Actually using v3.2.4)

### How to deploy:
* Add repo and install charm
```
helm repo add microsoft https://microsoft.github.io/charts/repo
helm install microsoft/spark --version 1.0.4
```

### Zeppelin
Zeppelin is a notebook with spark integrated, and a wide range of interpreters

#### Submit Spark jobs using Zeppelin
Create a notebook, in each section specify interpreter like:
```
%spark
somespark....

%sh
some sh.....

```

And run the section.

A zeppelin application allocates some resources in the spark cluster, so to use other application (like Livy session) it's necessary to kill the application in Spark webui. To restart the application go to menu -> interpreter -> spark -> restart

### Livy
Apache Livy is a service that enables easy interaction with a Spark cluster over a REST interface https://livy.apache.org/

#### Submit Spark jobs
* Open a session
* Wait session turn in state idle
* Send jobs to session

Look session_run.py for an example

## Known issues

### Helm chart
* Numpy is installed in the zeppelin pod, but not in the spark master and workers, and so spark jobs sended to cluster pretending to run spark MLlib doesn't work.
    * The problem is that the dependencies need to be sended with the job or installe directly in the cluster
        * Tried to send dependencies in a zip file (e.g. numpy) but it doesn't work
        * Tried to install dependencies in all worker and master, but it doesn't work 


## Working on

* Send job with dependencies
    * Tried with add dependencies in zeppelin interpreter, but it doesn't solve the problem

* Trying to modify helm chart to install libraries in the cluster
    * To download chart ```helm fetch microsoft/spark --version 1.0.4 --untar```

* Trying to install libraries directly in spark cluster pods (master and workers)
    * Done, but it doesn't solve the problem