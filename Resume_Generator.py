import streamlit as st
from validate_email_address import validate_email
from fpdf import FPDF

#-------------------VALIDATING INPUT FUNCTIONS----------------------------------------------------------

#Function to validate if the Name contains any numbers
def check_name(Name):
        if Name.replace(" ","").isalpha():                  #string.replace(old,new) 
            return True
        else :
            return False

#Function to validate Phone Number should contain only numbers
def check_phone(Phone_No):   
    if(Phone_No.isdigit() and len(Phone_No)==10):
        return True
    else:
        return False
    

#Function to validate Graduation Year 
def check_Grad(Grad_Year):
    if(Grad_Year.isdigit() and len(Grad_Year)==4):
        return True
    else :
        return False


st.title(':rainbow[Resume Generator]')

#-------------------------------INPUT FIELDS ---------------------------------------------

#About Section
with st.container():
    with st.expander("INTRODUCTION"):
        with st.form("About Me"):
            Name=st.text_input("Enter your Full Name", placeholder="Your Name")
            #Validating the Name
            if Name:
                if check_name(Name):
                    st.success("Name is successfully entered!")
                else :
                    st.error("Invalid input!..Please enter the name again...")

            Profile_Summary=st.text_area("About You ",placeholder="Give Profile Summary")

            Email=st.text_input("Enter your Email-id",placeholder="yourname@gmail.com")
            #Validating the Email
            if validate_email(Email):
                st.success("Email successfully entered!")
            else:
                st.error("Invalid Email!")

            Phone_No=st.text_input("Enter your Phone Number",placeholder="1234567809")
            #Validating the Phone Number
            if Phone_No:
                if check_phone(Phone_No):
                    st.success("Phone No. successfully entered!")
                else: 
                    st.error("Invalid input!...Please enter the valid Phone Number")

            Address=st.text_input("Enter your address: ",placeholder="City,State")
            submit_button=st.form_submit_button(':blue[Submit]')

        #Skills Section
    with st.expander("KEY SKILLS"):
        with st.form("Skills & Proficiencies"):
            Skills=st.text_input("Enter your skills (separated by comma)",placeholder="C/C++,HTML,CSS,JS.........")
            Language_Proficiency=st.text_input("Languages You know with their Proficiency",placeholder="English(Basic),Hindi(Fluent)")
            submit_button=st.form_submit_button(':blue[Submit]')

        #Experience Section
    with st.expander("PROFESSIONAL EXPERIENCE"):
        with st.form("Work Experience"):
            Company = st.text_input("Company Name",placeholder="Google/Amazon/Other..")
            Job_title = st.text_input("Job Title",placeholder="SDE I/Data Analyst/Other")
            Job_duration = st.text_input("Duration",placeholder="0000-0000")
            Job_description = st.text_area("Job Description",placeholder="Description of your Work")
            submit_button=st.form_submit_button(':blue[Submit]')

        #Achievements Section
    with st.expander("Achievements/Projects"):
        with st.form("Achievements/Projects"):
            Achievements=st.text_area("Achievements/Projects(Separated by .)",placeholder="Best Coder Award...........")
            submit_button=st.form_submit_button(':blue[Submit]')

        #Education Section
    with st.expander("QUALIFICATIONS"):
        with st.form("Education"):
            Qualification_degree=st.text_input("Enter your Qualification",placeholder="BCA/B.Tech/Other")
            University_Name=st.text_input("Enter your University Name",placeholder="XYZ University")
            Grad_Year=st.text_input("Enter Graduation year",placeholder="0000-0000")
            submit_button=st.form_submit_button(':blue[Submit]')
        
    
#Setting Background Color
st.markdown("""
            <style>
              [data-testid="stMain"]
            {
                background-color:#1c1c1c;
            }
            [data-testid="stExpander"]
            {
                background-color:#e0f7fa;
            }
            [data-testid="stVerticalBlock"]
            {
                background-color:white;
                padding:25px;
            }
            </style>
            """,unsafe_allow_html=True)

#-------------------------RESUME PREVIEW----------------------------------------
if st.button(':blue[Resume Preview]', help="Click to see the preview of your inputs"):
    st.subheader("Resume Preview")
    st.subheader("About Me")
    st.write(f"Name :{Name}")
    st.write(f"Email id :{Email}")
    st.write(f"Contact No.: :{Phone_No}")
    st.write(f"Address :{Address}")
    st.write(f"Profile Summary:{Profile_Summary}")

    st.subheader("Key Skills")
    st.write(f"Skills :{Skills}")
    st.write(f"Lanuages Known :{Language_Proficiency}")

    st.subheader("Experience")
    st.write(f"Company Name:{Company}")
    st.write(f"Job Title:{Job_title}")
    st.write(f"Job Duration:{Job_duration}")
    st.write(f"Job Description:{Job_description}")

    st.subheader("Achievements")
    st.write(f"Achievements/Projects : {Achievements}")

    st.subheader("Qualification")
    st.write(f"Degree:{Qualification_degree}")
    st.write(f"University Name:{University_Name}")
    st.write(f"Graduation Year:{Grad_Year}")
    

    #----------------Defining function to create pdf

