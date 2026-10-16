import streamlit as st
from werkzeug.security import check_password_hash

try:
    from .database import get_db_connection, register_student, get_student_by_id
    from .studentdetails import Student
except ImportError:
    from database import get_db_connection, register_student, get_student_by_id
    from studentdetails import Student


def main():
    st.title("School Canteen System")

    #Initializing session state variables
    if "page" not in st.session_state:
        st.session_state["page"] = "login"

    if "student" not in st.session_state:
        st.session_state["student"] = None

    #login page
    if st.session_state["page"] == "login":
        st.subheader("Login")
        with st.form("Login Form"):
            sid = st.number_input("Enter Student ID", min_value=1, step=1)
            pwd = st.text_input("Enter Password", type="password")
            submit = st.form_submit_button("Login")

        if submit:
            if not sid or not pwd:
                st.error("Please fill all the fields")
            else:
                stu_data = get_student_by_id(sid)
                if stu_data is None:
                    st.warning("Student ID not found. Please register.")
                    
                else:
                    checked = check_password_hash(stu_data[3], pwd)
                    if checked:
                        student = Student(stu_data[0], stu_data[1], stu_data[2])
                        st.session_state["student"] = student
                        st.success("Login Successful")
                        st.session_state["page"] = "order"
                        st.rerun()
                    else:
                        st.error("Incorrect Password")
        if st.button("Go to registration page"):
            st.session_state["NewStudentID"]=sid
            st.session_state["page"] = "register"
            st.rerun()

    #Registration page
    if st.session_state["page"] == "register":
        st.subheader("Register")
        with st.form("Registration Form"):
            sid = st.number_input(
                "Enter Student ID",
                min_value=1,
                step=1,
                value=st.session_state.get("NewStudentID", 1),
            )
            sname = st.text_input("Enter Student Name")
            sclass = st.selectbox(
                "Select Class",
                ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"],
            )
            pwd = st.text_input("Enter Password", type="password")
            submit = st.form_submit_button("Register")

        if submit:
            if not sid or not sname or not sclass or not pwd:
                st.error("Please fill all the fields")
            elif get_student_by_id(sid) is not None:
                st.error("This Student ID is already registered.")
            else:
                student = Student(sid, sname, sclass)
                success = register_student(student, pwd)
                if success:
                    st.success("Student Registered Successfully")
                    st.session_state["student"] = student
                    st.session_state["page"] = "order"
                    st.rerun()

        
    #Ordering page
    if st.session_state["page"] == "order":
        try:
            from .orders import main as order_main
        except ImportError:
            from orders import main as order_main
        order_main()


if __name__ == "__main__":
    main()

