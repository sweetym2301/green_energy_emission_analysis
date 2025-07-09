# 🌍 Green Energy Production & Emissions Dashboard

This project analyzes and visualizes **global green energy production**, fossil fuel trends, and emissions data over time for multiple countries.

It demonstrates:
- 📊 **Data cleaning** with Python (`pandas`)
- 📈 **Data visualization** with Matplotlib, Seaborn, and Plotly
- ⚡ **Interactive dashboard** with Streamlit
- 🔍 Filters for **Country** and **Year**
- 📂 Export filtered data

---

## ✅ Project Structure

```
Project-1/
 ├─ green_energy_emissions/
 │   ├─ data/                  # Raw dataset(s)
 │   ├─ outputs/               # Cleaned CSV output
 │   ├─ proj1_env/             # Virtual environment (not pushed to GitHub)
 │   ├─ cleaned_data.py        # Data cleaning script
 │   ├─ app.py                 # Streamlit dashboard
 │   ├─ README.md              # Project description
 │   ├─ .gitignore             # Ignored files/folders
 │   ├─ requirements.txt       # Project dependencies
```

---

## ✅ Key Features

- 📈 GDP, Population, Fossil Fuel Production & Energy Consumption trends
- 📉 Production Change (Coal, Gas, Oil) visualized year-wise
- 👤 Per Capita metrics for deeper insight
- 🔗 Correlation Heatmap to explore feature relationships
- ⬇️ Download filtered data as CSV

---

## 📌 What is TWh?

**TWh** = Terawatt-hour = 1,000,000,000,000 watt-hours  
It is used to measure large-scale energy production or consumption.

---

## 🚀 How to Run This Project

1️⃣ **Clone this repo:**
```bash
git clone <YOUR_GITHUB_REPO_URL>
```

2️⃣ **Navigate to the project:**
```bash
cd Project-1/green_energy_emissions
```

3️⃣ **Create & activate virtual environment:**
```bash
# Create venv
python -m venv proj1_env

# Activate (PowerShell)
.\proj1_env\Scripts\Activate

# OR Activate (Command Prompt)
proj1_env\Scripts\activate.bat
```

4️⃣ **Install dependencies:**
```bash
pip install -r requirements.txt
```

5️⃣ **Run the Streamlit app:**
```bash
streamlit run app.py
```

6️⃣ **Open the dashboard:**  
A browser will open at [http://localhost:8501](http://localhost:8501)

---

## ⚙️ Tech Stack

- Python 3.x
- Pandas, NumPy
- Matplotlib, Seaborn, Plotly
- Streamlit

---

## 👩‍💻 Author

**Sweety**

---

## 📜 License

This project is for learning and demonstration purposes.  
Feel free to fork & extend it!

---

✅ **Happy analyzing!**
