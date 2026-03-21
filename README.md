# GCP Real-Time Retail Streaming Pipeline

## Overview
This project demonstrates an end-to-end real-time retail streaming data pipeline built on Google Cloud Platform. A Python-based event producer generates simulated retail events and publishes them to Google Cloud Pub/Sub. An Apache Beam pipeline reads the streaming messages, parses JSON event records, and loads them into BigQuery for downstream analytics.

## Architecture
Python Producer -> Pub/Sub Topic -> Pub/Sub Subscription -> Apache Beam Pipeline -> BigQuery

## Tech Stack
- Google Cloud Platform
- Pub/Sub
- Apache Beam
- BigQuery
- Python

## Project Flow
1. A Python producer generates retail event data such as product views, add-to-cart actions, and purchases.
2. Events are published to a Pub/Sub topic.
3. Apache Beam consumes messages from the Pub/Sub subscription.
4. The pipeline parses JSON messages into structured records.
5. Parsed records are written into a BigQuery table.
6. BigQuery queries are used to analyze streamed retail data.

## BigQuery Schema
The `retail_events` table contains the following fields:

- `event_id` - unique event identifier
- `customer_id` - customer identifier
- `product_id` - product identifier
- `event_type` - type of event (`view`, `add_to_cart`, `purchase`)
- `quantity` - quantity associated with the event
- `price` - unit price of the product
- `event_time` - event timestamp

## Analytics Queries
The project includes analytical SQL queries to generate business insights from streamed event data.

### Query 1: Count events by type
This query shows the number of `view`, `add_to_cart`, and `purchase` events stored in BigQuery.

### Query 2: Top 10 products by total events
This query identifies the top products with the highest number of recorded retail events.

### Query 3: Total purchase revenue
This query calculates total revenue from purchase events using `quantity * price`.

## Business Summary
A business summary query was added to produce a one-row KPI snapshot of the streaming dataset, including:

- total events
- total views
- total add-to-cart events
- total purchases
- total purchase revenue

## Proof of Execution
The project was validated end-to-end with the following proof points:

- Pub/Sub messages successfully published and pulled from subscription
- Apache Beam pipeline successfully consumed streaming messages
- BigQuery table successfully loaded streaming event data
- Analytical queries successfully executed on stored event records

Screenshots are included in the `screenshots/` folder:
- `pubsub_messages.png`
- `bigquery_table_rows.png`
- `bigquery_schema.png`

## Repository Structure
```text
gcp-retail-streaming-pipeline/
├── docs/
├── screenshots/
├── sql/
│   ├── analytics_queries.sql
│   └── business_summary.sql
├── src/
│   ├── producer/
│   │   └── producer.py
│   └── dataflow_pipeline/
│       └── stream_to_bigquery.py
├── requirements.txt
├── .gitignore
└── README.md