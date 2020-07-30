# Spark
This repository has the goal of work on spark deployment for the C3.4

## Resume:
The most healthy way to achieve the goal is to deploy spark following documentation, in a way of having more control as possible.
An issue occured following the documentation, and so running spark-submit command, deviate this approach into a more pragmatical one in order to arrive at the first delivery with a proof of concept.
For this reason using a preconfigured Helm chart is considered. Unfortunately the chart show some issue with MLlib, that will is the main use of deployment. Moreover the control of the chart is less than a hand-made deployment.

In the following text it's described the specs of the chart with some usefull command and already tried approach.

## Prerequisites:
* kubectl configured

## How to deploy:
* Install Helm (Actually using v3.2.4)
* Add repo and install charm
```
helm repo add microsoft https://microsoft.github.io/charts/repo
helm install microsoft/spark --version 1.0.4
```
