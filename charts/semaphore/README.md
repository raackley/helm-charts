# Ansible Semaphore

This chart deploys Ansible Semaphore.

Project info can be found [here](https://www.ansible-semaphore.com/)

## Installation

Add and update the Helm repo.

```
helm repo add raackley-charts https://charts.ryanackley.com
```

```
helm repo update
```

Install (Helm v3).

```
helm install <release name> -n <namespace> --create-namespace raackley-stable/semaphore
```
