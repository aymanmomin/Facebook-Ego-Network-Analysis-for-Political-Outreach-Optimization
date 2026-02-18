# Project Documentation

This directory contains detailed technical documentation for the Facebook Ego Network Analysis project.

## Available Documents

### [Technical Report](technical-report.md)
Comprehensive analysis report including:
- Abstract and research questions
- Detailed methodology and iterative changes
- Complete results with visualizations
- Discussion of structural vs. social targeting
- Limitations and conclusions
- References and ethics statement

**Note**: After reorganizing files (see [REORGANIZATION_GUIDE.md](../REORGANIZATION_GUIDE.md)), the Report.md file will be located here as `technical-report.md`.

## Project Overview

This project demonstrates how network science can optimize political outreach campaigns by:
1. Identifying influential individuals within social networks
2. Detecting community structures
3. Simulating information diffusion
4. Comparing targeted vs. random strategies

## Key Metrics

- **Network Coverage**: 92.2% with targeted approach vs. 25.2% random
- **Community Detection**: 13 algorithmic communities identified
- **Adjusted Rand Index**: 0.221 (algorithmic vs. user-defined communities)
- **Clustering Coefficient**: 0.51 (strong community structure)
- **Average Path Length**: 3.75 (small-world properties)

## Methodology Summary

1. **Data Preprocessing**: Load and clean Facebook ego network data
2. **Network Analysis**: Calculate structural metrics
3. **Community Detection**: Apply Louvain algorithm
4. **Centrality Analysis**: Rank nodes by influence
5. **Simulation**: Model information spread using threshold models
6. **Evaluation**: Compare targeted vs. random seeding strategies

## Further Reading

For implementation details, see the main Jupyter notebook in the `notebooks/` directory.

For questions or discussions, please open an issue on GitHub.
