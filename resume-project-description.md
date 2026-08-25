# Resume-Ready Project Description

## Recommended project entry

### Blinkit Retail Sales Analysis | Python, Pandas, Matplotlib, Seaborn, Jupyter Notebook

Analysed **8,523 item-outlet records** to evaluate product-category contribution, fat-content mix, outlet-format performance, location-tier patterns, outlet-size distribution, and establishment-year cohorts. Cleaned and standardised inconsistent categorical labels, performed data-quality checks, calculated sales and rating KPIs, and created decision-oriented visualisations for portfolio presentation. Documented **1,463 missing item-weight values** and separated descriptive findings from causal claims.

## Resume bullet options

- Analysed **8,523 retail item-outlet records** using Python, Pandas, Matplotlib, and Seaborn to identify category, outlet-format, location-tier, and product-mix sales patterns.
- Standardised inconsistent fat-content labels, validated data types and duplicates, and documented **1,463 missing item-weight values** to improve analytical reliability.
- Built a reproducible Jupyter workflow with KPI summaries and **8 portfolio-ready visualisations** covering category ranking, outlet performance, cohort analysis, outlet size, location tier, and visibility-versus-sales relationships.
- Compared outlet formats using both total sales and average sale per record, improving interpretation by separating outlet scale from normalised performance.
- Translated exploratory results into business-facing insights, identifying the leading item category and outlet format while documenting dataset limitations and non-causal interpretation.

## Short version for a one-page resume

**Blinkit Retail Sales Analysis:** Analysed 8,523 retail records in Python using Pandas, Matplotlib, and Seaborn; standardised product labels, validated data quality, calculated sales KPIs, and developed visual analysis across categories, outlet formats, location tiers, outlet sizes, and establishment cohorts.

## Skills demonstrated

| Area | Evidence in project |
|---|---|
| Python analytics | Pandas-based loading, cleaning, grouping, reshaping, and KPI calculations |
| Data cleaning | Column-name standardisation, category-label harmonisation, missing-value profiling |
| Data visualisation | Ranked bar charts, grouped bars, line chart, scatter plot, and formatted tables |
| Business analysis | Category mix, outlet performance, location comparison, cohort interpretation |
| Data quality | Duplicate checks, negative-sales validation, numeric review, missingness documentation |
| Communication | Executive summary, section headings, chart titles, insight captions, limitations |

## Interview talking points

### What was the main business question?

The project asks which product categories and outlet formats contribute most to observed sales, and how outlet characteristics and product attributes help explain the sales mix.

### What data-cleaning step mattered most?

The `item_fat_content` field contained inconsistent labels such as `LF`, `low fat`, and `reg`. These were mapped to standard `Low Fat` and `Regular` labels before grouped comparisons so the same segment was not counted separately.

### How did you handle missing data?

The notebook reports missingness explicitly and preserves the missing item-weight values. It does not silently impute them because the correct imputation method would depend on the business context and a documented data dictionary.

### What is the main limitation?

The file is an educational item-outlet sales extract rather than a live company feed. The analysis is descriptive and does not prove causality, profitability, delivery performance, or customer behaviour.
