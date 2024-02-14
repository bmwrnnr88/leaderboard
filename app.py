import streamlit as st

# Initialize session state for the leaderboard
if 'leaderboard' not in st.session_state:
    st.session_state.leaderboard = []

# Function to get the leaderboard for a specific class period
def get_leaderboard_for_class(class_period):
    return sorted(
        [entry for entry in st.session_state.leaderboard if entry['Class'] == class_period],
        key=lambda x: x['Score'],
        reverse=True
    )

# Sidebar form to add or edit scores
with st.sidebar:
    st.title("Add or Edit Score")
    class_option = st.selectbox("Select Class", options=["Period 1", "Period 2", "Period 3", "Period 4", "Period 5"])
    name = st.text_input("Student Name")
    score = st.number_input("Score", min_value=0)
    add_button = st.button("Add/Update Score")
    
    if add_button:
        # Check if the student already exists in the leaderboard
        student_exists = False
        for entry in st.session_state.leaderboard:
            if entry['Class'] == class_option and entry['Name'] == name:
                entry['Score'] = score
                student_exists = True
                break
        if not student_exists:
            # Add new student to the leaderboard
            st.session_state.leaderboard.append({"Class": class_option, "Name": name, "Score": score})

# Main area to display the leaderboard for a selected class period
st.title("Mr. Ward's Class Leaderboard")
class_to_display = st.selectbox("Display Leaderboard for Class", options=["Period 1", "Period 2", "Period 3", "Period 4", "Period 5"])

# Display the leaderboard
leaderboard_for_display = get_leaderboard_for_class(class_to_display)
if leaderboard_for_display:
    # Display the crown image for the first place
    crown_url = "URL_TO_YOUR_CROWN_IMAGE"  # Replace with the direct URL to your crown image
    for i, entry in enumerate(leaderboard_for_display):
        if i == 0:  # First place
            st.markdown(f"![crown]({crown_url}) {entry['Name']}: {entry['Score']}", unsafe_allow_html=True)
        else:
            st.write(f"{entry['Name']}: {entry['Score']}")
else:
    st.write("No scores to display for this class.")
