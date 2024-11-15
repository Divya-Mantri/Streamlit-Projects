import streamlit as st

#Personal-Profile

st.header(':orange[Personal Profile]')
st.divider()
st.write("I'm a computer science student who's keen on learning and applying what I know. While I'm still getting the hang of programming languages, I'm excited about the chance to work in a team anduse my problem-solving skills. I might not have work experienceyet, but I'm ready to bring my passion and dedication to the table.I'm all about learning and putting my knowledge into action onreal projects.")
st.divider()

#Education
st.header(':orange[Education]')
st.markdown('''| :green-background[Course Name] | :green-background[Institute Name] |:green-background[Duration] |
| ----------- | ----------- | ----------- | 
| Master's of Computer Science | Government College| [2023-Present] |
| Bachelor's of Computer Science | Dayanand College | [2019-2023] |
| 12th Standard| Tagore Senior Secondary School  | [2018-2019] |''')
st.divider()


#Skills
st.header(':orange[Skills]')
st.markdown("""
- **C++ Language** 
- **Basic Python Language**
- **Basic SQl** """)
st.divider()


#Certifications
st.header(':orange[Certifications]')
st.markdown("""- SQL Certification
https://www.codechef.com/certificates/public/7e3a72c

- Python Certification
https://www.codechef.com/certificates/public/aebfd34""")



#---------------------------------------Sidebar Content-------------------------------------------------------

#Title & Designation
st.sidebar.markdown(""" <h1 style="font-size: 50px; color:#00FF00;">Divya</h1>""",unsafe_allow_html=True)
st.sidebar.subheader("*Programming Enthusiast*")
st.sidebar.divider()



#Contact-Details
st.sidebar.info("Contact Details -")
st.sidebar.markdown(""" :e-mail: divya@gmail.com """)
st.sidebar.markdown(""" :telephone_receiver:  +91 1234567899""")
st.sidebar.markdown(""" :round_pushpin: Haryana, India <br> <br>""",unsafe_allow_html=True)


#Hobbies
st.sidebar.info("Hobbies")
st.sidebar.markdown('''
- :rainbow[**Reading**]
- :rainbow[**Listening to Music**]
- :rainbow[**Watching Movies**]
- :rainbow[**Art**] ''')



