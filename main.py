import warnings
warnings.filterwarnings('ignore')
from crewai import Agent, Crew, Task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from pydantic import BaseModel
import os
import json
from pprint import pprint
from utils import get_openai_api_key, get_serper_api_key

# Set up API keys and environment
openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'  
os.environ["SERPER_API_KEY"] = get_serper_api_key()

# Initialize the tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

# Define Pydantic model for venue details
class VenueDetails(BaseModel):
    name: str
    address: str
    capacity: int
    booking_status: str

# Create Agents
venue_coordinator = Agent(
    role="Venue Coordinator",
    goal="Identify and book an appropriate venue based on event requirements",
    tools=[search_tool, scrape_tool],
    verbose=True,
    backstory=(
        "With a keen sense of space and understanding of event logistics, "
        "you excel at finding and securing the perfect venue that fits the event's theme, "
        "size, and budget constraints."
    )
)

logistics_manager = Agent(
    role='Logistics Manager',
    goal="Manage all logistics for the event including catering and equipment",
    tools=[search_tool, scrape_tool],
    verbose=True,
    backstory=(
        "Organized and detail-oriented, you ensure that every logistical aspect of the event "
        "from catering to equipment setup is flawlessly executed to create a seamless experience."
    )
)

marketing_communications_agent = Agent(
    role="Marketing and Communications Agent",
    goal="Effectively market the event and communicate with participants",
    tools=[search_tool, scrape_tool],
    verbose=True,
    backstory=(
        "Creative and communicative, you craft compelling messages and "
        "engage with potential attendees to maximize event exposure and participation."
    )
)

# Create Tasks
venue_task = Task(
    description="Find a venue in {event_city} that meets criteria for {event_topic}.",
    expected_output="All the details of a specifically chosen venue you found to accommodate the event.",
    human_input=True,
    output_json=VenueDetails,
    output_file="venue_details.json",
    agent=venue_coordinator
)

logistics_task = Task(
    description="Coordinate catering and equipment for an event with {expected_participants} participants on {tentative_date}.",
    expected_output="Confirmation of all logistics arrangements including catering and equipment setup.",
    human_input=True,
    async_execution=True,
    agent=logistics_manager
)

marketing_task = Task(
    description="Promote the {event_topic} aiming to engage at least {expected_participants} potential attendees.",
    expected_output="Report on marketing activities and attendee engagement formatted as markdown.",
    async_execution=True,
    output_file="marketing_report.md",
    agent=marketing_communications_agent
)

# Create the Crew
event_management_crew = Crew(
    agents=[venue_coordinator, logistics_manager, marketing_communications_agent],
    tasks=[venue_task, logistics_task, marketing_task],
    verbose=True
)

# Define event details
event_details = {
    'event_topic': "Tech Innovation Conference",
    'event_description': "A gathering of tech innovators and industry leaders to explore future technologies.",
    'event_city': "San Francisco",
    'tentative_date': "2024-09-15",
    'expected_participants': 500,
    'budget': 20000,
    'venue_type': "Conference Hall"
}

# Run the crew
if __name__ == "__main__":
    print("Starting Event Planning Automation...")
    result = event_management_crew.kickoff(inputs=event_details)
    print("\nEvent planning completed!")
    
    # Display venue details
    print("\n=== Venue Details ===")
    try:
        with open('venue_details.json') as f:
            venue_data = json.load(f)
        pprint(venue_data)
    except FileNotFoundError:
        print("venue_details.json not found yet")
    
    # Display marketing report
    print("\n=== Marketing Report ===")
    try:
        with open('marketing_report.md', 'r') as f:
            marketing_content = f.read()
        print(marketing_content)
    except FileNotFoundError:
        print("marketing_report.md not found yet")
