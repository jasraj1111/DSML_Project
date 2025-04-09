# 🚀 Dynamic Pricing Using Reinforcement Learning for Blinkit  


> 🔍 **Author:** [Jasraj Shendge](https://www.linkedin.com/in/jasrajshendge)  
> 🎓 **Institution:** Manipal University Jaipur  
> 📅 **Academic Year:** 2024–2025

---

## 📖 Overview

This project implements a **Dynamic Pricing Strategy** for Blinkit using **Reinforcement Learning (RL)** and **Price Elasticity of Demand (PED)**. Unlike static pricing, dynamic pricing allows businesses to **adjust prices based on real-time demand, consumer behavior, and market conditions**.

We explore two RL algorithms — **Q-Learning** and **Deep Q-Network (DQN)** — and compare their effectiveness in optimizing pricing strategies.

---

## 🎯 Objectives

- ✅ Predict and understand **Price Elasticity of Demand** (PED)  
- ✅ Implement **Q-Learning** and **DQN** for dynamic pricing  
- ✅ Maximize **revenue** and **profit margin** through smart decisions  
- ✅ Perform comparative analysis between RL techniques  
- ✅ Visualize and interpret the impact of price changes  

---

## 📊 Dataset Overview

The dataset is sourced from a grocery sales environment and contains the following key columns:

| Column | Description |
|--------|-------------|
| `Item_Identifier` | Unique product ID |
| `Item_Type` | Category of product |
| `Item_MRP` | Maximum Retail Price |
| `Item_Outlet_Sales` | Total sales generated |
| `Outlet_Location_Type` | Urban/Rural classification |
| `Outlet_Type` | Store type (Supermarket, Grocery, etc.) |

**Visualizations Included:**
- 📉 Price vs Sales Scatter Plot  
- 📊 PED Distribution Histogram  
- 📈 RL Reward Convergence  
- 📊 Exploration vs Exploitation Trend  
- 📊 Revenue & Profit Comparison Charts  

---

## 🧠 Machine Learning Techniques

### 📌 Step 1: PED Calculation using Regression

We evaluated **Random Forest**, **XGBoost**, and **Linear Regression** models. Based on R² scores, **XGBoost** was selected for PED estimation.

- PED was calculated by simulating a ±5% price change and recording the variation in predicted sales.
- Final PED scores were used to categorize items as elastic or inelastic.

### 📌 Step 2: Reinforcement Learning Models

| Model | Description |
|-------|-------------|
| **Q-Learning** | Tabular model, easy to interpret |
| **Deep Q-Network (DQN)** | Neural network-based, supports large state-action spaces |

---

## ⚙️ Training Configurations

| Hyperparameter | Value |
|----------------|-------|
| Learning Rate (α) | 0.1 |
| Discount Factor (γ) | 0.9 |
| Exploration Rate (ε) | Decays from 1.0 to 0.01 |
| Episodes | 1000 |

📈 Visualizations track reward convergence, PED alignment, and exploration strategies.

---

## 🧪 Experimental Results

| Item Type | Old Price | New Price (RL) | Revenue Change | Profit Margin Change |
|-----------|-----------|----------------|----------------|-----------------------|
| Dairy     | ₹50       | ₹55            | +8.5%          | +6.3%                |
| Snacks    | ₹30       | ₹27            | -3.2%          | +1.5%                |
| Beverages | ₹20       | ₹22            | +5.1%          | +4.8%                |

---

## 📊 Comparison: Q-Learning vs DQN

| Criteria | Q-Learning | DQN |
|----------|------------|-----|
| Interpretability | ✅ High | ⚠️ Lower |
| Scalability | ❌ Low | ✅ High |
| Revenue Improvement | Moderate | High |
| Training Time | Fast | Slower |
| Use Case Suitability | Small to Mid-Size | Large-scale environments |

📌 *DQN emerges as the better approach for complex, high-dimensional pricing scenarios.*

---

## 📁 Project Structure

📂 dynamic-pricing-rl
├── main.ipynb # Q-Learning implementation
├── dqn_model.ipynb # DQN agent implementation
├── evaluation.ipynb # Result analysis & visualization
├── RL_Pricing_Comparison.csv # Q-Learning vs. Static Pricing
├── PED_Results.csv # PED values by item
├── q_table.npy # Trained Q-table
├── model_weights.h5 # DQN model weights
└── README.md # Project overview (this file)

## ⚡ How to Run

### 1️⃣ Setup

bash
git clone https://github.com/jasrajshendge/dynamic-pricing-rl.git
cd dynamic-pricing-rl
pip install -r requirements.txt

2️⃣ Run Q-Learning Agent
bash
Copy
Edit
jupyter notebook main.ipynb
3️⃣ Run DQN Agent
bash
Copy
Edit
jupyter notebook dqn_model.ipynb

### Conclusion
This project proves the effectiveness of Reinforcement Learning in dynamic pricing when fused with Price Elasticity of Demand. The Q-Learning model offered strong baseline performance, while the DQN agent outperformed in real-world scalability and revenue lift. Together, these models showcase a powerful approach to automated, demand-sensitive pricing in the e-commerce domain.

🔮 Future Scope
Integrate competitor pricing and seasonal trends

Use Multi-Agent Reinforcement Learning (MARL) for multi-brand scenarios

Develop a real-time pricing engine for deployment

Explore hierarchical RL for region-based or product-cluster pricing

📬 Connect with Me
👨‍💻 Jasraj Shendge
📧 jasraj.shendge@example.com
🔗 LinkedIn
📂 GitHub

vbnet
Copy
Edit

Let me know if you'd like a `.pdf` version or need help designing a GitHub repo banner or README visu
