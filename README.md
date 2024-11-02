# FashChat: Your Timeless Fashion Analyzer

Welcome to **FashChat**, a fashion-forward tool that blends AI with style! FashChat helps you analyze outfits, explore makeup looks, and dive deep into iconic fashion moments from movies or celebrity appearances. Whether you want styling tips, outfit recommendations, or insight into current trends, FashChat is your go-to fashion advisor.

## Features

- **Outfit Analysis**: Upload an image of any outfit to get expert insights, trend checks, and styling suggestions.
- **Makeup Look Insights**: Discover tips and tricks to recreate a makeup look, personalized for you.
- **Movie/Celebrity Fit Analysis**: Analyze an iconic look from movies or celebrities and receive recommendations on where to find similar pieces.

## Installation Guide

To set up FashChat on your local machine, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/Usha66/fashchat.git
cd fashchat
```

### 2. Create a Virtual Environment (Optional but Recommended)

This keeps dependencies isolated to the project.

```bash
python -m venv fashchat-env
source fashchat-env/bin/activate  # On Windows: fashchat-env\Scripts\activate
```

### 3. Install Requirements

Ensure you have `pip` installed, then run:

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root to store your Google API key:

```plaintext
GOOGLE_API_KEY=your_google_api_key_here
```

### 5. Run the App

Launch the Streamlit app with the following command:

```bash
streamlit run fashchat.py
```

### 6. Access FashChat

After running the above command, open your browser and go to:

```plaintext
http://localhost:8501
```

**Note:** If you need to use a different port, add the `--server.port` flag:

```bash
streamlit run fashchat.py --server.port 8502
```

## Project Structure

```plaintext
├── fashchat.py          # Main application script
├── requirements.txt     # List of dependencies
├── .env                 # Environment variables (keep it secret!)
├── README.md            # Project documentation
└── assets               # Folder for any additional resources (e.g., logo image)
```

## Usage

1. **Outfit Analyzer**:
   - Upload an outfit image.
   - Choose analysis options (e.g., Trendiness Check, Styling Tips).
   - Click "Analyze Outfit" to receive feedback on your uploaded image.

2. **Makeup Look Insights**:
   - Upload a close-up image for makeup analysis.
   - Provide any specific insights or focus areas you want in the prompt.
   - Click "Analyze Makeup" to get detailed makeup insights.

3. **Movie/Celebrity Fit Analyze**:
   - Enter the movie or celebrity name.
   - Optionally, upload an image of the character or celebrity.
   - Select analysis options (e.g., Trend Analysis, Outfit Availability Suggestions).
   - Click "Analyze Movie/Celebrity Fit" to explore the outfit.

## Contributing

Contributions are welcome! Feel free to fork the project and create pull requests to improve FashChat.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---
