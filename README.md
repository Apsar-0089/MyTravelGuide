# 🌍 AI Travel Guide Assistant

An AI-powered Travel Guide Assistant built using **Python, LangChain, Gradio, and Large Language Models (LLMs)**. It provides personalized travel recommendations based on the user's preferred travel style and personality.

Whether you're an adventure enthusiast, luxury traveller, budget backpacker, or cultural explorer, this assistant helps you discover destinations and plan memorable travel experiences.

## 🚀 Live Demo

**Try the application:** https://mytravelguideassistant.onrender.com

## ✨ Features

- **AI-Powered Travel Recommendations:** Get personalized travel suggestions using Large Language Models.
- **Multiple Travel Personalities:** Choose from four different travel styles.
- **Adventure Explorer:** Discover trekking, hiking, camping, wildlife exploration, and outdoor adventures.
- **Luxury Traveller:** Explore premium destinations, luxury hotels, fine dining, and exclusive experiences.
- **Budget Backpacker:** Find affordable destinations, hostels, local food, and budget-friendly activities.
- **Cultural Explorer:** Discover historical places, architecture, museums, festivals, and local traditions.
- **Multiple LLM Provider Support:** Switch between supported LLM providers through environment variables.
- **Interactive Gradio Interface:** Simple and user-friendly interface for asking travel-related questions.

## 🧠 How It Works

1. The user enters a travel-related question or destination.
2. The user selects a preferred travel personality.
3. The application generates a system prompt based on the selected personality.
4. LangChain sends the system and user messages to the configured LLM.
5. The model generates personalized travel recommendations.
6. The response is displayed through the Gradio interface.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | LLM integration and model initialization |
| OpenAI | LLM provider |
| Google Gemini | LLM provider |
| Gradio | Interactive web interface |
| python-dotenv | Environment variable management |
| Render | Application deployment |

## 📂 Project Structure

```text
AI-Travel-Guide-Assistant/
│
├── app.py                 # Main application
├── requirements.txt       # Project dependencies
├── .env                   # API keys and configuration
├── .gitignore             # Files excluded from Git
└── README.md              # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Travel-Guide-Assistant.git
```

### 2. Navigate to the Project Directory

```bash
cd AI-Travel-Guide-Assistant
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the root directory.

For OpenAI:

```env
MODEL_PROVIDER=openai
MODEL_NAME=gpt-5.5
OPENAI_API_KEY=your_openai_api_key
```

For Google Gemini:

```env
MODEL_PROVIDER=google_genai
MODEL_NAME=your_gemini_model_name
GOOGLE_API_KEY=your_google_api_key
```

Replace the placeholder values with your actual API credentials and a model supported by your provider.

**Important:** Never upload your `.env` file or expose API keys on GitHub.

### 6. Run the Application

```bash
python app.py
```

Open the following URL in your browser:

```text
http://localhost:7860
```

## ☁️ Deployment

The application can be deployed using **Render**.

Deployment steps:

1. Push your project to a GitHub repository.
2. Log in to [Render](https://render.com/).
3. Create a new Web Service.
4. Connect your GitHub repository.
5. Configure the following commands:

**Build Command**

```bash
pip install -r requirements.txt
```

**Start Command**

```bash
python app.py
```

6. Add your API keys and model configuration under Render Environment Variables.
7. Deploy the application.

Render will provide a public URL to access your AI Travel Guide Assistant.

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `MODEL_PROVIDER` | Select the LLM provider (`openai` or `google_genai`) |
| `MODEL_NAME` | Specify the model name |
| `OPENAI_API_KEY` | OpenAI API authentication key |
| `GOOGLE_API_KEY` | Google Gemini API authentication key |
| `PORT` | Port assigned by the deployment platform |

## 🔮 Future Enhancements

- Integrate real-time weather information.
- Add hotel and flight recommendations.
- Include Google Maps integration for destination exploration.
- Generate personalized day-by-day travel itineraries.
- Add estimated travel budgets and expense breakdowns.
- Integrate real-time destination information and travel updates.
- Implement conversation memory for continuous interactions.

## 🎯 Learning Outcomes

Through this project, I explored:

- Integrating multiple LLM providers using LangChain.
- Working with system messages and human messages.
- Designing dynamic system prompts for different AI personalities.
- Managing API keys securely using environment variables.
- Building interactive AI applications using Gradio.
- Deploying Python-based AI applications on Render.

## 👨‍💻 Author

**Apsar Basha**

- GitHub: [@Apsar-0089](https://github.com/Apsar-0089)
- Portfolio: [AI Portfolio](https://ai-portfolio-chatbot-backend.vercel.app/)

---

⭐ If you find this project interesting, consider giving the repository a star!

*Built with Python, LangChain, Gradio, and LLMs.*
