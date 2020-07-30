# Spark

##Prerequisites:
* kubectl configured

##How to deploy:
* Install Helm (Actually using v3.2.4)
* Add repo and install charm
'''
helm repo add microsoft https://microsoft.github.io/charts/repo
helm install microsoft/spark --version 1.0.4
'''
