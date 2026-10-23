# Uber Eats Operational & Customer Intelligence System

## Objective
An educational end-to-end food-delivery analytics project using synthetic data to practice customer/restaurant segmentation, review sentiment analysis, delivery-time or tip prediction, and hourly demand forecasting.

## Day 1 contents
- Seven linked synthetic CSV datasets in `data/raw/`
- Reproducible data generator in `scripts/generate_data.py`
- Basic validation checks in `scripts/validate_data.py`
- Schema plan and data dictionary in `docs/`
- Prompt-engineering notes in `docs/`

## Setup and run
Python 3.10+ recommended.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/generate_data.py
python scripts/validate_data.py
```

Windows activation: `.venv\\Scripts\\activate`

## Data warning
All records are synthetic and do not represent real Uber Eats transactions or customers. Patterns and model outputs from these records are for training only.

## Git workflow
```bash
git init
git branch -M main
git switch -c feature/uber-eats-pipeline
git status
git add README.md .gitignore requirements.txt scripts docs data/raw
git commit -m "Initialize project and generate synthetic data"
git log -1 --oneline
```

## Next steps
Day 2 will derive customer/restaurant-level features and evaluate clustering approaches. Keep raw generated files unchanged and write later transformations into `data/processed/`.
