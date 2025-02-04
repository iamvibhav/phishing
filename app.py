import streamlit as st
import pandas as pd
import numpy as np
import os

# Page configuration
st.set_page_config(page_title="Phishing Website Detector", page_icon="🕵️")

# Diagnostic information
st.title("🕵️ Phishing Website Detector - Diagnostic Info")

# Check current working directory and list files
st.write("Current Working Directory:", os.getcwd())
st.write("Files in current directory:", os.listdir())

# Try to load the model with error handling
try:
    import joblib
    
    @st.cache_resource
    def load_model():
        # Try different paths
        possible_paths = [
            'phishing_detector_model.pkl',
            './phishing_detector_model.pkl',
            '../phishing_detector_model.pkl'
        ]
        
        for path in possible_paths:
            try:
                st.write(f"Attempting to load model from: {path}")
                model = joblib.load(path)
                st.success(f"Model successfully loaded from {path}")
                return model
            except Exception as e:
                st.warning(f"Failed to load model from {path}: {e}")
        
        raise ValueError("Could not load model from any attempted path")

    model = load_model()

    # Rest of your original app code follows...
    # (Keep the original get_user_input, predict_phishing, and main functions)

except Exception as e:
    st.error(f"Critical Error: {e}")
    st.write("Please check model file and deployment setup")
# Title and description
st.title("🕵️ Phishing Website Detection")
st.write("Enter website characteristics to determine if it's a potential phishing site.")

# Function to create input fields
def get_user_input():
    # We'll create input fields for a subset of most important features
    input_data = {}
    
    st.sidebar.header("Website Characteristics")
    
    # Numeric features (you might want to adjust ranges based on your data)
    numeric_features = [
        'length_url', 'nb_dots', 'nb_hyphens', 'nb_at', 'nb_qm', 
        'nb_subdomains', 'nb_redirection', 'nb_external_redirection', 
        'phish_hints', 'nb_hyperlinks', 'domain_registration_length'
    ]
    
    for feature in numeric_features:
        input_data[feature] = st.sidebar.number_input(
            feature.replace('_', ' ').title(), 
            min_value=0, 
            value=0
        )
    
    # Ratio features
    ratio_features = [
        'ratio_digits_url', 'ratio_extHyperlinks', 
        'ratio_intRedirection', 'safe_anchor'
    ]
    
    for feature in ratio_features:
        input_data[feature] = st.sidebar.slider(
            feature.replace('_', ' ').title(), 
            min_value=0.0, 
            max_value=1.0, 
            value=0.0, 
            step=0.01
        )
    
    # Binary/Categorical features
    binary_features = [
        'ip', 'https_token', 'shortening_service', 
        'login_form', 'external_favicon'
    ]
    
    for feature in binary_features:
        input_data[feature] = st.sidebar.selectbox(
            feature.replace('_', ' ').title(), 
            [0, 1]
        )
    
    return pd.DataFrame([input_data])

# Main prediction function
def predict_phishing(input_data):
    # Ensure all columns match training data
    prediction = model.predict(input_data)
    proba = model.predict_proba(input_data)
    
    return prediction[0], proba[0]

# Prediction section
def main():
    # Get user input
    input_data = get_user_input()
    
    # Prediction button
    if st.sidebar.button('Detect Phishing'):
        # Make prediction
        prediction, probabilities = predict_phishing(input_data)
        
        # Display results
        if prediction == 1:
            st.error("🚨 PHISHING WEBSITE DETECTED!")
            st.warning(f"Phishing Probability: {probabilities[1]:.2%}")
        else:
            st.success("✅ LEGITIMATE WEBSITE")
            st.info(f"Legitimate Probability: {probabilities[0]:.2%}")
        
        # Additional insights
        st.subheader("Prediction Details")
        st.write("Input Characteristics:")
        st.dataframe(input_data)

if __name__ == '__main__':
    main()