# wg-easy

This chart deploys wg-easy. Wg-easy is an implementation of WireGuard combined with an easy to use Web UI.

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
helm install <release name> -n <namespace> --create-namespace raackley-stable/wg-easy
```
