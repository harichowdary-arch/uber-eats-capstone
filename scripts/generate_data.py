"""Generate reproducible synthetic Uber Eats-style data for Day 1."""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "raw"
OUT.mkdir(parents=True, exist_ok=True)
SEED = 42
rng = np.random.default_rng(SEED)

# See docs/schema_plan.md for row counts and relationships.
N_CUSTOMERS, N_RESTAURANTS, N_DRIVERS, N_ORDERS = 300, 45, 70, 1800
CITIES = ["Hyderabad", "Bengaluru", "Chennai", "Pune", "Mumbai"]
CATEGORIES = ["Indian", "Pizza", "Burgers", "Chinese", "Healthy", "Desserts", "Cafe"]

def save(name, frame):
    frame.to_csv(OUT / f"{name}.csv", index=False)
    print(f"{name}.csv: {frame.shape[0]} rows, {frame.shape[1]} columns")

def main():
    customers = pd.DataFrame({
        "customer_id": [f"CUST{i:04d}" for i in range(1, N_CUSTOMERS + 1)],
        "age": rng.integers(18, 66, N_CUSTOMERS),
        "gender": rng.choice(["Female", "Male", "Non-binary", "Prefer not to say"], N_CUSTOMERS),
        "city": rng.choice(CITIES, N_CUSTOMERS),
        "signup_date": (pd.Timestamp("2023-01-01") + pd.to_timedelta(
            rng.integers(0, 1300, N_CUSTOMERS), unit="D")).strftime("%Y-%m-%d"),
    })
    restaurants = pd.DataFrame({
        "restaurant_id": [f"REST{i:03d}" for i in range(1, N_RESTAURANTS + 1)],
        "restaurant_name": [f"Restaurant {i:03d}" for i in range(1, N_RESTAURANTS + 1)],
        "category": rng.choice(CATEGORIES, N_RESTAURANTS),
        "city": rng.choice(CITIES, N_RESTAURANTS),
        "restaurant_rating": np.round(np.clip(rng.normal(4.0, .55, N_RESTAURANTS), 2.2, 5), 1),
        "avg_prep_time_minutes": rng.integers(8, 36, N_RESTAURANTS),
    })
    drivers = pd.DataFrame({
        "driver_id": [f"DRV{i:03d}" for i in range(1, N_DRIVERS + 1)],
        "vehicle_type": rng.choice(["Bike", "Scooter", "Bicycle", "Car"], N_DRIVERS),
        "experience_months": rng.integers(1, 73, N_DRIVERS),
        "driver_rating": np.round(np.clip(rng.normal(4.2, .4, N_DRIVERS), 2.5, 5), 1),
    })

    order_ids = [f"ORD{i:05d}" for i in range(1, N_ORDERS + 1)]
    customer_ids = rng.choice(customers["customer_id"], N_ORDERS)
    restaurant_ids = rng.choice(restaurants["restaurant_id"], N_ORDERS)
    restaurant_lookup = restaurants.set_index("restaurant_id")
    prep = np.array([restaurant_lookup.loc[x, "avg_prep_time_minutes"] for x in restaurant_ids])
    timestamps = pd.Timestamp("2026-01-01") + pd.to_timedelta(
        rng.integers(0, 90 * 24 * 60, N_ORDERS), unit="m")
    amounts = np.round(np.clip(rng.gamma(2.4, 220, N_ORDERS), 90, 2200), 2)
    statuses = rng.choice(["Delivered", "Cancelled", "Failed"], N_ORDERS, p=[.91, .065, .025])
    orders = pd.DataFrame({
        "order_id": order_ids, "customer_id": customer_ids, "restaurant_id": restaurant_ids,
        "order_timestamp": timestamps.strftime("%Y-%m-%d %H:%M:%S"),
        "order_amount_inr": amounts, "number_of_items": rng.integers(1, 9, N_ORDERS),
        "preparation_time_minutes": prep, "order_status": statuses,
    })

    delivery_rows, review_rows, payment_rows = [], [], []
    positive = ["Food arrived hot and tasted great.", "Quick delivery and friendly driver.",
                "Good value and carefully packed.", "Fresh food and accurate order."]
    negative = ["Delivery was late and the food was cold.", "Order was missing an item.",
                "Packaging was damaged and support was slow.", "Food quality was disappointing."]
    neutral = ["Food was okay, delivery was average.", "Order was as expected.",
               "Taste was fine but portion was small."]
    for i, order_id in enumerate(order_ids):
        delivered = statuses[i] == "Delivered"
        distance = round(float(np.clip(rng.gamma(2.1, 2.0), .4, 18)), 2)
        weather = rng.choice(["Clear", "Rain", "Cloudy", "Hot"], p=[.48, .16, .24, .12])
        traffic = rng.choice(["Low", "Moderate", "High"], p=[.28, .47, .25])
        delivery_time = int(max(10, prep[i] + distance * 4 +
                                (10 if traffic == "High" else 4 if traffic == "Moderate" else 0) +
                                (8 if weather == "Rain" else 0) + rng.normal(8, 5)))
        tip = round(float(np.clip(amounts[i] * rng.choice(
            [0, .03, .05, .08, .1], p=[.22, .18, .28, .22, .10]), 0, 250)), 2)
        delivery_rows.append({
            "delivery_id": f"DEL{i+1:05d}", "order_id": order_id,
            "driver_id": rng.choice(drivers["driver_id"]), "delivery_distance_km": distance,
            "delivery_time_minutes": delivery_time if delivered else np.nan,
            "weather": weather, "traffic_condition": traffic,
            "tip_amount_inr": tip if delivered else 0,
            "delivery_status": "Completed" if delivered else "Not completed",
        })
        if delivered and rng.random() < .72:
            rating = int(np.clip(round(rng.normal(4.1 - (.8 if delivery_time > 50 else 0), .9)), 1, 5))
            review_text = rng.choice(positive if rating >= 4 else negative if rating <= 2 else neutral)
            review_rows.append({
                "review_id": f"REV{len(review_rows)+1:05d}", "order_id": order_id,
                "customer_id": customer_ids[i], "rating": rating, "review_text": review_text,
                "review_timestamp": (timestamps[i] + pd.Timedelta(days=int(rng.integers(0, 5)))).strftime("%Y-%m-%d %H:%M:%S"),
            })
        pay_status = ("Refunded" if statuses[i] == "Cancelled" and rng.random() < .65
                      else "Paid" if delivered else rng.choice(["Pending", "Refunded"]))
        payment_rows.append({
            "payment_id": f"PAY{i+1:05d}", "order_id": order_id,
            "payment_method": rng.choice(["UPI", "Card", "Cash", "Wallet"]),
            "payment_amount_inr": amounts[i], "payment_status": pay_status,
        })

    tables = {
        "customers": customers, "restaurants": restaurants, "orders": orders,
        "deliveries": pd.DataFrame(delivery_rows), "drivers": drivers,
        "reviews": pd.DataFrame(review_rows), "payments": pd.DataFrame(payment_rows),
    }
    for name, frame in tables.items():
        save(name, frame)
    print("\nGeneration complete. All records are synthetic.")

if __name__ == "__main__":
    main()
