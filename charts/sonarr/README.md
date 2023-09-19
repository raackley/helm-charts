# Sonarr

This chart deploys Sonarr. Sonarr is a PVR for Usenet and BitTorrent users. It can monitor multiple RSS feeds for new episodes of your favorite shows and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available.

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
helm install <release name> -n <namespace> --create-namespace raackley-stable/sonarr
```
