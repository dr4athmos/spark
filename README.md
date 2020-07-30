# Spark
This repository has the goal of work on spark deployment for the C3.4

## Resume:
The most healthy way to achieve the goal is to deploy spark following documentation, in a way of having more control as possible.

An issue occured following the documentation in running spark-submit command, deviate this approach into a more pragmatical one in order to bring a proof of concept in for the first delivery.

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

### Submit Spark jobs using Zeppelin

## Livy
Apache Livy is a service that enables easy interaction with a Spark cluster over a REST interface https://livy.apache.org/

### Submit Spark jobs
* Open a session
* Wait session turn in state idle
* Send job to session

Look session_run.py for an example
