# Data Dictionary — Day 1

All records are synthetic and generated for learning. They are not actual Uber Eats records.

## customers.csv

Purpose: one row represents a customer.

| Column | Data type | Description | Example |
|---|---|---|---|
| `customer_id` | object | Unique synthetic customer identifier | CUST0001 |
| `age` | int64 | Customer age in years | 22 |
| `gender` | object | Synthetic demographic category | Male |
| `city` | object | Customer city | Hyderabad |
| `signup_date` | object | Date the customer account was created | 2026-02-16 |

## restaurants.csv

Purpose: one row represents a restaurant.

| Column | Data type | Description | Example |
|---|---|---|---|
| `restaurant_id` | object | Unique synthetic restaurant identifier | REST001 |
| `restaurant_name` | object | Generated restaurant display name | Fresh Bites 01 |
| `category` | object | Restaurant food category | Desserts |
| `city` | object | Restaurant city | Chennai |
| `restaurant_rating` | float64 | Restaurant rating on a 1–5 scale | 3.9 |
| `avg_prep_time_minutes` | int64 | Typical preparation time in minutes | 29 |

## orders.csv

Purpose: one row represents a order.

| Column | Data type | Description | Example |
|---|---|---|---|
| `order_id` | object | Unique synthetic order identifier | ORD00001 |
| `customer_id` | object | Customer who placed the order | CUST0103 |
| `restaurant_id` | object | Restaurant receiving the order | REST012 |
| `order_timestamp` | object | Timestamp when order was placed | 2026-01-03 04:20:00 |
| `order_amount_inr` | float64 | Order amount in Indian rupees | 438.89 |
| `number_of_items` | int64 | Number of items in the order | 8 |
| `preparation_time_minutes` | int64 | Preparation-time estimate in minutes | 14 |
| `order_status` | object | Order outcome category | Delivered |

## deliveries.csv

Purpose: one row represents a delivery record.

| Column | Data type | Description | Example |
|---|---|---|---|
| `delivery_id` | object | Unique synthetic delivery record identifier | DEL00001 |
| `order_id` | object | Order associated with this delivery | ORD00001 |
| `driver_id` | object | Assigned synthetic driver identifier | DRV029 |
| `delivery_distance_km` | float64 | Estimated delivery distance in kilometres | 3.28 |
| `delivery_time_minutes` | float64 | Simulated delivery duration in minutes; missing for non-completed deliveries | 40.0 |
| `weather` | object | Simulated weather condition | Rain |
| `traffic_condition` | object | Simulated traffic level | Low |
| `tip_amount_inr` | float64 | Simulated tip in Indian rupees | 0.0 |
| `delivery_status` | object | Whether delivery was completed | Completed |

## drivers.csv

Purpose: one row represents a driver.

| Column | Data type | Description | Example |
|---|---|---|---|
| `driver_id` | object | Unique synthetic driver identifier | DRV001 |
| `vehicle_type` | object | Driver vehicle category | Scooter |
| `experience_months` | int64 | Driver experience in months | 22 |
| `driver_rating` | float64 | Driver rating on a 1–5 scale | 4.3 |

## reviews.csv

Purpose: one row represents a customer review.

| Column | Data type | Description | Example |
|---|---|---|---|
| `review_id` | object | Unique synthetic review identifier | REV00001 |
| `order_id` | object | Reviewed order identifier | ORD00001 |
| `customer_id` | object | Customer who submitted review | CUST0103 |
| `rating` | int64 | Review rating on a 1–5 scale | 5 |
| `review_text` | object | Synthetic customer feedback text | Fresh food and accurate order. |
| `review_timestamp` | object | Timestamp when review was recorded | 2026-01-04 04:20:00 |

## payments.csv

Purpose: one row represents a payment record.

| Column | Data type | Description | Example |
|---|---|---|---|
| `payment_id` | object | Unique synthetic payment identifier | PAY00001 |
| `order_id` | object | Order associated with payment | ORD00001 |
| `payment_method` | object | Simulated payment method | Card |
| `payment_amount_inr` | float64 | Payment amount in Indian rupees | 438.89 |
| `payment_status` | object | Payment outcome category | Paid |

## Relationships

- `orders.customer_id` → `customers.customer_id`
- `orders.restaurant_id` → `restaurants.restaurant_id`
- `deliveries.order_id` → `orders.order_id`
- `deliveries.driver_id` → `drivers.driver_id`
- `reviews.order_id` → `orders.order_id`; `reviews.customer_id` → `customers.customer_id`
- `payments.order_id` → `orders.order_id`

## Limitations

Values are simulated from chosen distributions and simple rules. They are useful for practicing data workflows but cannot establish actual business performance or causal relationships.
