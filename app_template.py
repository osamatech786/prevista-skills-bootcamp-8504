import streamlit as st

# Initialize session state variables if they do not exist
if 'step' not in st.session_state:
    st.session_state.step = 1
    st.session_state.input1 = ""
    st.session_state.input2 = ""

# Define a function to calculate progress and percentage
def get_progress(step, total_steps=2):
    return int((step / total_steps) * 100)

# Define the total number of steps
total_steps = 2

# Calculate the current progress
progress = get_progress(st.session_state.step, total_steps)

# Display the progress bar and percentage
st.write(f"Progress: {progress}%")
st.progress(progress)

# Define the different steps
if st.session_state.step == 1:
    st.title("Step 1")
    st.session_state.input1 = st.text_input("Input Field 1", value=st.session_state.input1)
    if st.button("Next"):
        if st.session_state.input1:
            st.session_state.step = 2
            st.experimental_rerun()  # Ensure the app reruns to update the step
        else:
            st.warning("Please fill in the input field before proceeding.")

elif st.session_state.step == 2:
    st.title("Step 2")
    st.session_state.input2 = st.text_input("Input Field 2", value=st.session_state.input2)
    if st.button("Submit"):
        if st.session_state.input2:
            st.write("Form submitted successfully!")
            st.write(f"Input 1: {st.session_state.input1}")
            st.write(f"Input 2: {st.session_state.input2}")

            # Reset the form for the next use
            st.session_state.step = 1
            st.session_state.input1 = ""
            st.session_state.input2 = ""
            st.experimental_rerun()  # Ensure the app reruns to reset the form
        else:
            st.warning("Please fill in the input field before submitting.")
