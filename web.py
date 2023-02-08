import streamlit as st
import methods as meth

tasks = meth.get_tasks()

def add_task():
    task = st.session_state["new_task"]
    tasks.append(task + '\n')
    meth.write_tasks(tasks)


st.title("My Todo App")
st.subheader("yeeah")
st.write("This app will make you YEAHHHH")

for i, t in enumerate(tasks):
    checkbox = st.checkbox(t, key=t.strip('\n'))
    if checkbox:
        tasks.pop(i)
        meth.write_tasks(tasks)
        del st.session_state[t.strip('\n')]
        st.experimental_rerun()

st.text_input(label='', placeholder='Enter a todo:',
              on_change=add_task, key='new_task')

print(st.session_state)

