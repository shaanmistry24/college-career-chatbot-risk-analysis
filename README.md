# college-career-chatbot-risk-analysis

A research-based evaluation of an AI-powered college and career guidance chatbot built using OpenAI’s GPT-3.5 Turbo. This project investigates the chatbot’s reliability, fairness, and bias across a variety of student profiles and scenarios, offering insight into how AI can support educational decision-making. <br/>

View the research paper I wrote and published in Curieux Academic Journal (Part 1 of Decemeber 2023 issue): [Full Research Paper](https://docs.google.com/document/d/1W-ol3JfPnQzZcUNG8yUNs_Adi9o6Y5h9_hNTXL5jusc/edit?usp=sharing) <br/>

[Link to publication issue](https://www.curieuxacademicjournal.com/fall-winter2023) <br/>

## Overview

This chatbot helps high school students receive personalized advice on college and career pathways. By collecting key information such as age, GPA, test scores, interests, and preferred college traits, the chatbot generates tailored plans including school recommendations, majors, internships, summer programs, and career paths. <br/>

The project includes a formal risk assessment of the chatbot’s performance using AI-generated student profiles from different demographic and academic backgrounds. <br/>

## Features
- Built with OpenAI GPT-3.5 and Gradio
- Collects user input: age, GPA, interests, test scores, and preferences
- Provides a full college & career recommendation plan
- Responds to follow-up questions about schools, deadlines, and more
- Outputs 10 relevant websites based on user profile

## Key Results

- 100% accuracy in financial aid, internship, and entrance exam guidance  
- Lower accuracy (40–60%) in application deadlines and acceptance rates  
- Evidence of bias toward prestigious schools and conventional career paths  
- Limited representation of less mainstream fields (e.g., sports, music production) <br/>

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/EduBot-Fairness-Eval.git
cd college-career-chatbot-risk-analysis
```
### 2. Install dependencies
```bash
pip install openai gradio
```
### 3. Set OpenAI API key
- Replace "YOUR_OPENAI_API_KEY" in the code with your actual key <br/>
### 4. Run the chatbot
```bash
python chatbot_app.py
```


