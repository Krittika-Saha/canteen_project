import streamlit as st
import pandas as pd
try:
    from .database import get_available_menu
except ImportError:
    from database import get_available_menu

def total_bill(order_items):
    for item in order_items:
        item["Total"]= item["price"] * item["quantity"]
    return sum(item["Total"] for item in order_items)
 
def main():
    st.title("Canteen Ordering System")
    student = st.session_state.get("student")

    if student is None:
        st.warning("Please log in before placing an order.")
        if st.button("Go to Login"):
            st.session_state["page"] = "login"
            st.rerun()
        return

    st.subheader(f"Welcome, {student.name} from class {student.student_class}!")

    menu = get_available_menu()
    if not menu:
        st.warning("No menu items available at the moment.")
        return

    st.subheader("Today's Menu")

    with st.form("order_form"):
        h1, h2, h3 = st.columns([1, 3, 1])
        with h1:
            st.write("Item Name")
        with h2:
            st.write("Price")
        with h3:
            st.write("Quantity")

        selected_items = []
        for item in menu:
            item_id = item[0]
            item_name = item[1]
            item_price = item[2]

            col1, col2, col3 = st.columns([1, 3, 1])
            with col1:
                st.write(item_name)
            with col2:
                st.write(item_price)
            with col3:
                quantity = st.number_input(
                    f"Quantity for {item_name}",
                    min_value=0,
                    step=1,
                    key=f"qty_{item_id}",
                    label_visibility="collapsed",
                )

            if quantity > 0:
                selected_items.append(
                    {
                        "item_id": item_id,
                        "item_name": item_name,
                        "price": item_price,
                        "quantity": quantity,
                    }
                )

        submitted = st.form_submit_button("Place Order")

    if submitted:
        if not selected_items:
            st.warning("Please select at least one item with a quantity greater than zero.")
            return

        bill = total_bill(selected_items)
        st.session_state["confirmed_order"] = selected_items

        st.subheader("Order Summary")
        order_summ={
            "Item Name": [item["item_name"] for item in selected_items],
            "Price": [item["price"] for item in selected_items],
            "Quantity": [item["quantity"] for item in selected_items],
            "Total": [item["price"] * item["quantity"] for item in selected_items]
        }
        df= pd.DataFrame(order_summ)
        st.dataframe(df, use_container_width=True)

        st.success(f"Your order has been placed successfully. Total bill: {bill}")
