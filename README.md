# VexarDrive Fleet Analytics

## Polaris Data Scientist Intern Assignment

This project analyzes one week of fleet data from VexarDrive Technologies to build two analytical dashboards:

1. **Driver Safety & Risk Dashboard** — identifies risky vs. safer driving patterns.
2. **Vehicle Health Status Dashboard** — identifies vehicles requiring additional maintenance attention.

---

## Dataset Overview

The dataset contains:

- **30 drivers**
- **30 vehicles**
- **450 trips**
- **12,987 telemetry observations**

### Data Sources

| Sheet | Description |
|---|---|
| Drivers | Driver master data |
| Vehicles | Vehicle master data |
| Trips | Trip-level summary statistics |
| Telemetry | Per-minute GPS, accelerometer and gyroscope data |

### How the Sheets Join

```text
Telemetry.Trip_ID → Trips.Trip_ID
Trips.Driver_ID   → Drivers.Driver_ID
Trips.Vehicle_ID  → Vehicles.Vehicle_ID
```

The resulting master dataset contains **12,987 telemetry observations and 38 columns**. No missing values were introduced by the joins, and no duplicate columns were present.

---

# Driver Safety & Risk Analysis

Driver behaviour was evaluated using four driving-event types:

- Overspeed
- Harsh acceleration
- Harsh braking
- Aggressive lateral movement

Event counts were normalized by telemetry exposure to create comparable event rates across drivers.

The event rates were then converted into **fleet-relative percentile scores**, where a higher percentile represents higher relative frequency of the corresponding risky behaviour.

### Driver Risk Score

The composite risk score was calculated as:

```text
Risk Score =
0.35 × Overspeed Score
+ 0.25 × Braking Score
+ 0.20 × Acceleration Score
+ 0.20 × Lateral Score
```

Overspeed received the largest weight because excessive speed is a particularly important safety indicator in the context of the available telemetry. Braking, acceleration and lateral behaviour were given lower but meaningful weights.

The final score ranges approximately from 0–100 and represents **relative risk within this fleet**.

### Risk Categories

| Risk Score | Category |
|---:|---|
| < 40 | Lower Risk |
| 40–70 | Moderate Risk |
| > 70 | Higher Risk |

These thresholds are analytical assumptions intended to provide actionable fleet segmentation rather than calibrated accident probabilities.

### Driver Risk Results

The fleet contained:

- **7 Higher Risk drivers**
- **12 Moderate Risk drivers**
- **11 Lower Risk drivers**

The highest-ranked driver was **D24**, with a risk score of **91.9**.

> The risk score is a relative fleet-ranking indicator and should not be interpreted as an accident probability.

---

# Vehicle Health & Maintenance Analysis

Vehicle health was evaluated using four indicators:

- Sensor anomaly rate
- Starting odometer
- Days since service
- Vehicle age

Each metric was converted into a **0–100 fleet-relative percentile score**. A higher percentile indicates greater relative maintenance attention.

### Maintenance Attention Score

The composite score was calculated as:

```text
Maintenance Attention Score =
0.50 × Sensor Score
+ 0.20 × Odometer Score
+ 0.15 × Service Score
+ 0.15 × Age Score
```

Sensor anomaly rate received the largest weight because irregular sensor signatures are the most direct available indicator of abnormal vehicle behaviour.

Odometer, service recency and vehicle age were included as supporting indicators because higher usage, longer time since service and older vehicles can increase maintenance requirements.

### Maintenance Categories

| Attention Score | Category |
|---:|---|
| < 40 | Lower Attention |
| 40–70 | Monitor |
| > 70 | Higher Attention |

These thresholds are analytical assumptions designed to prioritize vehicles for inspection.

### Vehicle Health Results

The fleet contained:

- **7 Higher Attention vehicles**
- **8 Monitor vehicles**
- **15 Lower Attention vehicles**

**V02** had the highest maintenance-attention score at **94.8** and the highest observed sensor-anomaly rate at approximately **9.26%**.

> A high maintenance-attention score indicates that a vehicle should be prioritized for inspection or monitoring. It does not confirm mechanical failure.

---

# Sensor Anomaly Analysis

Sensor anomalies were identified using fleet-relative thresholds across the accelerometer and gyroscope measurements.

The telemetry dataset contained:

- **12,987 total telemetry observations**
- **620 observations with at least one sensor anomaly**
- **131 Gyro X anomalies**
- **131 Gyro Y anomalies**
- **130 Gyro Z anomalies**
- **132 Accel X anomalies**
- **131 Accel Y anomalies**
- **130 Accel Z anomalies**

