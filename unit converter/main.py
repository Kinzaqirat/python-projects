import streamlit as st


def temperature(from_unit, to_unit ,value):
    if from_unit =="°C" and to_unit =="°F":
        result = (value * 9/5)+ 32
        
    elif from_unit =="°F" and to_unit =="°C" :

        result = (value - 32) * 5/9
    elif from_unit=="°C" and to_unit =="°K":
        result= value + 273.15
    elif from_unit=="°F" and to_unit =="°K":
        result=  (value - 32) * 5/ 9 + 273.15
          
    else:
        result = value
    return result        

def mass(from_unit, to_unit ,value):
    units = {
    "Kilograms": 1,       
    "Grams":  0.001 ,
    "Pounds": 0.453592 ,
    "Ounces":  0.0283495 
} 
    result = value * units[from_unit] / units[to_unit]
    return result


def pressure_converter(from_unit, to_unit, value):
    units = {
        "Pascals": 1,
        "Hectopascals": 100,
        "Kilopascals": 1000,
        "Bar": 100000
    }
    result = value * units[from_unit] / units[to_unit]
    return result


def kilometer(from_unit, to_unit, value):
    units={
        "Kilometers": 1,       
    "Meters":  0.001 ,
    "Centimeters": 0.00001 ,
    "Millimeters":  0.000001,
    "Miles":  0.621371 ,
    "Yards":  0.0009144,
    "Feet":  0.0003048 ,
    "Inches":  0.0000254 
    }
    result = value * units[from_unit] / units[to_unit]
    return result




# Streamlit UI
st.set_page_config(page_title="Unit Converter")
st.markdown(
    """
    <style>
    .stApp{
       background-color:#FFE5B4;
       color:white;
          }
          </style>
          """,
          unsafe_allow_html=True
)


st.title("Unit Converter 🔢✅")

category=st.selectbox("Select ",["Mass","Tempreature","Pressure","Kilometers"])


if category == "Kilometers":
    from_unit = st.selectbox("From", ["Meters", "Kilometers", "Feet", "Miles","Centimeters","Millimeters","Yards","Inches"])
    to_unit = st.selectbox("To", ["Meters", "Kilometers", "Feet", "Miles","Centimeters","Millimeters","Yards","Inches"])
    value = st.number_input("Enter Value")
    result = kilometer(from_unit, to_unit, value)
    st.write(f"<p style='font-size:44px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)


elif category == "Tempreature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit",])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit","Kelvin"])
    value = st.number_input("Enter Value")
    result = temperature(from_unit, to_unit, value)
    st.write(f"<p style='font-size:44px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)



elif category == "Pressure":
    from_unit = st.selectbox("From", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
    to_unit = st.selectbox("To", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
    value = st.number_input("Enter Value")
    result = pressure_converter(from_unit, to_unit, value)
    st.write(f"<p style='font-size:24px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

elif category == "Mass":
    from_unit = st.selectbox("From", ["Kilograms","Grams","Pounds","Ounces"])
    to_unit = st.selectbox("To", ["Kilograms","Grams","Pounds","Ounces"])
    value = st.number_input("Enter Value")
    result = mass(from_unit, to_unit, value)
    st.write(f"<p style='font-size:44px;'>{value} {from_unit} is equal to {result:.2f} {to_unit}</p>", unsafe_allow_html=True)

st.write("---------------------------------")
st.write("Thanks for using 😊")
