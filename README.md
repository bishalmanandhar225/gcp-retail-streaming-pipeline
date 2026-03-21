# Retail Streaming Pipeline on GCP

## Overview

This project demonstrates an **end-to-end GCP Data Engineering pipeline** that generates retail event data in real time, publishes it to **Google Cloud Pub/Sub**, processes it using **Apache Beam**, and loads it into **BigQuery** for analytics.

The pipeline automates the flow of streaming retail events from message ingestion into a structured analytics table used for downstream querying and reporting.

---

## Architecture
### Pipeline Flow
        Python Event Producer
                ↓
        Google Cloud Pub/Sub Topic
                ↓
        Google Cloud Pub/Sub Subscription
                ↓
        Apache Beam Streaming Pipeline
                ↓
        BigQuery Table (retail_events)

**Apache Beam processes the streaming events and loads them into BigQuery.**

---

## Technologies Used

| Component | Technology |
|---|---|
| Cloud Platform | Google Cloud Platform |
| Messaging | Google Cloud Pub/Sub |
| Stream Processing | Apache Beam |
| Data Warehouse | BigQuery |
| Programming Language | Python |
| Version Control | Git + GitHub |

---

## Data Design

The pipeline writes streaming retail event records into a BigQuery analytics table.

This table is used for event-level analysis and business insight generation.

---

## BigQuery Table
### retail_events

| Column | Description |
|---|---|
| event_id | Unique event identifier |
| customer_id | Customer identifier |
| product_id | Product identifier |
| event_type | Event type such as view, add_to_cart, or purchase |
| quantity | Quantity associated with the event |
| price | Product price |
| event_time | Event timestamp |

---

## Pipeline Execution Steps

1. A Python producer generates simulated retail events.
2. Events are published to a **Pub/Sub topic**.
3. A **Pub/Sub subscription** makes the messages available for consumption.
4. An **Apache Beam streaming pipeline** reads messages from the subscription.
5. JSON event records are parsed into structured rows.
6. Parsed records are written into the **BigQuery retail_events** table.
7. BigQuery queries are executed to analyze the streaming data.

---

## Processing Strategy

The current pipeline uses a **streaming ingestion approach**.

During execution, events are continuously generated, published to Pub/Sub, consumed by Apache Beam, and appended into BigQuery.

This approach was used to:

- demonstrate real-time data ingestion on GCP
- validate end-to-end streaming pipeline execution
- support downstream analytical queries on live event data

In production systems, this pattern can be extended with additional capabilities such as schema validation, dead-letter handling, windowing, enrichment, and deployment on managed Dataflow runners.

---

## Analytics Queries

The project includes analytical SQL queries to generate business insights from streamed retail data.

Examples include:

- count of events by event type
- top 10 products by total events
- total purchase revenue
- business summary KPI query

---

## Repository Structure
src/producer/ Python producer for retail event generation  
src/dataflow_pipeline/ Apache Beam streaming pipeline  
sql/ BigQuery analytical SQL queries  
docs/ Project documentation  
screenshots/ Pipeline execution screenshots  

---

## Result
The pipeline successfully ingests, processes, and stores retail streaming event data in **BigQuery**, demonstrating a complete **real-time GCP data engineering workflow** using Pub/Sub, Apache Beam, and BigQuery.

---

## Author

**Bishal Manandhar**