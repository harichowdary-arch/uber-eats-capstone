# Day 7 — Run, Finalize and Git Guide

## 1. Where to place the files

Copy these into your existing repository. Do not replace the repository folder or `.git` folder.

- `notebooks/day7_finalization_validation.ipynb` → existing `notebooks/` folder.
- `presentation/uber_eats_final_presentation.pptx` → create/use `presentation/` folder at project root.
- `docs/DAY7_RUN_AND_GIT_GUIDE.md` → existing `docs/` folder.

Expected final paths:
- `notebooks/day7_finalization_validation.ipynb`
- `presentation/uber_eats_final_presentation.pptx`
- `docs/DAY7_RUN_AND_GIT_GUIDE.md`

## 2. Install dependencies

Open a terminal at the project root and activate your existing virtual environment:

```bash
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pandas numpy matplotlib scikit-learn statsmodels joblib jupyter ipykernel
```

Prophet is optional. Install only if you plan to run the Prophet section in Day 5:
```bash
python -m pip install prophet
```

## 3. Run the notebooks in order

In VS Code, open the project folder and select the `.venv` Python interpreter/kernel.

Run these notebooks from top to bottom:
1. `customer_segmentation.ipynb`
2. `restaurant_segmentation.ipynb`
3. `day3_customer_feedback_nlp.ipynb`
4. `day4_delivery_time_prediction.ipynb`
5. `day5_hourly_demand_forecasting.ipynb`
6. `day6_end_to_end_ml_pipeline_business_insights.ipynb`
7. `day7_finalization_validation.ipynb`

If a notebook has a different filename in your repository, use the actual filename. Run the notebooks from the project root or with the notebook opened from `notebooks/`; the notebooks use relative project-root detection.

The Day 7 notebook checks for expected files and saved evaluation evidence. It does not train models or fabricate missing scores. Review any `Missing` / `Not found` items and rerun the corresponding notebook.

## 4. Complete the presentation

Open `presentation/uber_eats_final_presentation.pptx`.

Replace the prompts/placeholders with actual values from your generated outputs:
- Dataset row counts: `data/raw/*.csv`
- Cluster counts and profiles: segmentation notebook outputs
- NLP evaluation: Day 3 metrics/confusion matrix
- Regression best model and MAE/RMSE/R²: `outputs/delivery_time_prediction/`
- Forecast comparison and 24-hour forecast: `outputs/demand_forecasting/`

Do not claim Prophet was used unless its model and evaluation results exist. Clearly say that the data is synthetic and the results are for demonstration.

Suggested timing (15–20 minutes):
- Business problem + dataset: 2–3 min
- Data preparation + segmentation: 4 min
- NLP + regression: 4–5 min
- Forecasting: 2–3 min
- Business impact, limitations, future scope: 3–4 min
- Questions: remaining time

## 5. Git workflow — safe feature branch first

First save and review all changes on the feature branch:

```bash
git status
git switch feature/uber-eats-pipeline
git pull origin feature/uber-eats-pipeline
git add -A
git status
git diff --cached --stat
```

Check that `.venv/`, `.env`, credentials, `__pycache__/`, `.ipynb_checkpoints/`, and large generated files are not staged. If needed, unstage a file:
```bash
git restore --staged path/to/file
```

Then commit and push:
```bash
git commit -m "Finalize Day 7 capstone deliverables"
git push origin feature/uber-eats-pipeline
```

## 6. Merge feature branch into main

Only after the feature branch is pushed and reviewed:

```bash
git switch main
git pull origin main
git merge feature/uber-eats-pipeline
```

If there are no conflicts, push the updated main branch:
```bash
git push origin main
```

If Git reports conflicts, do not blindly overwrite files. Open each conflicted file, resolve the conflict markers, then:
```bash
git add <resolved-file>
git commit
git push origin main
```

If `main` is protected and direct push is rejected, create a Pull Request from `feature/uber-eats-pipeline` into `main` on GitHub and merge it through the repository's normal review process.

## 7. Final verification

```bash
git status
git log --oneline -5
```

Confirm the GitHub repository contains the Day 7 notebook, presentation and updated documentation. A clean `git status` means there are no uncommitted changes.
