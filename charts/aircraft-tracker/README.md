# Aircraft Tracker

This deploys containers, and a set of services that will track Aircraft via ADS-B receiver, and then uploads the data to FlightAware and to FlightRadar24.

Deployment that reads data from receiver is based on: [https://github.com/sdr-enthusiasts/docker-readsb-protobuf](https://github.com/sdr-enthusiasts/docker-readsb-protobuf)

Deployment that seds data to FlightAware is based on: [https://github.com/sdr-enthusiasts/docker-piaware](https://github.com/sdr-enthusiasts/docker-piaware)

Deployment that sends data to FlightRadar24 is based on: [https://github.com/sdr-enthusiasts/docker-flightradar24](https://github.com/sdr-enthusiasts/docker-flightradar24)

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
helm install <release name> -n <namespace> --create-namespace raackley-stable/aircraft-tracker
```
