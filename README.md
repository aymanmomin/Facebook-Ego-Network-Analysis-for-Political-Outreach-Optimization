# Facebook Ego Network Analysis for Political Outreach Optimization

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![NetworkX](https://img.shields.io/badge/NetworkX-2.8+-orange.svg)](https://networkx.org/)

> A data-driven approach to optimizing political outreach campaigns using network science and community detection algorithms.

## 📌 Overview

> **For Employers**: See [EMPLOYER_HIGHLIGHTS.md](EMPLOYER_HIGHLIGHTS.md) for a quick summary of skills demonstrated and business impact.

This project applies advanced network analysis techniques to identify influential users and communities within social networks, enabling more efficient and cost-effective political outreach strategies. By leveraging the Facebook ego network dataset from Stanford SNAP, this analysis demonstrates how targeted approaches can achieve **92.2% outreach coverage** compared to just **25.2% with random targeting**.

### Key Applications
- **Political Campaigns**: Optimize advertising spend by targeting high-influence individuals
- **Social Media Marketing**: Identify key influencers and community structures
- **Information Diffusion**: Model and predict how information spreads through networks
- **Community Analysis**: Understand social group dynamics and relationships

## 🔑 Key Features

### Network Analysis
- **Structural Metrics**: Clustering coefficient (C = 0.51), average path length (L = 3.75)
- **Degree Distribution**: Identifies hub nodes and network topology
- **Small-World Properties**: Analyzes network efficiency and connectivity

### Community Detection
- **Louvain Algorithm**: Detects 13 algorithmic communities with varying densities
- **Comparison with Ground Truth**: Evaluates against user-defined social circles
- **Adjusted Rand Index (ARI)**: Measures alignment between detection methods (ARI = 0.221)

### Centrality Analysis
- **Degree Centrality**: Identifies highly connected influencers
- **Betweenness Centrality**: Discovers bridge nodes connecting different communities
- **Eigenvector Centrality**: Finds nodes connected to other important nodes

### Influence Propagation
- **Threshold Model**: Simulates information spread with configurable activation thresholds
- **Targeted vs. Random Seeding**: Compares strategic vs. random user targeting
- **ROI Analysis**: Demonstrates significant efficiency gains with data-driven approaches

## 🚀 Quick Start

> **New to this project?** See [QUICKSTART.md](QUICKSTART.md) for a 5-minute setup guide.

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Clone this repository:
```bash
git clone https://github.com/aymanmomin/Facebook-Ego-Network-Analysis-for-Political-Outreach-Optimization.git
cd Facebook-Ego-Network-Analysis-for-Political-Outreach-Optimization
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. The dataset is included in the `data/` directory (Stanford SNAP Ego-Facebook dataset)

### Usage

Open and run the Jupyter notebook:
```bash
# Main analysis notebook
jupyter notebook cpsc-572-facebook-ego-network-analysis.ipynb
```

Or use JupyterLab:
```bash
jupyter lab
```

The notebook is fully self-contained and includes:
- Automatic package installation
- Data loading and preprocessing
- All analysis steps with detailed explanations
- Visualization generation

## 📊 Results & Insights

### Community Structure
- **13 Communities Detected**: Varying from tight-knit groups (density = 1.0) to loose networks (density = 0.154)
- **High-Density Communities**: Enable rapid information spread within groups
- **Low-Density Communities**: Require bridge nodes for effective reach

### Influence Campaigns
- **Targeted Approach**: 92.2% network coverage with strategic seeding
- **Random Approach**: Only 25.2% coverage with same budget
- **Key Finding**: Degree centrality is the most effective metric for practical targeting

### Bridge Nodes
Critical connectors identified (nodes 277, 175, 19, 23, 25) that link otherwise disconnected communities, essential for cross-community influence.

## 📁 Project Structure

```
├── notebooks/
│   └── facebook-ego-network-analysis.ipynb  # Main analysis notebook
├── data/                          # Facebook ego network dataset
│   ├── facebook_combined.txt      # Combined edge list
│   ├── *.edges                    # Individual ego networks
│   ├── *.circles                  # User-defined social circles
│   ├── *.feat                     # Node features
│   └── network_communities.html   # Interactive visualization
├── visualizations/                # Analysis output images
│   ├── day1_results.png           # Basic statistics
│   ├── day2_results.png           # Community detection
│   ├── day3_results.png           # Influence simulation
│   ├── part1_results.png
│   └── part2_results.png
├── docs/                          # Documentation
│   ├── README.md                  # Documentation index
│   └── technical-report.md        # Detailed analysis report
├── requirements.txt               # Python dependencies
├── CONTRIBUTING.md                # Contribution guidelines
├── REORGANIZATION_GUIDE.md        # File organization instructions
├── README.md                      # This file
├── LICENSE                        # MIT License
└── .gitignore                     # Git ignore patterns
```

**Note**: See [REORGANIZATION_GUIDE.md](REORGANIZATION_GUIDE.md) for instructions on organizing files into the recommended structure.

## 🛠️ Technical Stack

- **NetworkX**: Graph manipulation and analysis
- **Python-Louvain**: Community detection
- **Pandas**: Data manipulation
- **NumPy**: Numerical computations
- **Matplotlib**: Static visualizations
- **PyVis**: Interactive network visualizations
- **Scikit-learn**: Similarity metrics (ARI)
- **tqdm**: Progress tracking

## 📈 Methodology

1. **Data Preprocessing**: Load ego network, filter isolates, construct graph
2. **Structural Analysis**: Calculate network metrics and compare with null models
3. **Community Detection**: Apply Louvain algorithm and compare with ground truth
4. **Centrality Computation**: Rank nodes by influence potential
5. **Threshold Simulation**: Model information diffusion with activation thresholds
6. **Strategy Comparison**: Evaluate targeted vs. random seeding approaches

## 🎯 Use Cases

This framework can be adapted for:
- **Marketing Campaigns**: Identify brand ambassadors and influencers
- **Public Health**: Optimize health intervention programs
- **Corporate Communications**: Internal information dissemination strategies
- **Academic Research**: Social network studies and graph theory
- **Product Launches**: Viral marketing and early adopter identification

## 📚 Dataset

**Stanford SNAP Ego-Facebook Network**
- **Source**: [Stanford Network Analysis Project](https://snap.stanford.edu/data/ego-Facebook.html)
- **Description**: Anonymized Facebook friendship networks from survey participants
- **Size**: 4,039 nodes, 88,234 edges
- **Features**: Anonymized profile attributes, user-defined circles
- **Citation**: J. McAuley and J. Leskovec. Learning to Discover Social Circles in Ego Networks. NIPS, 2012.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open issues for bugs or feature requests
- Submit pull requests with improvements
- Share your use cases and adaptations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Ayman Momin**
- GitHub: [@aymanmomin](https://github.com/aymanmomin)
- LinkedIn: [Connect with me](https://www.linkedin.com/in/aymanmomin/)

## 📖 Additional Resources

- **[RESUME_EXAMPLES.md](RESUME_EXAMPLES.md)** - Ready-to-use resume bullets and LinkedIn posts
- **[EMPLOYER_HIGHLIGHTS.md](EMPLOYER_HIGHLIGHTS.md)** - Executive summary for recruiters
- **[QUICKSTART.md](QUICKSTART.md)** - 5-minute setup guide
- **[Report.md](Report.md)** - Detailed technical analysis

## 🙏 Acknowledgments

- Stanford Network Analysis Project (SNAP) for providing the dataset
- NetworkX development team for the excellent graph analysis library
- Python open-source community

---

**⭐ If you find this project useful, please consider giving it a star!**