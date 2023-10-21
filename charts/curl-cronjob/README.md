# Wordle

This chart deploys literally just a curl cronjob.  Just provide a schedule and a url.  That's it.

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
helm install <release name> -n <namespace> --create-namespace raackley-stable/curl-cronjob
```
