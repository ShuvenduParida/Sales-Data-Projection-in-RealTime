DynamoDB Stream to S3 via EventBridge Pipe and Firehose

This project demonstrates how to stream DynamoDB table changes into Amazon S3 using EventBridge Pipes, Kinesis Data Firehose, and a Lambda transform function.
It includes a sample Lambda function that transforms DynamoDB NewImage records into clean JSON before storing them in S3.

🚀 Architecture
DynamoDB
Table with Streams enabled (NewImage).
EventBridge Pipe
Source: DynamoDB Stream.
Target: Kinesis Data Firehose.
Kinesis Data Firehose
Transformation Lambda (this project).
Destination: S3 bucket.
S3
Stores transformed JSON files.

🧩 Lambda Transform Function
Written in Python 3.
Accepts DynamoDB Stream records (via Firehose).
Decodes base64 → parses DynamoDB JSON types → re-encodes as JSON.
Handles strings (S), numbers (N), lists (L), maps (M), booleans (BOOL), and nulls.
Returns output in Firehose-compatible format.

📂 Repository Structure
.
├── lambda_function.py     # Main Lambda code
├── requirements.txt       # Dependencies (if any)
├── README.md              # Project documentation
└── /mock-data             # (Optional) Example DynamoDB Stream events for testing


