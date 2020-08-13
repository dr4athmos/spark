### Spark operator
![Architecture](spark-operator_architecture-diagram.png)

- Following the https://dzlab.github.io/ml/2020/07/14/spark-kubernetes/ article spark-operator was deployed in minikube and spark-pi example job was computed.
- Tried same approach with GARR cloud, but it don't work, look at log in [spark-operator-garr-cloud-error](spark-operator-garr-cloud-error.txt)
    - Reported to Claudio Pisa that has the same issue running with superuser, to better inspect
- Following the second part that sends to operator a scala project
    - Can't push in minikube registry, maybe to configure better https://minikube.sigs.k8s.io/docs/handbook/registry/

## Useful resources and some notes
- SparkAI 2019 Spark Operator—Deploy, Manage and Monitor Spark clusters on Kubernetes -Jiri Kremser (Red Hat, Inc):
    - https://www.youtube.com/watch?v=muTqsay1ix4
    - https://github.com/radanalyticsio/spark-operator
- SparkAI 2020 Deploying Apache Spark Jobs on Kubernetes with Helm and Spark Operator:
    - https://www.youtube.com/watch?v=dreE1UdOiIQ&t=609s
    - https://github.com/TomLous/medium-spark-k8s
        - Error in building image at step 8 (java error)
        - Error in push chart at step 10 (chartmuesum mkdir 500 permission denied, probably related to minikube registry issue for GKP spark-on-k8s-operator)
- Google cloud platform spark on k8s operator: (who is using spark k8s operator https://github.com/GoogleCloudPlatform/spark-on-k8s-operator/blob/master/docs/who-is-using.md)
    - https://github.com/GoogleCloudPlatform/spark-on-k8s-operator
        - Error on permission of service account...
            - Solved using initialization of dzlab demo
        - Trying to deploy python application...
            - Ok in minikube
            - Error in GARR cloud, it's not a permission problem, maybe a version compatibility issue?
    - https://dzlab.github.io/ml/2020/07/14/spark-kubernetes/
      https://dzlab.github.io/ml/2020/07/15/spark-kubernetes-2/
      code https://github.com/dzlab/snippets/tree/master/spark-k8s
        - Deployed operator
        - Runned spark-pi example
        - Following second part... Error in pushing into minikube registry (probably some error on port forwarding?)
            - Need to try another registry like dockerhub
        - Spark-pi example works if spark applications are deployed in the same namespace as spark-operator
            - This means that can be replicated in GARR cloud without create another namespace with edit clusterrole
                - Don't work... for log look at spark-operator-garr-cloud-error.txt
