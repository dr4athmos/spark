# Spark
From version 2.4 spark support deployment on k8s.
Recently version 3.0.0 of spark was released and the k8s deployment is currently experimental.
It gives the possibility to build a spark docker image to submit into kubernetes.

Following the "Spark+AI 2020 summit" seems that in the near future deployng spark on k8s
will be done by a kubernates operator called spark operator and mantained by google and databricks.

The Kubernetes Operator for Apache Spark aims to make specifying and running Spark applications as easy and idiomatic as running other workloads on Kubernetes. It uses Kubernetes custom resources for specifying, running, and surfacing status of Spark applications. This tool is in beta version.
In the list of who is using spark-operator there is CERN that may have the same use cases of neanias (https://github.com/GoogleCloudPlatform/spark-on-k8s-operator/blob/master/docs/who-is-using.md)

In this repository is resumed the status of the spark deployment kubernetes cluster in the GARR cloud.
Three folders report the status for each "branch":
- spark_submit for the solution that follows the docs spark docs
- spark-operator for the solution that use the spark operator
- helm_chart for the solution that use the microsoft/spark helm chart with zeppelin and livy

A folder with instruction to run demo on minikube will follow...