def generate_pdf(Name,Email,Phone_No,Address,Profile_Summary,Skills,Language_Proficiency,Company,Job_title,Job_duration,Job_description,Achievements,Qualification_degree,University_Name,Grad_Year):
    #create pdf object
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Times",size=12)
    # pdf.set_right_margin(20)  # Right margin of 20 units
   


    #Title
    pdf.set_font("Times",style="B",size=30)
    pdf.cell(200,10,txt=f"{Name}",align="C")
    pdf.ln(15)

    #Personal Details
    pdf.set_font("Times",size=10)
    pdf.cell(60,10,txt=f"{Address}",align="C")
    pdf.cell(10,10,txt="|",align="C")
    pdf.cell(60,10,txt=f"{Email}",align="C")
    pdf.cell(10,10,txt="|",align="C")
    pdf.cell(60,10,txt=f"{Phone_No}",align="C")
    pdf.ln(20)

    #About Section
    pdf.set_font("Times",size=14,style="B")
    pdf.cell(200,10,txt="Professional Summary",align="L",ln=True,border="B")
    pdf.set_font("Times",size=12)
    pdf.multi_cell(200,10,txt=f"{Profile_Summary}",align="L")
    pdf.ln(5)

    #Key Skills
    pdf.set_font("Times",size=14,style="B")
    pdf.cell(200,10,txt="Key Skills",align="L",ln=True,border="B")
    pdf.set_font("Times",size=12)
    for skill in Skills.split(","):
        pdf.cell(200,10,txt=f" {skill.strip()}",ln=True,align="L")        #strip() to removes any extra space from the beginning and end of the text
    pdf.ln(2)
    
    pdf.set_font("Times",size=14,style="B")
    pdf.cell(200,10,txt="Language Proficiency",align="L",ln=True,border="B")
    pdf.set_font("Times",size=12)
    for language in Language_Proficiency.split(","):
        pdf.cell(200,10,txt=f" {language.strip()}",ln=True,align="L")  
        
    pdf.ln(5)

    #Work Experience
    if Company.strip():
        pdf.set_font("Times",size=14,style="B")
        pdf.cell(200,10,txt="Experience",ln=True,border="B",align="L")
        pdf.set_font("Times",size=12,style="B")
        pdf.cell(200,10,txt=f"{Job_title}",ln=True,align="L")
        pdf.set_font("Times", size=12, style="") 
        pdf.cell(200,10,txt=f"{Company}",align="L")
        pdf.cell(20,10,txt=f"{Job_duration}",align="R")
        pdf.multi_cell(200,10,txt=f"{Job_description}",align="L")
        pdf.ln(5)

    #Achievements
    pdf.set_font("Times",size=14,style="B")
    pdf.cell(200,10,txt="Achievements/Projects",ln=True,border="B",align="L")
    pdf.set_font("Times",size=12,style="")
    for Achievements in Achievements.split("."):
        pdf.cell(200,10,txt=f"{Achievements.strip()}",ln=True,align="L")
    pdf.ln(5)


    #Education Section
    pdf.set_font("Times",size=14,style="B")
    pdf.cell(200,10,txt="Education",ln=True,border="B",align="L")
    pdf.set_font("Times",size=12,style="B")
    pdf.cell(200,10,txt=f"{University_Name}",align="L",ln=True)
    pdf.set_font("Times", size=12, style="") 
    pdf.cell(100,10,txt=f"{Qualification_degree}",align="L")
    pdf.cell(100,10,txt=f"{Grad_Year}",align="R",ln=True)
    pdf.ln(5)

    pdf.output("resume.pdf")

if st.button(':blue[Generate Resume]',help="Click to Generate your Resume!"):
    generate_pdf(Name,Email,Phone_No,Address,Profile_Summary,Skills,Language_Proficiency,Company,Job_title,Job_duration,Job_description,Achievements,Qualification_degree,University_Name,Grad_Year)
    with open("resume.pdf","rb") as file:
        st.download_button("Download your Resume",file,"resume.pdf",help="Click to Download Resume")

