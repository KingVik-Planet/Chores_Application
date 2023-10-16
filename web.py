import streamlit as st
import functions

chores = functions.get_chores()


def add_chore():
    chore = st.session_state["new_chore"] + "\n"
    chores.append(chore)
    functions.write_chores(chores)




st.title("The Chores List App")
st.subheader("Write the Chores of the day")
st.write("This app is created to give Daily Chores and Increase Productivity")

for index, chore in enumerate(chores):

    checkbox = st.checkbox(chore, key = chore)
    if checkbox:
        chores.pop(index)
        functions.write_chores(chores)
        del st.session_state[chore]
        st.experimental_rerun()



st.text_input(label= "", placeholder= "Add a Chore...",
              on_change=add_chore, key = "new_chore")

st.session_state