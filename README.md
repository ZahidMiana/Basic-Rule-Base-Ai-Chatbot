# Rule Based Chatbot

A simple, elegant rule-based chatbot built with Python Flask and a modern web interface.

## 🚀 Features

- **Pattern Matching**: Uses regex patterns to understand user input
- **Multiple Responses**: Randomized responses for natural conversation
- **Modern UI**: Beautiful, responsive chat interface
- **Modular Design**: Clean separation of concerns with three Python modules

## 📁 Project Structure

```
rule_based_chatbot/
├── app.py              # Flask web server
├── processor.py        # Input processing logic
├── rules.py            # Patterns and responses
├── templates/
│   └── index.html      # Chat interface
├── static/
│   ├── style.css       # Styling
│   └── script.js       # Frontend logic
└── README.md
```

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Pattern Matching**: Python Regex (re module)

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/rule_based_chatbot.git
   cd rule_based_chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install flask
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open in browser**
   ```
   http://127.0.0.1:5000/
   ```

## 💬 Supported Conversations

| Category | Example Inputs |
|----------|---------------|
| Greetings | hi, hello, hey, hola |
| Wellbeing | how are you, how do you do |
| Identity | what is your name, who are you |
| Gratitude | thank you, thanks |
| Help | help, assist, support |
| Farewell | bye, goodbye, see you |

## 📸 Screenshot

![Chatbot Interface](https://github.com/ZahidMiana/Basic-Rule-Base-Ai-Chatbot/assets/screenshot.png)

The chatbot features a modern, minimalistic design with:
- Clean white background with subtle shadows
- Bot messages on the left (light gray bubbles)
- User messages on the right (blue bubbles)
- Responsive design for mobile devices

## 🎯 How It Works

1. User types a message in the chat window
2. Message is sent to Flask backend via AJAX
3. Processor matches input against regex patterns
4. Random response from matching category is selected
5. Response is displayed in the chat window

## 📸 Screenshot

The chatbot features a modern gradient design with:
- Bot messages on the left (white bubbles)
- User messages on the right (gradient bubbles)
- Responsive design for mobile devices

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
