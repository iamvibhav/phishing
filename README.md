# Phishing Website Detection App

This project uses a machine learning model to detect phishing websites. It provides a simple web interface to check the legitimacy of a given URL.

## Project Structure

*   `app.py`: Contains the Flask web application code.
*   `phishing_detector_model.pkl`: The pre-trained machine learning model for phishing detection.
*   `requirements.txt`: Lists the project's dependencies.
*   `README.md`: This file.

## Getting Started

1.  **Clone the repository (optional, if you have a repo):**
    ```bash
    git clone [https://github.com/your_username/phishing-website-detection-app.git](https://www.google.com/search?q=https://github.com/your_username/phishing-website-detection-app.git)
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app:**
    ```bash
    python app.py
    ```

    This will start the Flask development server.  You'll typically see an address like `http://127.0.0.1:5000/` in your terminal.

## Usage

1.  Open your web browser and go to the address shown in your terminal (e.g., `http://127.0.0.1:5000/`).

2.  Enter the URL you want to check in the provided text box.

3.  Click the "Check" button.

4.  The app will display the prediction (phishing or legitimate) for the given URL.

## Model

The project uses a pre-trained machine learning model (`phishing_detector_model.pkl`) to classify URLs.  The specific model architecture and training details are not included in this README, but would typically be described in more detail in a full project description.

## Dependencies

The `requirements.txt` file lists the Python packages required to run this application.  These typically include Flask and the libraries used for the machine learning model (e.g., scikit-learn, pandas, numpy).

## Contributing

Contributions are welcome!  Please open an issue or submit a pull request.

## License

(Specify the license, e.g., MIT)
