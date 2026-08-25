# GitHub Repos — Trend Explorer

A friendly, beginner-level data project that looks at real GitHub repositories (mostly AI/ML tools) and answers questions like *"which project is the most popular?"* and *"is this repo growing fast?"* — using nothing scarier than pandas and matplotlib.

## What's in here

| File | What it does |
|---|---|
| `cleaning_feature_engineering.ipynb` | Loads the raw data, fixes data types, splits dates from times, and adds a `repo_age_days` column |
| `visualization.ipynb` | Charts, comparisons, easy math, and a guessing game built on the cleaned data |

## What you need

- Python with `pandas` and `matplotlib` installed
- The dataset file `ml_repositories.csv` in the same folder, with these columns:
  `id`, `name`, `full_name`, `owner`, `stars`, `forks`, `open_issues`, `language`, `created_at`, `updated_at`

## How to run it

1. Open `cleaning_feature_engineering.ipynb` and run all the cells — this cleans the raw data.
2. Open `visualization.ipynb` and run all the cells — it reloads and re-cleans the data on its own, so it also works standalone.

## What you'll find inside `visualization.ipynb`

- 📊 **Charts** — top repos by stars, languages pie chart, stars vs forks (top 5 and everyone), star distribution, repos per owner, busiest repos by open issues, a creation-date timeline, and a bonus bubble chart
- 🕵️ **Detective questions** — repeat owners, oldest/newest repo, which language has the highest average stars
- ➗ **Easy math** — star-to-fork ratio, stars gained per day
- 🎮 **A guessing game** — pick which repo has more stars before it's revealed
- 📝 **A fill-in-the-blank report** — write up what you found in your own words

## Why it's built this way

No heavy feature engineering, no machine learning — just clean data, clear charts, and questions anyone can explore and explain themselves.
