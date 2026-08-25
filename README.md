# Blinkit Sales Analysis — Retail EDA Case Study

A Python and Pandas exploratory analysis of item and outlet sales data. The project examines item categories, fat content, outlet type, outlet location, visibility, weight, ratings, and sales to identify practical retail performance questions.

> **Portfolio focus:** data cleaning, category standardization, grouped analysis, outlet comparison, KPI calculation, and visual storytelling.

## Business objective

Retail operators need to understand which item groups and outlet formats contribute most to sales and how product attributes relate to observed performance. This case study turns an item-outlet extract into a structured exploratory workflow.

## Verified dataset facts

The source CSV contains **8,523 records**, 12 columns, zero duplicate rows, and 1,463 empty cells [1]. After standardizing the fat-content labels, the extract produces **$1,201,681.48** in total sales [1].

| Metric | Verified result |
|---|---:|
| Records | 8,523 |
| Columns | 12 |
| Empty cells | 1,463 |
| Duplicate rows | 0 |
| Total sales | $1,201,681.48 |
| Top item type by sales | Fruits and Vegetables: $178,124.08 |
| Top outlet type by sales | Supermarket Type1 |
| Average rating | 3.97 |

## Visual evidence

![Top item groups](images/blinkit_top_item_groups.png)

The chart summarizes the leading item groups from the same sales file used by the notebook. It provides a quick visual entry point before reviewing the full exploratory workflow.

## Key business insights

Fruits and Vegetables is the leading item type by observed sales at **$178,124.08**, and Supermarket Type1 is the leading outlet type by total sales in the extract. The average rating is **3.97**, which should be interpreted alongside sales volume and missing-value patterns rather than as a standalone quality KPI.

The dataset contains 1,463 empty cells, so comparisons should document whether missing item weight, visibility, or outlet attributes are excluded, imputed, or retained. The notebook standardizes inconsistent fat-content labels such as `LF`, `reg`, and `low fat` before grouped analysis.

## Analytical workflow

The notebook profiles the CSV, reviews data types and missingness, standardizes column names, harmonizes fat-content labels, calculates total sales, and compares sales by item type and outlet characteristics. The project presentation is included as a supplementary artifact.

## Data-quality checks

The validation script checks the expected 12 columns, row count, duplicate count, non-negative sales, numeric rating conversion, standardized fat-content categories, and the documented total sales. It also reports missing cells so a reviewer can see where additional production-grade data-quality work is needed.

## Repository structure

```text
├── Blinkit Analysis.pptx
├── README.md
├── blinkit-sales-analysis.ipynb
├── blinkit_data.csv
├── images/
│   └── blinkit_top_item_groups.png
├── requirements.txt
└── scripts/
    └── validate_data.py
```

## How to reproduce

```bash
git clone https://github.com/Corvus06655/blinkit-sales-analysis.git
cd blinkit-sales-analysis
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python scripts/validate_data.py
```

Then open `blinkit-sales-analysis.ipynb` in Jupyter and run the notebook cells from top to bottom.

## Data provenance and limitations

The repository contains the CSV used for this educational retail case study. It is not a live Blinkit internal reporting feed, and the results should not be interpreted as current company performance. Because key fields contain missing values, operational decisions should use a documented data dictionary, refresh timestamp, and missingness policy.

## References

[1]: blinkit_data.csv — item-outlet sales extract.
[2]: blinkit-sales-analysis.ipynb — cleaning, standardization, and exploratory workflow.
[3]: images/blinkit_top_item_groups.png — item-group visualization generated from project data.

## Author

**Mayank Srivastava** · [GitHub](https://github.com/Corvus06655) · [LinkedIn](https://linkedin.com/in/mayank-srivastava-076020215)
