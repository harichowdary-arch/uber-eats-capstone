# Prompt Engineering Notes — Day 1

## P.T.C.F. framework
- **Persona:** Data engineer supporting a food-delivery analytics training project.
- **Task:** Plan a reproducible Python generator for seven linked synthetic tables.
- **Context:** Include customer demographics, restaurant category/rating, orders, deliveries, drivers, reviews, payments, order amount, distance, preparation and delivery time, tips, timestamps, weather, traffic, and statuses. Use synthetic IDs and avoid real personal data.
- **Format:** Python script using pandas/NumPy, CSV files in `data/raw/`, plus a data dictionary and validation checks.

## Role-based prompting
A data-engineering role emphasizes table relationships, repeatability, schema consistency, and validation.

## Few-shot prompting
Example 1: `order_id=ORD00001, customer_id=CUST0001, order_amount_inr=450.00, order_status=Delivered`
Example 2: `order_id=ORD00002, customer_id=CUST0002, order_amount_inr=280.00, order_status=Cancelled`
These are format examples only, not real orders.

## Structured-output prompting
Specify exact table names, column names, types, categories, key relationships, and filenames before implementing the generator.

## Evaluation and revision
Validate row counts, unique primary keys, foreign-key integrity, missing values, valid ranges, and repeatability. Update these notes if the actual implementation differs from this plan.
