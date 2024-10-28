# MeshCommander

This chart deploys MeshCommander. MeshCommander is a Intel® AMT remote management tool, that allows you to manage Intel® AMT clients from a web browser.

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
helm install <release name> -n <namespace> --create-namespace raackley-stable/meshcommander
```
