# Helm Charts

## Description
This is a collection of various Helm Charts.  Each Helm Chart is in it's own subdirectory with specific instructions for usage.

## Helm Charts
* Wireguard Server
* Transmission Bittorrent Server with VPN
* Aircraft Tracker

## Chart Repository
Charts in this project are stored in a GitLab Package Repo.  To install the Helm repo, run the following.

```
helm repo add raackley-stable https://gitlab.com/api/v4/projects/34881477/packages/helm/stable
```

There is also a testing repo you can optionally use.  This repo is only updated from Merge Request branches.

```
helm repo add raackley-stable https://gitlab.com/api/v4/projects/34881477/packages/helm/test
```
