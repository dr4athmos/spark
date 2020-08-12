### Spark k8s deployment
https://spark.apache.org/docs/latest/running-on-kubernetes.html
https://spark.apache.org/docs/latest/building-spark.html

## Prerequisites from the docs
- A runnable distribution of Spark 2.3 or above.
- A running Kubernetes cluster at version >= 1.6 with access configured to it using kubectl. If you do not already have a working Kubernetes cluster, you may set up a test cluster on your local machine using minikube.
    - We recommend using the latest release of minikube with the DNS addon enabled.
    - Be aware that the default minikube configuration is not enough for running Spark applications. We recommend 3 CPUs and 4g of memory to be able to start a simple Spark application with a single executor.
- You must have appropriate permissions to list, create, edit and delete pods in your cluster. You can verify that you can list these resources by running kubectl auth can-i <list|create|edit|delete> pods.
    - The service account credentials used by the driver pods must be allowed to create pods, services and configmaps.
- You must have Kubernetes DNS configured in your cluster.

## Status
built image from a runnable distribution of spark, pushed on dockerhub and used with spark-submit:
./bin/spark-submit \
    --master k8s://https://k8s-api-pa1.cloud.garr.it:443 \
    --deploy-mode cluster \
    --name spark-pi \
    --class org.apache.spark.examples.SparkPi \
    --conf spark.executor.instances=2 \
    --conf spark.kubernetes.container.image=dr4thmos/spark:dist_built \
    --conf spark.kubernetes.namespace=g-thomascecconello-unimibit \
    --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark \
    local:///$SPARK_HOME/examples/jars/spark-examples_2.12-3.0.0.jar 100000

pod doesn't found volumes and configmaps, but these are in the k8s cluster:
![Issue](https://github.com/dr4thmos/spark_submit/spark_submit_issue.png)