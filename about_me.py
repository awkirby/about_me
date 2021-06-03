"""
This script is used to host an interactive, shareable version of my resume
"""
import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.title('Alex Kirby\'s Interactive Resume')
st.subheader('Data Scientist, Technical Project Manager, Nuclear Engineer and Polymath')

int1, int2 = st.beta_columns(2)

with int1:
    st.header('About me')
    st.markdown('I am an engineer with over 8 years experience in data analysis, simulation and technical project'
                ' management at a world class engineering firm. '
                'I pride myself on delivering projects end-to-end on time and to quality. '
                'Complex problems don’t faze me as I deal with them every day. '
                'I have sought new challenges throughout my career and am comfortable delivering them '
                'with a high degree of independence. '
                'I am a strong communicator, who enjoys working with others to come up with ideas and solve problems. ')

    st.header('Switzerland')
    st.markdown('In 2021 I moved to Switzerland to support my wife\'s career. '
                'This has given me a unique opportunity to broaden my career and focus fully on data science and '
                'data analytics (the favourite part of my job!) ')
    st.markdown('The fantastic scenery, chocolate and proximity to ski resorts is not bad either!')

with int2:
    st.image('alex+benoit_wallensee.jpg', 'Enjoying Switzerland', width=300)

line = '-' * 50

st.write(line)

st.header('Work Experience')

work1, work2, work3 = st.beta_columns(3)

with work1:
    st.subheader('Rolls-Royce, 2015-2020, United Kingdom')

    st.markdown('I worked in data analytics, modelling and simulation for the company\'s nuclear business. '
                'My main focus throughout my time was in using data to return value to the business and our customer. '
                'I achieved this through inter-disciplinary projects that leveraged new data from literature or '
                'other departments, development of tools in Python, Matlab or the Unix shell (awk, grep etc.), and '
                'innovative approaches to analysing simulation data. '
                'Over that time, I took on increasingly senior projects working independently at first, '
                'before starting to work with graduates and later a team of 4 other engineers. ')
    st.markdown('See my resume or [Linkedin](https://www.linkedin.com/in/alexwkirby/) for more details')

    # Function to avoid writing st.markdown for every new line!
    def new_line(text):
        lines = text.split("  ")
        for sentence in lines:
            st.markdown(sentence)

    skills = ("**Skills:**  * Data Analytics  * Software Development  * Code Verification and Validation  " +
                "* Statistical Methods Development  * Technical Project Management  * Technical Communication  " +
                "* Coding (Python, Matlab, Unix Shell, Fortran, SQL, Git)  * LEAN Process Improvement")
    new_line(skills)

with work2:
    st.image('D-class.jpg', 'First I worked on this...', width=400)

    value_add = {"2017": 10, "2018": 5, "2019": 600, "2020": 6}
    df_value_add = pd.DataFrame.from_dict(value_add, orient='index', columns=['Customer Value Added (£m)'])

    st.bar_chart(df_value_add)
    st.markdown("##### Delivering a project with £600m+ in benefits ruins the bar chart...")

with work3:
    st.image('rr-smr.jpg', '... then this', use_column_width='auto')

st.subheader('nucleargraduate, 2013-2015, United Kingdom')

grad1, grad2, grad3 = st.beta_columns(3)

with grad1:
    st.markdown("The nucleargraduate scheme is a multi-disciplinary training scheme that included placements "
                "outside my sponsor company, and development of soft-skills in leadership, communications and "
                "project management.")

    st.markdown("As part of the scheme I took on 4 different roles at 3 different companies all over the UK.  " +
                "I also completed training in the UK and Europe on a range of topics, and acted as an ambassador" +
                " for Science, Technology, Engineering and Mathematics at UK schools (running afternoon science " +
                "classes and career days")

    st.markdown("I have applied the flexibility and adaptability I developed during the scheme throughout my" +
                "career.  " +
                " Giving me the confidence to take on projects in different areas and disciplines.")

with grad2:
    st.image("graduate_work_locations.jpg",
             "Working all over the UK")

    st.markdown("##### [More Details]"
                "(https://www.google.com/maps/d/u/0/edit?mid=1NDFfBxakxr0z4w1OXK4QinJBvGQpAA3x&usp=sharing)")

with grad3:
    st.image("graduate_training_locations.jpg",
             "Training all over Europe")

    st.markdown("##### [More Details]"
                "(https://www.google.com/maps/d/u/0/edit?mid=1vtYC-WFr68J5N5FQw-a42WIwP9CAZe4c&usp=sharing)")

st.write(line)

st.header('Education')

ed1, ed2 = st.beta_columns(2)

with ed1:
    st.subheader("AiCore, Data Science and Machine Learning Fellowship, February – July 2021  ")

    st.markdown("Intensive 18-week course in the application and deployment of code, "
                "covering Python, SQL and Bash coding, collaboration and change control (Github), "
                "cloud services (AWS), exploratory data analysis and processing (Pandas, Selenium and Jupyter-Labs), "
                "machine learning (Scikit-learn, Statsmodels, Pytorch), and neural networks (PyTorch).  " +
                "https://github.com/awkirby")

    st.subheader("MIT, Machine Learning with Python: from Linear Models to Deep Learning, February – May 2021")

    st.markdown("Principles and algorithms for turning training data into effective automated predictions.  " +
                "This included building common algorithms from first principles in Python"
                "and applying tools such as Pytorch to solve image classification problems.  " +
                "Taught through edX with identical course content to Master’s level module at MIT.")

    st.subheader("Imperial College London, 2009-2013")

    st.markdown("Chemical with Nuclear Engineering (MEng), Upper Second-Class Honours (3.7 GPA equivalent)")




