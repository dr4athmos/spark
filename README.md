# Spark
This repository has the goal of work on spark deployment for the C3.4

## Resume:
The most healthy way to achieve the goal is to deploy spark by following documentation, in a way of having more control as possible on the deployment.

An issue occured following the documentation in running spark-submit command, deviate this approach into a more pragmatical one in order to bring a proof of concept for the first delivery.

For this reason using a preconfigured Helm chart was considered. Unfortunately the chart show some issue with MLlib, that will be the main use of this deployment. Moreover the control of the chart is less than a hand-made deployment.

Positive note is that this solution suggest the use of Livy that could be used to manage jobs queue (to investigate)

Next it's described the specs of the chart with some usefull command and already tried approach.

## Helm chart
### Prerequisites:
* kubectl configured

### How to deploy:
* Install Helm (Actually using v3.2.4)
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

A zeppelin application allocates some resources in the spark cluster, so to use other application like Livy session it's needed to kill the application in Spark webui. To restart the application go to menu -> interpreter -> spark -> restart

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

* Pods OS is alpine linux and some dependencies for python libraries may be missing.

### Spark k8s deployment

spark-submit gives "missing OAUTH", the same problem occurs with other command not related with spark. 

Details in spark-submit_issue.txt

## Working on

* Trying to document and send to Claudio Pisa the spark k8s deployment issue

* Trying to modify helm chart to install libraries in the cluster
    * To download chart ```helm fetch microsoft/spark --version 1.0.4 --untar```

* Trying to install libraries connecting into the spark cluster pod (master and workers)