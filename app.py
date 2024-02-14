import streamlit as st

# Initialize session state for the leaderboard
if 'leaderboard' not in st.session_state:
    st.session_state.leaderboard = []

# Sidebar form to add or edit scores
with st.sidebar:
    st.title("Add or Edit Score")
    class_option = st.selectbox("Class", options=["Period 1", "Period 2", "Period 3", "Period 4", "Period 5"], key="class")
    name = st.text_input("Student Name", key="name")
    score = st.number_input("Score", min_value=0, key="score")
    add_button = st.button("Add/Update Score")

    if add_button:
        # Update the leaderboard
        updated = False
        for entry in st.session_state.leaderboard:
            if entry["Class"] == class_option and entry["Name"] == name:
                entry["Score"] = score
                updated = True
                break
        if not updated:
            st.session_state.leaderboard.append({"Class": class_option, "Name": name, "Score": score})

# Main page showing the leaderboard
st.title("Mr. Ward's Class Leaderboard")

class_selection = st.selectbox("Select Class", options=["All Classes"] + ["Period 1", "Period 2", "Period 3", "Period 4", "Period 5"], index=0, key="class_filter")

# Sort and filter the leaderboard
leaderboard = sorted(st.session_state.leaderboard, key=lambda x: (-x["Score"], x["Class"]))
if class_selection != "All Classes":
    leaderboard = [entry for entry in leaderboard if entry["Class"] == class_selection]

# Display the leaderboard with crown for the top scorer
crown_url = "https://github.com/bmwrnnr88/leaderboard/blob/main/crown.jpg?raw=true"  # Replace with the direct URL to your crown image
for i, entry in enumerate(leaderboard):
    if i == 0:  # First place
        st.markdown(f"![crown]({crown_url}) {entry['Class']} - {entry['Name']}: {entry['Score']}", unsafe_allow_html=True)
    else:
        st.write(f'{entry["Class"]} - {entry["Name"]}: {entry["Score"]}')
