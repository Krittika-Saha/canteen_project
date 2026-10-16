import streamlit as st

try:
    from .database import (get_menu_items, update_menu)
except ImportError:
    from database import (get_menu_items, update_menu)



def show_admin_menu():
    st.title("Canteen Menu")

    menu_items = get_menu_items()

    edited_menu = st.data_editor(
        menu_items,
        width="stretch",
        disabled=["item_id", "item_name"],
        column_config={
            "item_id": "item_id",
            "item_name": "item_name",
            "price": st.column_config.NumberColumn(
                "price",
                min_value=0,
                step=1
            ),
            "available": st.column_config.CheckboxColumn(
                "available"
            )
        },
        hide_index=True
    )

    if st.button("Save Changes"):
        update_menu(edited_menu)
        st.success("Menu updated successfully!")

def show_orders():
    if "confirmed_order" in st.session_state:
        confirmed_order = st.session_state["confirmed_order"]
    if "student" in st.session_state:
        student = st.session_state["student"]
    
    st.subheader("Confirmed Orders")
    osumm={
        "Student ID": student.student_id,
        "Order": [str({"Item Name": item["item_name"], "Price": item["price"], "Quantity": item["quantity"], "Total": item["price"] * item["quantity"]} for item in confirmed_order)],
        "Total Bill": sum(item["price"] * item["quantity"] for item in confirmed_order)
    } 
    st.dataframe(osumm, use_container_width=True)   
    



def main():
    show_admin_menu()
    if st.button("View Confirmed Orders"):
        show_orders()


if __name__ == "__main__":
    main()