# Marketing Campaign Assistant 🚀

This repository contains an automated multi-agent system designed to streamline the creation of comprehensive marketing campaigns. By leveraging the **Google ADK (Agent Development Kit)**, the system orchestrates several specialized AI agents to handle everything from market research to final visual generation.

---

## ## Overview

The **Marketing Campaign Assistant** operates as a `SequentialAgent` pipeline. It processes a campaign request through a specialized chain of command, ensuring each phase of the marketing process is handled by a dedicated expert.

### The Agent Lineup

| Agent | Role | Primary Output |
| --- | --- | --- |
| **Market Researcher** | Conducts live web searches to identify trends and competitors. | `market_research_summary` |
| **Messaging Strategist** | Defines the core value proposition and tone. | `key_messaging` |
| **Ad Copy Writer** | Drafts creative variations for various platforms. | `ad_copy_variations` |
| **Visual Suggester** | Conceptualizes the aesthetic and imagery themes. | `visual_concepts` |
| **Campaign Formatter** | Compiles all data into a professional, structured brief. | `final_campaign_brief` |

---

## ## Prerequisites

Before running the project, ensure you have the following installed:

* **Python 3.10+**
* **Google ADK** (Access to `google.adk`)
* **API Keys**: A valid Google Gemini API key.

### Environment Setup

1. **Environment Variables**: Create a `.env` file in the root directory:
```env
# Ensure your GOOGLE_API_KEY is exported in your shell or .env

```


2. **Dependencies**:
```bash
pip install python-dotenv

```



---

## ## Project Structure

* `agent.py`: The entry point (provided code) that initializes and links the agents.
* `marketing_campaign_agent/instructions.py`: This module must contain the specific string constants (e.g., `MARKET_RESEARCH_INSTRUCTION`) that define the "personality" and constraints for each agent.

---

## ## Logic Flow

The system follows a linear "waterfall" logic where each agent's output informs the next:

1. **Research**: The `MarketResearcher` uses the `Google Search` tool to pull real-time data.
2. **Strategy**: The data is passed to the `MessagingStrategist` to find the "hook."
3. **Creation**: Copy and Visual concepts are generated based on the strategy.
4. **Formatting**: The `CampaignBriefFormatter` cleans the text for human consumption.


---

## ## Usage

To execute the agent, you can call the `root_agent` (the orchestrator) with your campaign prompt:

```python
# Example execution
result = root_agent.run("Launch a sustainable bamboo toothbrush brand for Gen Z.")

print(result.final_campaign_brief)


```

> **Note:** If `python-dotenv` is missing, the system defaults to the `gemini-2.5-flash` model but will warn you to set your API keys manually.

