# Wireguard

This helm chart will install a Wireguard server.

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
helm install <release name> -n <namespace> --create-namespace raackley-stable/wireguard
```

## Settings

| Key           | Type   | Default | Description                                 |
| ------------- | ------ | ------- | ------------------------------------------- |
| env.peers     | string | "1"     | Number of peers to create config files for. |
| env.serverUrl | string | n/a     | External host the client will connect to.   |
| env.peerDNS   | string | n/a     | DNS server to use.                          |
