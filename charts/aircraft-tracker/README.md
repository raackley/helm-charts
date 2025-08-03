# Aircraft Tracker

This deploys containers, and a set of services that will track Aircraft via ADS-B receiver, and then uploads the data to FlightAware, FlightRadar24, and ADS-B Exchange.

Deployment that reads data from receiver is based on: [https://github.com/sdr-enthusiasts/docker-adsb-ultrafeeder](https://github.com/sdr-enthusiasts/docker-adsb-ultrafeeder)

Deployment that sends data to FlightAware is based on: [https://github.com/sdr-enthusiasts/docker-piaware](https://github.com/sdr-enthusiasts/docker-piaware)

Deployment that sends data to FlightRadar24 is based on: [https://github.com/sdr-enthusiasts/docker-flightradar24](https://github.com/sdr-enthusiasts/docker-flightradar24)

Deployment that sends data to ADS-B Exchange is based on: [https://github.com/sdr-enthusiasts/docker-adsbexchange](https://github.com/sdr-enthusiasts/docker-adsbexchange)

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
