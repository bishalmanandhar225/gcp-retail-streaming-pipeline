# GCP Real-Time Retail Streaming Pipeline

## Objective
Build an end-to-end streaming data pipeline using GCP services.

## Architecture
Event Generator -> Pub/Sub -> Dataflow -> BigQuery -> Dashboard

## Tech Stack
- GCP
- Pub/Sub
- Dataflow (Apache Beam)
- BigQuery
- Python

## Project Status

### Completed
- Created Pub/Sub topic and subscription
- Built Python event producer
- Built Apache Beam pipeline to read from Pub/Sub and load into BigQuery
- Created BigQuery dataset and table
- Validated end-to-end streaming flow with live data

### Proof
- Pub/Sub messages screenshot
- BigQuery loaded rows screenshot
- BigQuery schema screenshot