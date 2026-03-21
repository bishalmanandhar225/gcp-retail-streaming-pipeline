SELECT
  COUNT(*) AS total_events,
  COUNTIF(event_type = 'view') AS total_views,
  COUNTIF(event_type = 'add_to_cart') AS total_add_to_cart,
  COUNTIF(event_type = 'purchase') AS total_purchases,
  ROUND(SUM(CASE WHEN event_type = 'purchase' THEN quantity * price ELSE 0 END), 2) AS total_purchase_revenue
FROM `gcp-retail-streaming-pipeline.retail_streaming.retail_events`;