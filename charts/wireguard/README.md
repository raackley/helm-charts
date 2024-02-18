# Wireguard

DEPRECATED: Please use wg-easy instead.

This helm chart will install a Wireguard server.

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
helm install <release name> -n <namespace> --create-namespace raackley-stable/wireguard
```

## Settings

| Key                    | Type   | Default   | Description                                      |
| ---------------------- | ------ | --------- | ------------------------------------------------ |
| env.peers              | string | "1"       | Number of peers to create config files for.      |
| env.serverUrl          | string | n/a       | External host the client will connect to.        |
| env.peerDNS            | string | n/a       | DNS server to use.                               |
| service.type           | string | ClusterIP | Service type to use for Wireguard.               |
| service.loadBalancerIP | string | n/a       | IP for Load Balancer if using type LoadBalancer. |
| persistence.enabled    | bool   | false     | Enables persistent storage                       |
| persistence.size       | string | "100Mi"   | Size of persistent storage volume                |
