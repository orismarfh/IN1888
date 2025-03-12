# 🏦 IN1888 - Crypto Exchange File Processor

🚀 **IN1888** is a Python-based script designed to process and format financial records from exchange files.  
It **normalizes CPF/CNPJ formats**, converts **dates**, adjusts **cryptocurrency quantities** to **10 decimal places**, and reformats **monetary values** for accurate reporting.

---

## 📖 Features
✅ **Formats CPF/CNPJ** – Removes non-numeric characters for consistency.  
✅ **Converts dates** – Ensures standardized date formats.  
✅ **Formats cryptocurrency amounts** – Converts to 10 decimal places.  
✅ **Monetary values normalization** – Converts amounts into proper currency format.  

---

## 📂 File Processing Example
### **Input (`2025_02_exchange_bin.txt`):**

0110|01012025|John Doe|123.456.789-00|100000|25000|BTC|1000000000 
0510|01012025|Company X|12.345.678/0001-00|500000|ETH|2000000000


### **Output (After Processing):**

0110|01012025|John Doe|12345678900|1.000,00|250,00|BTC|0,1000000000 
0510|01012025|Company X|12345678000100|5.000,00|ETH|0,2000000000

---

## 🚀 How to Use
### 1️⃣ Clone the Repository
```bash
git clone git@github.com:orismarfh/IN1888.git
cd IN1888

2️⃣ Install Dependencies
pip install pandas
3️⃣ Run the Script
python processar_arquivo.py
📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

👤 Created by @orismarfh – Feel free to contribute or report issues! 🚀




# IN1888
