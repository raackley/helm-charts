# flaresolverr

This chart deploys flaresolverr. FlareSolverr is a proxy server to bypass Cloudflare and DDoS-GUARD protection.
More information about flaresolverr can be found [here](https://github.com/FlareSolverr/FlareSolverr).

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
helm install <release name> -n <namespace> --create-namespace raackley-stable/flaresolverr
```
