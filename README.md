💼 AI/ML Capstone Project Portfolio
Welcome to a showcase of real-world machine learning solutions designed to tackle critical industry problems—from customer churn prediction to intelligent ticket assignment and context-aware chatbots. This portfolio demonstrates end-to-end ML development, leveraging robust MLOps practices.

📊 Project 1: End-to-End ML Pipeline for Customer Churn Prediction
🎯 Goal/Purpose
Can a machine learning model accurately predict customer churn before it's too late, enabling proactive retention strategies and minimizing revenue loss?

This project delivers a production-ready ML pipeline built entirely with Scikit-learn's powerful Pipeline API. It automates every step: data preprocessing, feature transformation, hyperparameter tuning, and model selection. The pipeline is meticulously optimized for recall on churned customers, as every missed churn instance directly impacts revenue.

🚀 Highlights
Complete End-to-End Workflow: Seamlessly integrates all stages of the ML lifecycle.

Robust Model Selection: Implements and compares Logistic Regression and Random Forest models.

Optimized for Churn Prediction: Uses GridSearchCV and class balancing techniques to significantly enhance minority class (churned customers) recall.

Automated Model Evaluation: Automatically selects the superior performing model and provides visualizations of top influential features.

Deployment Ready: Exports the final, optimized pipeline using joblib for straightforward deployment and reusability.

🤖 Project 2: Auto Ticket Assignment Using NLP (BERT)
🎯 Goal/Purpose
What if IT support tickets could route themselves, drastically reducing manual effort and improving resolution times?

Manual ticket assignment is a major bottleneck, draining IT resources, leading to misrouted cases, and frustrating users. This project leverages transformer-based NLP models to automatically classify incoming incident tickets into one of 74 distinct functional groups. This automation saves significant time, minimizes human error, and frees up IT personnel for more critical tasks.

🚀 Highlights
Advanced Text Classification: Employs BERT fine-tuning for highly accurate classification of complex ticket text.

Handles Real-World Data: Designed to manage high class imbalance commonly found in ITSM datasets.

Built for IT Workflows: Developed with practical IT Service Management (ITSM) processes in mind.

Direct Impact: Enables faster ticket triage, leads to lower resolution times, and ultimately results in higher user satisfaction.

💬 Project 3: Context-Aware Chatbot for UV Detectors (LangChain + OpenAI + Streamlit)
🎯 Goal/Purpose
What if users could simply talk to your product documentation and receive instant, contextually relevant answers?

Traditional methods of digging through manuals for product specifications are inefficient. This intelligent chatbot, built with LangChain, OpenAI, and FAISS, allows users to ask natural language questions about UV detector specifications and receive accurate, context-aware responses. It transforms static documentation into an interactive expert.

🚀 Highlights
Interactive User Interface: Features a polished and intuitive UI developed with Streamlit.

Intelligent Conversation Flow: Maintains conversation memory using LangChain to provide coherent interactions.

Semantic Search: Embeds product manuals and FAQs into a FAISS vector store for efficient and relevant information retrieval.

Versatile Applications: Ideal for enhancing sales support, streamlining tech onboarding, and providing instant product help.

📂 How to Use
To explore and run any of these projects locally, follow the setup instructions below.

🛠️ Setup (For All Projects)
Bash

git clone https://github.com/YOUR_USERNAME/your-capstone-repo.git
cd your-capstone-repo
pip install -r requirements.txt
▶️ Run the Chatbot (Project 3)
Bash

streamlit run context_aware_chatbot.py
Enter your OpenAI API key in the sidebar within the Streamlit application to begin chatting with UV detector specs.

📬 Connect With Me
Let's connect and discuss data, AI, machine learning, or collaborative project opportunities!

🔗 LinkedIn – Hafsa Ahmed