The anomaly analysis is intended to identify unusual sensor signatures that may warrant further investigation.

An anomaly does not automatically indicate a mechanical fault because unusual readings can also result from driving conditions, sensor noise, mounting issues or other factors.

---

# Key Findings

## Highest-Risk Drivers

| Rank | Driver ID | Risk Score |
|---:|---|---:|
| 1 | D24 | 91.9 |
| 2 | D03 | 90.5 |
| 3 | D19 | 88.8 |
| 4 | D14 | 88.6 |
| 5 | D06 | 88.3 |
| 6 | D23 | 87.2 |
| 7 | D12 | 83.4 |

These drivers showed the highest combined relative rates of overspeeding, harsh braking, harsh acceleration and aggressive lateral behaviour.

## Highest-Attention Vehicles

| Rank | Vehicle ID | Attention Score |
|---:|---|---:|
| 1 | V02 | 94.8 |
| 2 | V12 | 86.7 |
| 3 | V19 | 81.6 |
| 4 | V01 | 78.3 |
| 5 | V23 | 77.9 |
| 6 | V10 | 77.7 |
| 7 | V24 | 73.6 |

---

# Dashboard Outputs

Two dashboards were developed from the analysis.

### Driver Safety & Risk Dashboard

The dashboard provides:

- Total driver count
- Higher / Moderate / Lower risk distribution
- Average fleet risk score
- Top risky drivers
- Risk score vs. overspeed rate
- Behaviour-rate comparison across top risky drivers

### Vehicle Health Status Dashboard

The dashboard provides:

- Vehicle maintenance-attention rankings
- Sensor anomaly rates
- Maintenance attention vs. vehicle usage
- Top vehicles requiring maintenance attention
- Vehicle maintenance categories

Dashboard images are included in the repository under the `dashboards/` directory.

---

# Data Quality & Validation

The analysis included validation of:

- Dataset dimensions
- Missing values
- Duplicate columns
- Join integrity
- Unique Driver IDs
- Unique Vehicle IDs
- Unique Trip IDs
- Sensor distributions
- Sensor percentiles
- Event counts and rates

Final master dataset:

```text
Rows:    12,987
Columns: 38
Missing values introduced by joins: 0
Duplicate columns: 0
Drivers: 30
Vehicles: 30
Trips: 450
```

---

# Methodology Assumptions

The scoring framework uses relative fleet percentiles because the supplied dataset does not provide externally validated safety or maintenance thresholds.

The main assumptions are:

1. Higher risky-event rates indicate greater relative driver risk.
2. Higher sensor anomaly rates indicate greater relative vehicle-health concern.
3. Higher odometer readings represent greater cumulative vehicle usage.
4. More days since service indicate greater potential maintenance attention.
5. Older vehicles may require greater maintenance attention.
6. The selected weights reflect analytical judgement and should be validated against historical outcomes before production use.
7. The score thresholds are designed for fleet prioritization rather than diagnosis or prediction.

---

# Additional Applications

The dataset could be extended to support:

- Predictive maintenance
- Driver coaching and safety training
- Fleet utilization analysis
- Vehicle replacement planning
- Sensor-quality monitoring
- Route and operational efficiency analysis
- Accident-risk modelling after linking historical incident data
- Fuel or energy efficiency analysis
- Driver performance monitoring
- Fleet-level maintenance planning

---

# Limitations

- Scores are relative to the supplied fleet and may change with a different fleet population.
- Driver risk scores are not calibrated accident probabilities.
- Sensor anomalies do not confirm mechanical failures.
- Odometer, vehicle age and service recency are proxy indicators.
- The selected score weights and thresholds are analytical assumptions.
- The dataset represents one week of activity and may not capture longer-term behaviour.
- Larger historical datasets and domain validation would be required before production deployment.

---

# Repository Structure

```text
VexarDrive-Fleet-Analytics/
│
├── VexarDrive_Analysis.ipynb
│
├── dashboard/
│   ├── driver_safety_dashboard.png
│   └── vehicle_health_dashboard.png
│
├── outputs/
│   ├── driver_ranking.csv
│   ├── driver_behavior_summary.csv
│   ├── event_summary.csv
│   ├── vehicle_health_ranking.csv
│   └── vehicle_sensor_anomalies.csv
│
└── report/
    └── VexarDrive_Technical_Report.pdf
```

---

# Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Google Colab / Jupyter Notebook
