"""Validate generated Day 1 CSV files and key relationships."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw"
FILES = ["customers", "restaurants", "orders", "deliveries", "drivers", "reviews", "payments"]

def main():
    tables = {}
    for name in FILES:
        path = DATA / f"{name}.csv"
        if not path.exists():
            raise FileNotFoundError(f"Missing {path}. Run python scripts/generate_data.py first.")
        tables[name] = pd.read_csv(path)
        print(f"{name}: {tables[name].shape[0]} rows x {tables[name].shape[1]} columns")

    primary_keys = {
        "customers": "customer_id", "restaurants": "restaurant_id", "orders": "order_id",
        "deliveries": "delivery_id", "drivers": "driver_id", "reviews": "review_id",
        "payments": "payment_id",
    }
    for table, key in primary_keys.items():
        assert tables[table][key].notna().all(), f"Null primary key in {table}"
        assert tables[table][key].is_unique, f"Duplicate primary key in {table}"

    checks = [
        ("orders", "customer_id", "customers", "customer_id"),
        ("orders", "restaurant_id", "restaurants", "restaurant_id"),
        ("deliveries", "order_id", "orders", "order_id"),
        ("deliveries", "driver_id", "drivers", "driver_id"),
        ("reviews", "order_id", "orders", "order_id"),
        ("reviews", "customer_id", "customers", "customer_id"),
        ("payments", "order_id", "orders", "order_id"),
    ]
    for child, col, parent, parent_col in checks:
        invalid = ~tables[child][col].isin(tables[parent][parent_col])
        assert not invalid.any(), f"Invalid foreign key: {child}.{col}"
    assert tables["restaurants"]["restaurant_rating"].between(1, 5).all()
    assert tables["drivers"]["driver_rating"].between(1, 5).all()
    assert tables["reviews"]["rating"].between(1, 5).all()
    assert tables["orders"]["order_amount_inr"].ge(0).all()
    assert tables["deliveries"]["delivery_distance_km"].gt(0).all()
    print("\nPASS: primary keys, foreign keys, and basic value ranges validated.")

if __name__ == "__main__":
    main()
