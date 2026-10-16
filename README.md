# 🥪 School Canteen Digital Ordering & Token Management System

A secure, modular, web-based canteen ordering and token management system built using **Python**, **Streamlit**, and **MySQL**. 

Designed  for school environments with no-phone/no-online-payment policies, allowing students to place orders from school screens using a digital token balance, to be recharged by physical cash recharges.


## Key Features

* **Student Portal**: Secure login and registration with hashed passwords (`Werkzeug`).
* **Digital Token & Cash Recharge System**: Students have a digital balance and can request cash recharges approved by staff. Can monitor changes to balance live.
* **Digital Menu**: Real-time digital menu where staff can update item list and pricing.
* **Ordering and Tracking**: Cart-selection system supporting item quantities and order statuses (`Placed` $\rightarrow$ `Preparing` $\rightarrow$ `Ready` $\rightarrow$ `Collected`), and live auto-refreshing tracking.
* **Admin Panel**: Interface for canteen staff to manage incoming orders, approve cash recharges, and control menu list and inventory.


##  Tech Stack

* **Frontend**: [Streamlit](https://streamlit.io/)
* **Database**: [MySQL](https://www.mysql.com/) via `mysql-connector-python`
* **Data Manipulation**: [Pandas](https://pandas.pydata.org/)
* **Security**: `Werkzeug` (Password Hashing)


## Project Structure

```text
canteenproject/
│
├── authetication.py     # Student entry point, login, registration & session routing
├── admin.py             # Canteen staff interface (Order status, Menu editor, Recharge approvals)
├── orders.py            # Student ordering interface, cart & order tracking
├── database.py          # MySQL connection, table creation & CRUD operations
├── README.md            # Project documentation
└── requirements.txt     # Module list for easy project set up
```
---

## Setup and Installation
### 1. Clone or Download the Repository
Clone the repository using your terminal or download the ZIP folder directly from GitHub.

* **Option A: Using Git Clone**
  ```bash
  git clone https://github.com/Krittika-Saha/canteen_project.git
  cd canteen_project
  ```
* **Option B: Downloading as ZIP**
  Click the green **Code** button on the GitHub repository page and select **Download ZIP**, then extract it to your preferred folder.

![Clone or Download Repo](path/to/your/screenshot.png)

---

### 2. Install Dependencies
Open your terminal inside the project directory and install all required Python packages using the `requirements.txt` file:

```bash
pip3 install -r requirements.txt
```

---

### 3. Configure Database Credentials
Open `database.py` and update your local MySQL connection settings if necessary:
```python
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_mysql_password",
        database="test",
    )
```

---

### 4. Run the Application

You will need to run the **Admin Panel** and the **Student Portal / Authentication** in separate terminal windows.

* **Run the Canteen Admin Panel:**
  ```bash
  streamlit run admin.py
  ```

* **Run the Student Portal & Authentication System:**
  ```bash
  streamlit run authetication.py
  ```

---
