# **Optimizing Political Outreach via Facebook Ego Network Analysis**  
**Author**: Ayman Momin

---

## **Abstract**  
This study analyzes a Facebook ego network to identify influential users and communities for optimizing political advertising. Using network science techniques (Louvain community detection, centrality metrics, and threshold models), we demonstrate that targeting high-degree nodes within structurally detected communities achieves **92.2% outreach coverage**, compared to **25.2% for random seeding**. Despite low alignment between algorithmic communities and user-defined circles (ARI = 0.221), structural targeting proves highly efficient. Key limitations include dataset bias (single ego network) and threshold assumptions.  

---

## **1. Introduction**  
### **Motivation**  
Political campaigns increasingly rely on social media to maximize outreach. Traditional strategies often waste resources on low-impact users. Network science offers a data-driven alternative: by identifying influential individuals and communities, campaigns can prioritize high-impact targets.  

### **Research Questions**  
1. How do structural properties (clustering, density) differ between communities in a Facebook ego network?  
2. Which non-ego nodes act as bridges/hubs for information spread?  
3. How does structural targeting compare to random seeding in outreach efficiency?  

### **Dataset Choice**  
We selected the [Stanford SNAP Ego-Facebook dataset](https://snap.stanford.edu/data/ego-Facebook.html) because:  
- It provides anonymized, real-world social connections.  
- Includes user-defined circles (ground truth for communities).  
- Avoids API restrictions and privacy concerns.  

---

## **2. Methods**  
### **Data Preprocessing**  
- **Excluded Ego Node**: The dataset contains friendships between the ego’s friends, not including the ego itself. This avoided dominance by a central node.  
- **Filtered Isolates**: Removed 0 isolated nodes (no isolates present).  

### **Network Analysis**  
1. **Structural Metrics**:  
   - **Clustering Coefficient**: \( C = 0.51 \), indicating strong community structure.  
   - **Average Path Length**: \( L = 3.75 \), reflecting small-world properties.  
   - **Degree Distribution**: Right-skewed (Fig. 1a), with hubs like Node 53 (degree = 0.697).  

2. **Null Model**:  
   - Used a **configuration model** (degree-preserving randomization) instead of Erdős-Rényi.  
   - **Why?** ER’s Poisson degree distribution poorly matches real-world networks.  

3. **Community Detection**:  
   - **Louvain Algorithm**: Chosen for scalability and resolution balance.  
   - **ARI Calculation**: Compared to user-defined circles (ground truth).  

4. **Centrality Analysis**:  
   - **Degree**: Primary metric for outreach (highest practical relevance).  
   - **Betweenness**: Limited utility due to sparse distribution.  

5. **Influence Simulation**:  
   - **Threshold Model**: Activated nodes if ≥20% of neighbors adopted.  
   - **Seeding**: Targeted top 5% degree-central nodes vs. random.  

### **Iterative Changes**  
- **Initial Approach**: Used ER null model; switched to configuration model after feedback.  
- **Failed Assumption**: Attempted to remove ego node (not present in dataset).  
- **Code Fixes**: Error handling for small communities in betweenness calculations.  

---

## **3. Results**  
### **Key Findings**  
1. **Community Structure** (Fig. 1b-c):  
   - **Louvain Communities**: 13 groups, avg. size 25 nodes.  
   - **User Circles**: 24 groups, avg. size 10 nodes.  
   - **ARI = 0.221**: Partial alignment (e.g., some structural clusters overlapped with "family" circles).  

2. **Centrality** (Fig. 2a):  
   - **Hubs**: Node 53 (degree = 0.697), Node 322 (degree = 0.505).  
   - **Bridges**: Sparse betweenness scores (top bridge: Node 122, betweenness = 0.12).  

3. **Influence Spread** (Fig. 3a-b):  
   - **Targeted Seeding**: 92.2% coverage (307 nodes).  
   - **Random Seeding**: 25.2% coverage (84 nodes).  

#### **3.1 Community Structure & Density**  
We detected 13 communities using the Louvain algorithm, with significant variation in density (Fig. 4a):  
- **High-Density Communities**:  
  - *Community 6* (Density = 0.872) and *Community 7* (Density = 1.0) represent **tightly-knit groups** (e.g., family or coworkers).  
  - These communities require fewer seeds for full activation due to high interconnectivity.  
- **Low-Density Communities**:  
  - *Community 4* (Density = 0.154) and *Community 5* (Density = 0.171) are **sparse**, likely aggregating acquaintances or distant friends.  
  - Influence spreads slower here, requiring bridge nodes to connect subgroups.  

#### **3.2 Bridge Nodes**  
Betweenness centrality analysis identified critical connectors:  
- **Top Bridge Nodes**: 277, 175, 19, 23, 25.  
- **Role**: These nodes link otherwise disconnected communities (e.g., Node 277 connects Communities 0 and 2).  


### **Visualizations**  
- **Figure 1**: Basic statistics and null model comparison (`part1_results.png`).  
- **Figure 2**: Community comparison and centrality distributions (`part2_results.png`).  
- **Figure 3**: Activation spread and curves (`day3_activation.png`, `part3_results.png`).  


---

## **4. Discussion**  
### **Structural vs. Social Targeting**  
- **Low ARI**: Algorithmic communities capture structural clusters, not explicit social roles.  
- **Practical Implication**: Hybrid strategies (structural + social) may optimize outreach.  


#### **4.1 Structural Heterogeneity**  
- **High-Density Communities**: Act as echo chambers—once activated, information spreads rapidly internally but struggles to cross boundaries without bridges.  
- **Low-Density Communities**: Require bridge nodes (e.g., Node 277) for cross-community influence.  

#### **4.2 Hybrid Targeting Strategy**  
- **Hubs vs. Bridges**:  
  - **Node 53** (degree = 0.697) efficiently activates its dense community (Community 1, density = 0.331).  
  - **Node 277** (betweenness = 0.12) enables spillover into adjacent communities.  
- **Implication**: Combine hub targeting (for intra-community spread) and bridge targeting (for inter-community reach).  


### **Why Degree Centrality Worked**  
- **Hub Dominance**: High-degree nodes connect many neighbors, enabling rapid cascades.  
- **Small-World Effect**: Short paths (\( L = 3.75 \)) allow influence to jump communities.  

### **Limitations**  
1. **Ego Network Bias**: Friendships are centered on one user; global Facebook structure is unknown.  
2. **Deterministic Model**: Assumes perfect information spread (no resistance/noise).  
3. **Threshold Sensitivity**: Real campaigns may require higher thresholds (e.g., 30%).  

---

## **5. Conclusion**  
This study demonstrates that network science can drastically improve political outreach efficiency. Key takeaways:  
- **Target Hubs**: Prioritize high-degree nodes (e.g., Node 53) for rapid spread.  
- **Validate with Social Context**: Use user circles to refine messaging.  
- **Scalability**: Methods apply to any friendship-based network (Twitter, LinkedIn).  

Future work should test these strategies on larger, aggregated ego networks and incorporate stochastic thresholds.  

or use this - updated based on the new research question

This analysis reveals two critical insights for political outreach:  
1. **Community Density Matters**: Target hubs in high-density communities (e.g., Community 7) for rapid local saturation.  
2. **Bridges Enable Broad Reach**: Augment hub targeting with bridge nodes (e.g., 277, 175) to cross community boundaries.  

While degree centrality remains the primary metric for efficiency, betweenness centrality refines cross-community strategies.  


---

## **References**  
- Dataset: Leskovec, J., & Mcauley, J. (2012). [Learning to Discover Social Circles in Ego Networks](https://snap.stanford.edu/data/ego-Facebook.html).  
- Software: NetworkX, Python-Louvain, PyVis.  

---

## **Appendices**  
### **Code Availability**  
- GitHub Repository: [Link] (Include your Kaggle notebook or GitHub link).  
- Key Functions: Threshold model, Louvain detection, configuration model.  

### **Ethics Statement**  
- Data anonymized; no personal identifiers used.  
- Simulations hypothetical; no real campaigns targeted.  

