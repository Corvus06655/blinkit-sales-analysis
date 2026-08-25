# Interview Preparation — Retail Sales & Outlet Performance Analytics

## Project overview

This project analyses an item-outlet retail sales extract and turns it into a structured business analysis. The workflow starts with data quality, standardises categorical labels, defines KPIs, compares product and outlet segments, screens numeric relationships, and ends with cautious recommendations.

## Business problem

The business wants to understand which categories and outlet formats contribute most to observed sales, whether high-volume segments are also strong on a normalized basis, how sales are distributed across location tiers and outlet sizes, and which relationships deserve further investigation.

## Dataset explanation

The file contains 8,523 records and 12 columns, including item identifiers, item type, fat content, item visibility, item weight, sales, rating, outlet type, outlet size, outlet location tier, outlet identifier, and outlet establishment year. There are 1,559 unique item identifiers and 10 unique outlet identifiers in the extract.

## Data-cleaning decisions

Column names were trimmed, converted to lowercase, and standardised with underscores so that the analysis uses stable field names. Fat-content labels were harmonised because `LF`, `low fat`, and `Low Fat` represent the same business segment, while `reg` and `Regular` represent the same segment.

The notebook checks duplicates, missing cells, negative sales, and numeric fields. It does not impute item weight because 1,463 values are missing and the appropriate imputation method cannot be justified without additional business context. Keeping the missingness visible is more honest than creating artificial precision.

## KPI definitions

Total sales is the sum of the `sales` field across records. Average sales is the mean sales value per record. Average rating is the mean recorded rating. Category and outlet contribution are calculated as each group's total sales divided by total sales. For outlet performance, average sales per record is used as a simple normalized comparison alongside total sales.

## Why each analysis was performed

The fat-content view checks product-mix contribution. The item-category ranking identifies assortment leaders and lower-contribution groups. The outlet-format comparison separates scale from normalized performance. Location-tier and outlet-size views add operating context. Establishment year is treated as a cohort dimension. The correlation screen tests whether simple linear relationships among sales, rating, visibility, weight, and establishment year are strong enough to justify deeper investigation.

## Most important findings

Fruits and Vegetables is the leading category at 178,124.08 observed sales units. Supermarket Type1 is the total-sales leader at 787,549.89, while Supermarket Type2 has the highest average sales per record at 141.68. Tier 3 is the highest-sales location tier at 472,133.03, and Medium outlets contribute the highest sales by size at 507,895.73.

Sales has almost no linear correlation with item visibility (-0.001) or rating (0.011) in this extract. The correct interview interpretation is that these simple linear signals are weak here; they do not prove that visibility or rating is irrelevant, nor do they establish causality.

## Most difficult technical problem

The original notebook passed a two-column grouped DataFrame into `plt.pie`, which caused `ValueError: x must be 1D`. The minimal fix was to pass the intended one-dimensional `Item Visibility` series and add a descriptive title. The grouped table remains available so average item weight is not lost.

## Biggest limitation

The data does not include price, cost, margin, inventory availability, customer-level behaviour, order dates, or delivery performance. As a result, the analysis describes observed sales patterns but cannot estimate profitability, customer retention, operational causality, or current company performance.

## Business recommendations

Use Fruits and Vegetables and Supermarket Type1 as scale-focused areas for deeper review, but compare them with record counts and average sales before making efficiency claims. Use the Supermarket Type1 versus Supermarket Type2 difference as a hypothesis for operational benchmarking. Review lower-contribution categories by outlet format and location tier, and define a missing-weight policy before using weight in decisions.

## Likely interviewer questions and strong answers

### Why did you choose this dataset?

I chose it because it supports a realistic retail analytics workflow: product attributes, outlet characteristics, sales, ratings, and visibility are available in one extract. It lets me demonstrate data cleaning, grouped analysis, KPI design, visualization, and business interpretation without pretending to have unavailable customer or profit data.

### How did you handle missing values?

I profiled missingness and found 1,463 missing item-weight values. I reported them and kept the field missing rather than imputing it blindly. For any weight-based follow-up, I would agree on a business rule, test sensitivity, and document the impact.

### Why did you not impute missing weights?

The dataset does not explain whether missing weight is random, category-specific, or related to a product-entry process. A mean fill could reduce variance and create false confidence. I preferred transparent missingness until a defensible business rule is available.

### How did you validate the data?

I checked expected columns, row count, duplicate rows, missing cells, negative sales, numeric conversion, and standardised fat-content categories. The repository also includes a validation script that confirms the core dataset facts.

### Why use average sales instead of only total sales?

Total sales measures scale, but a segment can lead simply because it has more records. Average sales per record adds a normalized view. I present both rather than treating either metric as a complete efficiency measure.

### What does correlation tell you here?

It measures linear association between two numeric fields in this extract. For example, sales and visibility have a correlation of -0.001, which is effectively negligible as a simple linear signal. Correlation is useful for screening, but it does not control for confounders or prove causation.

### Why can you not claim causation?

This is observational, cross-sectional data without an experiment, controls, or a temporal design. Product mix, outlet type, pricing, availability, and selection effects could influence the observed patterns. I therefore use language such as associated with or observed in the extract.

### How did you identify underperforming segments?

I would compare total sales, average sales per record, record counts, and contribution percentage together. A low total may reflect fewer observations, so I would not label a segment underperforming until the denominator and peer comparison are clear.

### What business decision would you make from the analysis?

I would prioritize a drill-down, not an immediate allocation decision: start with category and outlet leaders, compare scale versus average performance, then investigate weaker combinations by location tier, outlet type, size, visibility, and rating. Profit and inventory fields would be needed before making a final commercial recommendation.

### What would you do with customer-level data?

I would add order frequency, repeat rate, basket size, cohort retention, customer segmentation, and date-based trends. I would also connect customer outcomes to product and outlet dimensions while protecting privacy and validating the grain of every join.
