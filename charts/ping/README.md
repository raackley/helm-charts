# Ping

This chart deploys a simple nginx deployment that returns "pong" and http 200 on "/ping" (by default), and a related IngressRoute rule.  This could be useful to test your cluster and Ingress externally.

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
helm install <release name> --set ingressroute.service.name=<release name>-nginx -n <namespace> --create-namespace raackley-stable/ping
```
