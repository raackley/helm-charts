# vlmcsd

This chart deploys vlmcsd. More information about the project can be found [here](https://github.com/Wind4/vlmcsd).  The container image can be found [here](https://hub.docker.com/r/dreista/vlmcsd).

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
helm install <release name> -n <namespace> --create-namespace raackley-stable/vlmcsd
```
