# Transmission-VPN

This helm chart will install a Transmission (Bittorrent) server with VPN client.

This helm chart is based off of [this](https://github.com/haugene/docker-transmission-openvpn) project.  See the project's documentation for more details.

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
helm install <release name> -n <namespace> --create-namespace raackley-stable/transmission-vpn
```
