# Helm Charts

## Description
This is a collection of various Helm Charts.  Each Helm Chart is in it's own subdirectory with specific instructions for usage.

## Helm Charts
* Aircraft Tracker
* Ansible Semaphore
* IngressRoute
* Lidarr
* Overseerr
* "Ping"
* Plex Server
* Prowlarr
* Radarr
* Readarr
* SearXNG
* Sonarr
* Tautulli
* Transmission Bittorrent Server with VPN
* Wireguard Server
* Wordle

## Chart Repository
Charts in this project are stored in a GitLab Package Repo.  To install the Helm repo, run the following.

```
helm repo add raackley-charts https://charts.ryanackley.com
```

There is also a testing repo you can optionally use.  This repo is only updated from Merge Request branches.

```
helm repo add raackley-charts-test https://charts-test.ryanackley.com
```
