# VPN Proxy

This chart deploys a VPN Proxy service.  This uses the gluetun container which connects to a VPN server and provides a proxy service for apps to connect to.

[This](https://github.com/qdm12/gluetun-wiki/blob/main/setup/connect-a-lan-device-to-gluetun.md) explains how to configure the proxy.

[This](https://github.com/qdm12/gluetun-wiki/tree/main/setup/providers) explains how to configure your VPN if you use one of the given services.  If you do not have one of them, you can still configure an OpenVPN servicer described [here](https://github.com/qdm12/gluetun-wiki/blob/main/setup/openvpn-configuration-file.md).


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
helm install <release name> -n <namespace> --create-namespace raackley-stable/vpn-proxy
```
