# 🚀 **Dynamic Pricing Using Reinforcement Learning for Blinkit**  

📌 **Author:** Jasraj Shendge  
📌 **Institution:** Manipal University Jaipur  

## 📖 **Introduction**  

### **Problem Statement**  
Blinkit, a fast-growing **online grocery delivery platform**, faces challenges in **optimizing pricing strategies** to maximize revenue, sales, and customer satisfaction. Unlike static pricing, **dynamic pricing** adapts based on real-time demand, seasonality, and competition.  

### **Business Goals**  
✅ **Identify the optimal pricing strategy** to maximize revenue and profit.  
✅ **Understand price elasticity** and how customers respond to pricing changes.  
✅ **Implement dynamic pricing** that adjusts in **real-time**.  

---

## 🎯 **Project Contributions**  

✔️ **Incorporating Price Elasticity of Demand (PED) for Smarter Pricing**  
✔️ **Developing a Reinforcement Learning (RL) Model for Dynamic Pricing**  
✔️ **Visualizing & Evaluating Revenue, Profitability, and PED Alignment**  

---

## 📊 **Dataset Description & Visualization**  

The dataset contains essential pricing and sales data:  

| **Column Name**      | **Description**  |
|----------------------|----------------|
| `Item_Identifier`    | Unique product ID |
| `Item_Type`         | Product category |
| `Item_MRP`          | Maximum Retail Price |
| `Item_Outlet_Sales` | Total sales generated |
| `Outlet_Location_Type` | Store location type (Urban/Rural) |
| `Outlet_Type`       | Type of store |

### 📌 **Data Insights**  
- 📉 **Price vs. Sales Relationship:** Scatter plot showing sales variation with price changes.  
- 📊 **Distribution of Price Elasticity of Demand (PED):** Identifies elastic & inelastic products.  

---

## 🧠 **Algorithm Used: Q-Learning for Dynamic Pricing**  

Q-learning is a **reinforcement learning algorithm** that helps the agent learn **optimal pricing strategies** by interacting with the environment.  

### 🔢 **Q-Learning Formula**  

\[
Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max Q(s', a') - Q(s, a) \right]
\]

Where:  
- \( Q(s, a) \) = Value of taking action \( a \) in state \( s \).  
- \( \alpha \) = Learning rate.  
- \( r \) = Reward (profit/revenue from pricing decision).  
- \( \gamma \) = Discount factor.  
- \( \max Q(s', a') \) = Best Q-value for the next state \( s' \).  

### 📌 **Flowchart of the RL Model**  
🔹 **Input Data** (MRP, Sales, PED, Demand Trends)  
🔹 **Agent Observes Price & PED**  
🔹 **Agent Decides Pricing Action (Increase, Maintain, Decrease)**  
🔹 **Revenue & Demand Feedback Collected**  
🔹 **Q-Table Updated Based on Reward**  
🔹 **Agent Learns & Optimizes Pricing**  

---

## ⚙️ **Hyperparameters & Training Process**  

| **Hyperparameter** | **Value Used** |
|-------------------|--------------|
| Learning Rate \( \alpha \) | 0.1 |
| Discount Factor \( \gamma \) | 0.9 |
| Exploration Rate \( \epsilon \) | Starts at 1.0, decays to 0.01 |
| Number of Episodes | 1000 |

### 📊 **Training Visualization**  

📈 **1. Reward Convergence Over Time**  
📊 **2. Exploration vs. Exploitation Trade-off**  

---

## 📊 **Experimental Results & Evaluation**  

### ✅ **Key Metrics Used**  

| **Metric** | **Description** |
|------------|----------------|
| **Revenue Improvement (%)** | Change in revenue due to RL pricing |
| **Profit Margin Impact (%)** | Impact on overall profitability |
| **PED Alignment (%)** | How well the RL model aligns with PED analysis |
| **Exploration vs. Exploitation Balance** | Evaluates whether the RL agent is too aggressive or conservative |

### ✅ **Evaluation Results**  

| **Item Type** | **Old Price** | **New Price (RL)** | **Revenue Change (%)** | **Profit Margin Change (%)** |
|--------------|--------------|---------------------|----------------------|---------------------------|
| Dairy       | 50           | 55                  | +8.5%                 | +6.3%                      |
| Snacks      | 30           | 27                  | -3.2%                 | +1.5%                      |
| Beverages   | 20           | 22                  | +5.1%                 | +4.8%                      |

### 📊 **Result Visualizations**  

📉 **1. Revenue Improvement (%) by Item Type**  
📈 **2. Profit Margin Impact (%) by Item Type**  
📊 **3. Price Elasticity Alignment (PED Impact Score Distribution)**  
📊 **4. Exploration vs. Exploitation: Price Change Distribution**  

![output](https://github.com/user-attachments/assets/6e8722f6-63c6-4ecf-945f-f894623b83ad)
![Figure_1](https://github.com/user-attachments/assets/7d1c482f-d31f-4827-be89-fffcca9d862e)
![Figure_2](https://github.com/user-attachments/assets/de806cb1-498c-447e-934e-3955a3627b01)
![Figure_3](https://github.com/user-attachments/assets/026abde7-55ec-405e-85c2-1cb04b48be50)
![Figure_4](https://github.com/user-attachments/assets/e0e6c79b-40d4-4d64-a225-48648828d7b0)


---

## 🚀 **Conclusion & Future Work**  

### 📌 **Conclusion**  
This project successfully demonstrates **Reinforcement Learning-based Dynamic Pricing**, integrating **PED insights** into pricing decisions. The **Q-Learning algorithm** optimally adjusts prices to **maximize revenue and profit**.  

### 🔮 **Future Enhancements**  
✔️ **Testing on Real-World E-Commerce Data**  
✔️ **Using Deep Q-Learning for Improved Decision-Making**  
✔️ **Integrating Seasonal & Competitor Pricing Factors**  

---

## 📁 **Project Structure**  

```
📂 dynamic-pricing-rl  
│── 📜 RL_Pricing_Comparison.csv  # Comparison of RL vs. static pricing  
│── 📜 PED_Results.csv  # Price Elasticity of Demand data  
│── 📜 q_table.npy  # Trained Q-table  
│── 📜 main.ipynb  # Jupyter notebook for training the RL model  
│── 📜 evaluation.ipynb  # Notebook for analyzing and visualizing results  
│── 📜 README.md  # This file  
```

---

## ⚡ **How to Run This Project**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/yourusername/dynamic-pricing-rl.git
cd dynamic-pricing-rl
```

### **2️⃣ Install Dependencies**  
```sh
pip install numpy pandas matplotlib seaborn gym
```

### **3️⃣ Train the RL Model**  
```sh
python main.py
```

### **4️⃣ Evaluate Results**  
```sh
python evaluation.py
```

---

## 👨‍💻 **Connect with Me**  

📧 **Email:** jasraj.shendge@example.com  
🌐 **LinkedIn:** [Jasraj Shendge](https://www.linkedin.com/in/jasrajshendge/)  
📂 **GitHub:** [jasrajshendge](https://github.com/jasrajshendge)  

---

Let me know if you need further modifications! 🚀🔥
