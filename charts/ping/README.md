# Ping

This chart deploys a simple nginx deployment that returns "pong" and http 200 on "/ping" (by default), and a related IngressRoute rule.  This could be useful to test your cluster and Ingress externally.

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
helm install <release name> -n <namespace> --create-namespace raackley-stable/ping
```
