# Aircraft Tracker

This deploys containers, and a set of services that will track Aircraft via ADS-B receiver, and then uploads the data to FlightAware and FlightRadar24.  Other feeders such as ADS-B Exchange can be configured as part of the Ultrafeeder deployment.

Deployment that reads data from receiver is based on: [https://github.com/sdr-enthusiasts/docker-adsb-ultrafeeder](https://github.com/sdr-enthusiasts/docker-adsb-ultrafeeder)

Deployment that sends data to FlightAware is based on: [https://github.com/sdr-enthusiasts/docker-piaware](https://github.com/sdr-enthusiasts/docker-piaware)

Deployment that sends data to FlightRadar24 is based on: [https://github.com/sdr-enthusiasts/docker-flightradar24](https://github.com/sdr-enthusiasts/docker-flightradar24)

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
helm install <release name> -n <namespace> --create-namespace raackley-stable/aircraft-tracker
```
