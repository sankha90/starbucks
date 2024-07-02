import streamlit as st
from PIL import Image

st.title("Subhra Sankha Sardar 🎆")
 
st.write("")  # Add a gap
st.write("")  # Add a gap
with st.expander("What's my origin story 🎓"):
    st.divider()  # Add a divider
    st.write("● I am a seasoned Data Scientist with over 10 years of experience, \
         currently a part of financial crime analytics/risk at Axis Bank.")
    st.write("● I hold a PostGraduate Diploma in Business Analytics from IIM Calcutta, IIT Kharagpur, and ISI Kolkata.")
    st.write("● At Axis Bank, I developed a transaction monitoring framework that prevented fraudulent transactions \
         worth 15 million INR, designed a DTM rules framework reducing false positive alerts, and \
         automated a credit conversion factor, significantly reducing man-hours.")
    st.write("● Proficient in Python, SQL, VBA, PySpark, scikit-learn, Spark MLlib, Pandas, and NLP, \
         I am also experienced in data visualization tools like Matplotlib and Seaborn.")
    st.write("● My leadership experience includes managing a functional team, mentoring junior members, \
         and facilitating cross-functional collaborations.")
         
st.write("")  # Add a gap
st.write("")  # Add a gap
           
with st.expander("Why I'm the Perfect Blend ☕🍪"):
    st.divider()  # Add a divider
    st.write("To demonstrate this I have prepared a little analysis where we will look at the this year's performance and some social media recommendation and then possible recommendations.")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Stores", "421")
    col2.metric("New Stores", "95")
    col3.metric("Cities", "61")
    col4.metric("Target of Total Stores ", "1000")
    st.write("")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Revenue in FY23", "₹1087 Cr")
    col2.metric("Net Loss", "₹25 Cr")
    col3.metric("Revenue in FY24", "₹1000 Cr")
    col4.metric("Net Loss", "₹81 Cr")

    st.write("")

    st.write("I wanted to explore despite a pretty good growth why the Net loss is increasing and found out a few reaons. \
             I have classified them as 'organizational' , 'social' and 'market' risks.")
    
    st.warning('Organizational Risk', icon="⚠️")
    st.write("Tata Starbucks saw an 84.45% jump in advertising and promotional costs to ₹34.05 crore in FY23, as it invested more to drive brand awareness and attract customers")
    st.write("The company paid a royalty of ₹76.83 crore to its parent Starbucks Corporation in FY23, which added to its overall expenses")

    st.info('Market Risk', icon="ℹ️")
    st.write("Starbucks cited 'weak demand for QSRs in general' as the primary reason for the widening losses. \
             This suggests a broader industry-wide slowdown in consumer demand for cafe and restaurant chains.")
    st.write("While Starbucks has introduced more affordable menu options, it may not have been able to fully offset the impact of rising input costs and other overheads through higher prices, leading to margin pressures.")

    st.error('Social Risk', icon="🚨")
    st.write("StarbucksIndia youtube channel has less than 10 videos , StarbucksIndia Facebook has 1M followers but the engagement as really low \
             On twitter the engegemt is low as well , on top of that they have been at the forefront of controversies with ads like It starts with your name. \
             Now the ad is not there but the internet never forgets and an analysis of the youtube comments shows that :"
             )
    st.image('images/output.png', caption='Trend of sentiment on youtube over time')
    st.image('images/sentiment.png', caption='sentiment on youtube')

    st.success('Few recommendations', icon="💡")
    st.write("Improve advertising: Invest in advertising on popular platforms like Meta and Instagram to attract younger customers")
    st.write("Expand store network in premium locations")
    st.write("Introduce more affordable options Tata Starbucks has revamped its menu to include more affordable, \
             Indian-inspired options like masala chai, filter coffee, smaller beverage cups, street-style sandwiches , \
             milkshakes and bite-sized snacks to appeal to a wider audience. This helped drive 71% revenue growth in FY22")
    st.write("Focus on delivery and takeaway: Tata Starbucks is seeing 35% same-store sales compared to pre-COVID levels, \
             with delivery now contributing 11-12% of revenue. Optimizing delivery operations can help boost margins")
    st.write("Enhance the in-store experience: In India, consumers frequent cafes for the ambience and to spend time, not just for coffee.\
             Improving the in-store experience can attract more customers.")
    
st.write("")  # Add a gap
st.write("")  # Add a gap

with st.expander("Vision for Starbucks 🌟"):
    st.divider()  # Add a divider
    st.write("### Establishing the Data Science Function")
    st.write("My vision for establishing the Data Science function at Starbucks involves integrating data-driven decision-making processes across all departments. This includes leveraging data analytics to optimize marketing strategies, enhance customer experiences, and streamline operations.")
    
    st.write("### Optimizing Loyalty Marketing Initiatives")
    st.write("I plan to use predictive analytics to better understand customer preferences and behavior, enabling more personalized marketing campaigns that drive customer loyalty and retention.")
    
    st.write("### Enhancing Digital Customer Experience")
    st.write("By analyzing customer feedback and interaction data, I aim to identify areas for improvement in the digital experience, ensuring a seamless and satisfying journey for every customer.")
    
    st.write("### Network Planning and Site Optimization")
    st.write("Using geospatial analysis and predictive modeling, I will identify optimal locations for new stores, ensuring maximum reach and profitability.")
    
   



    




    














               

