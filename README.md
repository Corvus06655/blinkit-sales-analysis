# Retail Sales & Outlet Performance Analytics

A portfolio-ready **Python and Jupyter Notebook case study** that examines item-level retail sales across product categories, fat-content segments, outlet formats, location tiers, outlet sizes, and establishment-year cohorts.

The project is intentionally framed as a business analysis rather than a collection of charts. It moves from data quality and KPI definitions to product mix, outlet performance, normalized comparisons, correlation screening, and management-oriented recommendations.

## Business Problem

Retail teams need to understand which product categories and outlet formats contribute most to observed sales, whether high-volume segments are also efficient on a per-record basis, and where further investigation may be worthwhile. This project converts a raw item-outlet extract into a reproducible analytical workflow for those questions.

## Objectives

The analysis is designed to answer five practical questions:

1. Which item categories and fat-content segments contribute most to observed sales?
2. Which outlet formats, sizes, and location tiers lead on total sales?
3. Do normalized measures tell a different story from total sales alone?
4. Do visibility, rating, weight, or establishment year show linear associations with sales?
5. What data-quality limitations should management consider before acting on the findings?

## Dataset

The repository contains an educational item-outlet sales extract with **8,523 records** and **12 columns**. It includes item attributes, outlet characteristics, sales, and ratings. The file is not a live internal Blinkit reporting feed; therefore, findings are descriptive and should not be interpreted as current company performance.

| Metric | Verified result |
|---|---:|
| Records | 8,523 |
| Columns | 12 |
| Unique item identifiers | 1,559 |
| Unique outlet identifiers | 10 |
| Duplicate rows | 0 |
| Missing cells | 1,463 |
| Missing item-weight values | 1,463 |
| Negative sales records | 0 |
| Total sales | 1,201,681.48 dataset units |
| Average sales per record | 140.99 |
| Median sales per record | 143.01 |
| Average rating | 3.97 / 5 |

## Tools and Technologies

Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook, Git, and GitHub.

## Data Cleaning and Validation

The notebook standardises column names by trimming whitespace, replacing spaces with underscores, and converting labels to lowercase. The `item_fat_content` field is harmonised so that `LF` and `low fat` map to `Low Fat`, while `reg` maps to `Regular`.

The quality review checks row and column counts, duplicate records, missing values, numeric ranges, negative sales, and available data types. Missing item-weight values are reported rather than silently imputed because the correct treatment depends on the business context and a documented data dictionary.

## KPI Framework

The notebook defines total sales as the sum of the `sales` field and average sales as the mean sales value per item-outlet record. It also reports average rating, record count, unique item identifiers, unique outlets, category contribution, outlet contribution, median sales, and standard deviation where relevant.

For outlet comparisons, the project separates **total sales** from **average sales per record**. This avoids treating a segment as efficient merely because it has more observations in the extract.

## Analysis Covered

The original exploratory flow is preserved and expanded with concise explanatory text above the visual sections. It includes:

- Product-attribute comparison by fat content.
- Sales mix by standardised fat-content segment.
- Ranked sales by item category.
- Fat-content mix by outlet location tier.
- Sales by outlet establishment year as a cohort view.
- Sales by outlet size and location tier.
- Outlet-format comparison using total sales and average sales per record.
- Category contribution and cumulative-share analysis.
- Correlation screening across sales, rating, visibility, weight, and establishment year.

## Key Findings

Fruits and Vegetables is the leading category by observed sales at **178,124.08**, closely followed by Snack Foods at **175,433.92**. Supermarket Type1 is the largest outlet format by total observed sales at **787,549.89**, but Supermarket Type2 has the highest average sales per record at **141.68** compared with **141.21** for Supermarket Type1.

Tier 3 contributes the highest observed sales among location tiers at **472,133.03**, while Medium outlets contribute the highest observed sales among outlet-size groups at **507,895.73**. The cleaned fat-content totals are **776,319.68 for Low Fat** and **425,361.80 for Regular**.

The correlation screen shows almost no linear association between sales and item visibility (**-0.001**) or sales and rating (**0.011**) in this extract. These results are screening signals only; they do not establish causality and do not rule out non-linear or confounded relationships.

## Business Recommendations

Management should use the leading category and outlet-format results as prioritisation signals, then drill down by outlet type, location tier, size, visibility, and rating before making assortment or promotion decisions. Supermarket Type1 is a scale leader, while Supermarket Type2 is the normalized average-sales leader; this difference is a useful starting point for operational comparison rather than a reason to declare one format universally best.

Lower-contribution categories should be reviewed alongside their record counts and outlet mix. Any action involving item weight should first define a missing-value policy because 1,463 weight values are unavailable. Revenue should not be interpreted as profit because the dataset does not include cost or margin fields.

## Limitations

The extract does not contain customer-level behaviour, orders over time, delivery performance, price, cost, profit, inventory availability, or experimental controls. Outlet establishment year is used as a cohort dimension, not as a daily or monthly time series. Correlations are descriptive and cannot prove causation. The project therefore supports prioritisation and hypothesis generation, not final commercial decisions.

## Repository Structure

```text
├── README.md
├── blinkit-sales-analysis.ipynb
├── blinkit_data.csv
├── Blinkit_Retail_Sales_Analysis.pptx
├── blinkit_top_item_groups.png
├── requirements.txt
└── scripts/
    └── validate_data.py
```

## How to Run

```bash
git clone https://github.com/Corvus06655/blinkit-sales-analysis.git
cd blinkit-sales-analysis
python -m venv .venv

# Windows
.venv\\Scripts\\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
python scripts/validate_data.py
```

Open `blinkit-sales-analysis.ipynb` in Jupyter and run the cells from top to bottom.

## Screenshots and Presentation

The repository includes `Blinkit_Retail_Sales_Analysis.pptx`, a duplicate-free requirements presentation with clear definitions for every chart requirement. The notebook's existing chart image is retained at `blinkit_top_item_groups.png`; the notebook itself contains the full exploratory workflow and explanatory text above each graph section.

## Future Improvements

Future versions could add a documented data dictionary, outlet-level unique-item counts, a profit or margin field, customer/order-level time series, statistical significance testing for group comparisons, and an interactive dashboard with filters once the required business fields are available.

## Author

**Mayank Srivastava** · [GitHub](https://github.com/Corvus06655) · [LinkedIn](https://linkedin.com/in/mayank-srivastava-076020215)
