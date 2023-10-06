# Wordle

This chart deploys Reddit History Deleter cronjob.  See [this](https://gitlab.com/raackley/reddit-history-deleter) for project details.

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
helm install <release name> -n <namespace> --create-namespace raackley-stable/reddit-history-deleter
```
