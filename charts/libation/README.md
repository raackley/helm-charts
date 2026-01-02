# Libation

This chart deploys Libation. Libation is an indexer manager/proxy built on the popular arr .net/reactjs base stack to integrate with your various PVR apps. Libation supports management of both Torrent Trackers and Usenet Indexers.

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
helm install <release name> -n <namespace> --create-namespace raackley-stable/libation
```
