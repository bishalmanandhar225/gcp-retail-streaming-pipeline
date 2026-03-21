import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import json


class ParseMessage(beam.DoFn):
    def process(self, element):
        row = json.loads(element.decode("utf-8"))
        yield row


def run():
    project_id = "gcp-retail-streaming-pipeline1"
    subscription = f"projects/{project_id}/subscriptions/retail-events-sub"
    table_spec = f"{project_id}:retail_streaming.retail_events"

    pipeline_options = PipelineOptions(
        streaming=True,s
        save_main_session=True
    )

    with beam.Pipeline(options=pipeline_options) as pipeline:
        (
            pipeline
            | "Read from PubSub" >> beam.io.ReadFromPubSub(subscription=subscription)
            | "Parse JSON" >> beam.ParDo(ParseMessage())
            | "Write to BigQuery" >> beam.io.WriteToBigQuery(
                table=table_spec,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
                create_disposition=beam.io.BigQueryDisposition.CREATE_NEVER
            )
        )


if __name__ == "__main__":
    run()