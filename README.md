# VexarDrive Fleet Analytics

## Polaris Data Scientist Intern Assignment

This project analyzes one week of fleet data from VexarDrive Technologies to build two analytical dashboards:

1. **Driver Safety & Risk Dashboard** — identifies risky vs. safer driving patterns.
2. **Vehicle Health Status Dashboard** — identifies vehicles requiring additional maintenance attention.

---

## Dataset

The dataset contains:

- 30 drivers
- 30 vehicles
- 450 trips
- 12,987 telemetry observations

### Data Sources

| Sheet | Description |
|---|---|
| Drivers | Driver master data |
| Vehicles | Vehicle master data |
| Trips | Trip-level summary statistics |
| Telemetry | Per-minute GPS, accelerometer and gyroscope data |

### Joins

```text
Telemetry.Trip_ID → Trips.Trip_ID
Trips.Driver_ID   → Drivers.Driver_ID
Trips.Vehicle_ID  → Vehicles.Vehicle_ID
