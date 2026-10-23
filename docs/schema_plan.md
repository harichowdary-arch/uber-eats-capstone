# Schema Plan — Day 1

| Dataset | Grain | Primary key | Foreign keys | Rows |
|---|---|---|---|---:|
| Customers | One synthetic customer | customer_id | — | 300 |
| Restaurants | One synthetic restaurant | restaurant_id | — | 45 |
| Orders | One order | order_id | customer_id, restaurant_id | 1,800 |
| Deliveries | One delivery record per order | delivery_id | order_id, driver_id | 1,800 |
| Drivers | One synthetic driver | driver_id | — | 70 |
| Reviews | One review | review_id | order_id, customer_id | Varies |
| Payments | One payment record per order | payment_id | order_id | 1,800 |

All row counts and values are synthetic design choices for learning.
