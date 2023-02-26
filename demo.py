import streamlit as st
import pickle
import os

#load the model from the pickle file
model = pickle.load(open('optimum_model.pkl','rb'))


# create a function that will take the inputs from the user
def predict_default(YW, YP, WPP, WPA, CROPPING_INTENSITY,
       YW_CV_TEMPORAL, YP_CV_TEMPORAL, CLIMATEZONE,
       AREA_IN_CLIMATEZONE_HA):
    
    # Pre-processing user input
    YW = float(YW)
    YP = float(YP)
    WPP = float(WPP)
    WPA = float(WPA)
    CROPPING_INTENSITY = float(CROPPING_INTENSITY)
    YW_CV_TEMPORAL = float(YW_CV_TEMPORAL)
    YP_CV_TEMPORAL = float(YP_CV_TEMPORAL)
    CLIMATEZONE = int(CLIMATEZONE)
    AREA_IN_CLIMATEZONE_HA = int(AREA_IN_CLIMATEZONE_HA)
    

 
    # Making predictions 
    prediction = model.predict( 
        [[YW, YP, WPP, WPA, CROPPING_INTENSITY,
       YW_CV_TEMPORAL, YP_CV_TEMPORAL, CLIMATEZONE,
       AREA_IN_CLIMATEZONE_HA]])

    # set prediction whole number integer
    prediction = float(prediction)

    return prediction

# main function
def main():
    st.title('''Sub-Saharan Africa yield Predictor :sparkles:''')
    YW = st.number_input('Water-limited yield potential')
    YP = st.number_input('Yield potential')
    WPP = st.number_input('water productivity levels productivity potential')
    WPA = st.number_input('water productivity levels productivity avarage')
    CROPPING_INTENSITY =st.number_input('Cropping intensity')
    YW_CV_TEMPORAL = st.number_input('temporal coefficient of variation for Water-limited yield potential')
    YP_CV_TEMPORAL = st.number_input('temporal coefficient of variation for yield potential')
    CLIMATEZONE = st.number_input('Climate zone')
    AREA_IN_CLIMATEZONE_HA = st.number_input('Area in climate zone (ha)')
    button = st.button('Predict')
    if button:
        prediction = predict_default(YW, YP, WPP, WPA, CROPPING_INTENSITY,
       YW_CV_TEMPORAL, YP_CV_TEMPORAL, CLIMATEZONE,
       AREA_IN_CLIMATEZONE_HA)
        st.success('The tool recommends {}'.format(prediction))

if __name__ == '__main__':
    main()
