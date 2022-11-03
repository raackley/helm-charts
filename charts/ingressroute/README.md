# IngressRoute

This is literally just a simple IngressRoute chart.  This could be used along side other packaged charts where an IngressRoute may not have been templated.

## Installation

Add and update the Helm repo.

```
helm repo add raackley-stable https://gitlab.com/api/v4/projects/34881477/packages/helm/stable
```

```
helm repo update
```

Install (Helm v3).

```
helm install <release name> -n <namespace> --create-namespace raackley-stable/ingressroute
```