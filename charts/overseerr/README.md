# Overseerr

This chart deploys Overseerr.  Overseerr is a request management and media discovery tool built to work with your existing Plex ecosystem.

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
helm install <release name> -n <namespace> --create-namespace raackley-stable/overseerr
```
