# Transmission-VPN

This helm chart will install a Transmission (Bittorrent) server with VPN client.

This helm chart is based off of [this](https://github.com/haugene/docker-transmission-openvpn) project.  See the project's documentation for more details.

Non-built-in VPN config can be found in [this](https://github.com/haugene/vpn-configs-contrib) project.

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
helm install <release name> -n <namespace> --create-namespace raackley-stable/transmission-vpn
```
