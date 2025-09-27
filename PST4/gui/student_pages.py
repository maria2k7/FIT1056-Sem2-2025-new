# gui/student_pages.py
import streamlit as st

def show_student_management_page(manager):
    """Renders all components for the student management page."""
    st.header("Student Management")

    # --- Search Section (remains the same) ---
    st.subheader("Find a Student")
    # ...
    with st.form("Search for a student?"):
        student_name = st.text_input("Student Name")
        student_id = st.text_input("ID")
        submitted = st.form_submit_button("Search!")
        
        if submitted:
            # This call now works because we implemented the method in PST3.
            # TODO: Add a check for blank name/instrument.
            if student_name and student_id:
                lookup_student = manager.find_student_by_id(student_id)
                if lookup_student:
                    st.success(f"Successfully found {student_name}!")
                    # You can use st.balloons() for extra flair.
                else:
                    st.error(f"Hmm, perhaps this student doesn't exist. Try again next time!")
            else:
                st.warning("Please enter both a name and an instrument.")
    # --- Registration Section (now works correctly) ---
    st.subheader("Register New Student")
    with st.form("registration_form"):
        reg_name = st.text_input("New Student Name")
        reg_instrument = st.text_input("First Instrument")
        submitted = st.form_submit_button("Register Student")
        
        if submitted:
            # This call now works because we implemented the method in PST3.
            # TODO: Add a check for blank name/instrument.
            if reg_name and reg_instrument:
                new_student = manager.register_new_student(reg_name, reg_instrument)
                if new_student:
                    st.success(f"Successfully registered {reg_name}!")
                    # You can use st.balloons() for extra flair.
                else:
                    st.error(f"Could not register student. A teacher for {reg_instrument} might not be available.")
            else:
                st.warning("Please enter both a name and an instrument.")