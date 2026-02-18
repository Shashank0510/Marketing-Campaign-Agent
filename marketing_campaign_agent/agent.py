import os

try:
    from dotenv import load_dotenv
    load_dotenv()

    MODEL_NAME = os.environ.get("GOOGLE_GENAI_MODEL", "gemini-2.0-flash")
except ImportError:
    print("Warning: python-dotenv not installed. Ensure API key is set")
    MODEL_NAME = "gemini-2.5-flash"



from google.adk.agents import LlmAgent,SequentialAgent
from google.adk.tools import google_search

from marketing_campaign_agent.instructions import (
    MARKET_RESEARCH_INSTRUCTION,
    MESSAGING_STRATEGIST_INSTRUCTION,
    AD_COPY_WRITER_INSTRUCTION,
    VISUAL_SUGGESTER_INSTRUCTION,
    FORMATTER_INSTRUCTION,
    CAMPAIGN_ORCHESTRATOR_INSTRUCTION,
    VISUAL_GENERATION_INSTRUCTION
    

)

market_research_agent = LlmAgent (
    name = "MarketResearcher",
    model = MODEL_NAME,
    instruction = MARKET_RESEARCH_INSTRUCTION,
    tools = [google_search],
    output_key ="market_research_summary"
)


messaging_strategist_agent = LlmAgent(
    name="MessagingStrategist",
    model=MODEL_NAME,  # Using environment variable
    instruction=MESSAGING_STRATEGIST_INSTRUCTION,
    output_key="key_messaging" 
)

ad_copy_writer_agent = LlmAgent(
    name="AdCopyWriter",
    model=MODEL_NAME,  
    instruction=AD_COPY_WRITER_INSTRUCTION,
    output_key="ad_copy_variations" 
)

visual_suggester_agent = LlmAgent(
    name="VisualSuggester",
    model=MODEL_NAME, 
    instruction=VISUAL_SUGGESTER_INSTRUCTION,
    output_key="visual_concepts" 
)

formatter_agent = LlmAgent(
    name="CampaignBriefFormatter",
    model=MODEL_NAME,  
    instruction=FORMATTER_INSTRUCTION,
    output_key="final_campaign_brief" 
)

visual_image_agent = LlmAgent (
    name = "VisualGenerator",
    model = 'gemini-2.5-flash-image',
    instruction = VISUAL_GENERATION_INSTRUCTION,
    output_key = "final_image"
)


campagin_orchestrator = SequentialAgent(
    name = "MarketingCampaginAssistant",
    description = CAMPAIGN_ORCHESTRATOR_INSTRUCTION,
    sub_agents=[
        market_research_agent,
        messaging_strategist_agent,
        ad_copy_writer_agent,
        visual_suggester_agent,
        formatter_agent,
        visual_image_agent 
    ]
)

root_agent = campagin_orchestrator