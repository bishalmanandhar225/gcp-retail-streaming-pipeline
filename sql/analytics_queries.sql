-- Query 1: Count events by event type
SELECT
  event_type,
  COUNT(*) AS total_events
FROM `gcp-retail-streaming-pipeline.retail_streaming.retail_events`
GROUP BY event_type
ORDER BY total_events DESC;

-- Query 2: Top 10 products by total events
SELECT
  product_id,
  COUNT(*) AS total_events
FROM `gcp-retail-streaming-pipeline.retail_streaming.retail_events`
GROUP BY product_id
ORDER BY total_events DESC
LIMIT 10;

-- Query 3: Total purchase revenue
SELECT
  SUM(quantity * price) AS total_purchase_revenue
FROM `gcp-retail-streaming-pipeline.retail_streaming.retail_events`
WHERE event_type = 'purchase';