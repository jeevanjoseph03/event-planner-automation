# Event Planner Automation with CrewAI

An intelligent multi-agent system that automates event planning using CrewAI framework. This project demonstrates the power of AI agents working together to handle venue coordination, logistics management, and marketing communications.

## 🚀 Features

- **Venue Coordination**: AI agent finds and books appropriate venues based on event requirements
- **Logistics Management**: Handles catering, equipment, and other event logistics
- **Marketing & Communications**: Creates marketing strategies and engagement plans
- **Human-in-the-loop**: Interactive feedback system for better decision making
- **Structured Output**: Generates JSON and Markdown reports

## 🏗️ Architecture

This project uses three specialized AI agents:

1. **Venue Coordinator Agent**: Searches and evaluates venues using web scraping and search tools
2. **Logistics Manager Agent**: Coordinates catering, equipment, and operational requirements
3. **Marketing Communications Agent**: Develops marketing strategies and attendee engagement plans

## 🛠️ Tech Stack

- **CrewAI**: Multi-agent orchestration framework
- **OpenAI GPT-3.5-turbo**: Language model for AI agents
- **Serper API**: Web search capabilities
- **Pydantic**: Data validation and structured outputs
- **Python**: Core programming language

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Serper API key

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/jeevanjoseph03/event-planner-automation.git
cd event-planner-automation
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your API keys to `.env`

## 🔧 Configuration

Create a `.env` file with your API keys:

```env
OPENAI_API_KEY=your_openai_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

### Getting API Keys

- **OpenAI API Key**: Get it from [OpenAI Platform](https://platform.openai.com/api-keys)
- **Serper API Key**: Get it from [Serper.dev](https://serper.dev/)

## 🎯 Usage

Run the event planner automation:

```bash
python main.py
```

The system will:
1. Start with venue coordination
2. Ask for your feedback on venue options
3. Run logistics and marketing tasks in parallel
4. Generate output files with results

### Customizing Event Details

Modify the `event_details` dictionary in [`main.py`](main.py):

```python
event_details = {
    'event_topic': "Your Event Name",
    'event_description': "Event description",
    'event_city': "Target City",
    'tentative_date': "YYYY-MM-DD",
    'expected_participants': 100,
    'budget': 10000,
    'venue_type': "Conference Hall"
}
```

## 📁 Project Structure

```
event-planner-automation/
├── main.py                 # Main application file
├── utils.py                # Utility functions for API keys
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in repo)
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation
├── venue_details.json     # Generated venue information
└── marketing_report.md    # Generated marketing report
```

## 📄 Output Files

The system generates two main output files:

- **`venue_details.json`**: Structured venue information including name, address, capacity, and booking status
- **`marketing_report.md`**: Comprehensive marketing strategy and attendee engagement plan

## 🤖 Agents Overview

### Venue Coordinator
- **Role**: Find and secure appropriate venues
- **Tools**: Web search and scraping capabilities
- **Output**: Structured venue details in JSON format

### Logistics Manager
- **Role**: Handle all event logistics
- **Tools**: Research capabilities for vendors and equipment
- **Output**: Logistics confirmation and arrangements

### Marketing Communications Agent
- **Role**: Create marketing strategies
- **Tools**: Market research and communication planning
- **Output**: Marketing report in Markdown format

## 🔄 Workflow

1. **Sequential Execution**: Venue task runs first with human feedback
2. **Parallel Execution**: Logistics and marketing tasks run simultaneously
3. **Human Input**: System asks for approval at key decision points
4. **File Output**: Results saved as structured files

## 🚨 Troubleshooting

### Common Issues

1. **Model Access Error**: Make sure you have access to GPT-3.5-turbo model
2. **API Key Error**: Verify your API keys are correctly set in `.env`
3. **Missing Files**: Ensure all dependencies are installed via `requirements.txt`

### Debug Mode

Set `verbose=True` in agents and crew for detailed logging.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and commit: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Course

This project was created as part of the **"Multi AI Agent Systems with CrewAI"** course, demonstrating practical applications of multi-agent AI systems.

## 🙏 Acknowledgments

- CrewAI team for the amazing framework
- OpenAI for providing the language models
- Serper for web search capabilities

---

**Note**: This is a demo project for educational purposes. Make sure to secure your API keys and never commit them to version control.