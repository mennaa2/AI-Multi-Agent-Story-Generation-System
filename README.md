# 🎬 StorySight AI

StorySight AI is an intelligent Multi-Agent AI system that transforms uploaded images into interactive creative stories using Computer Vision and Natural Language Processing.

The system is designed as a collaborative AI pipeline where multiple specialized AI agents work together to generate, evaluate, and improve stories dynamically based on user feedback.

---

# 🚀 Features

- 🖼️ Image Caption Generation using BLIP
- ✍️ AI Story Generation based on selected genre
- 🧠 Story Evaluation with Zero-Shot Classification
- ⭐ User Rating & Feedback System
- 🔄 Automatic Story Improvement & Rewriting
- 🎭 Multiple Genres Supported
- 🌐 Interactive Streamlit Web Interface

---

# 🧠 Multi-Agent Architecture

The project follows a Multi-Agent AI design where each agent has a dedicated responsibility.

## 1️⃣ Vision Agent

Responsible for understanding uploaded images and generating captions using:

- `Salesforce/blip-image-captioning-base`

### Tasks

- Process uploaded images
- Extract visual understanding
- Generate descriptive captions

---

## 2️⃣ Narrative Agent

Generates creative stories from captions using:

- `google/flan-t5-base`

### Tasks

- Create complete stories
- Support multiple genres
- Improve stories based on user feedback

### Supported Genres

- Sci-Fi
- Fantasy
- Drama
- Comedy

---

## 3️⃣ Critic Agent

Evaluates generated stories using:

- `facebook/bart-large-mnli`
- `google/flan-t5-base`

### Tasks

- Analyze story quality
- Detect coherence and emotional strength
- Generate short critiques and feedback

---

# 🔄 Feedback & Improvement Loop

One of the main goals of this project is creating an interactive storytelling experience.

After generating a story, users can:

- Rate the story ⭐
- Write custom feedback 📝
- Select improvement reasons if dissatisfied

The system then rewrites the story dynamically based on:

- Story too long
- Story too short
- Story boring
- Story inaccurate
- Story does not match expectations
- General enhancement request

This creates a Human-in-the-Loop AI workflow.

---

# 🛠️ Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- BLIP Image Captioning
- FLAN-T5
- BART Large MNLI
- PIL
- PyTorch

---

# ▶️ How to Run
streamlit run app.py

---

# 💡 Future Improvements

- Memory-enabled agents
- Better long-story coherence
- Voice narration support
- Image sequence storytelling
- Fine-tuned custom models
- Agent communication optimization


---

# 🙏 Acknowledgment

- Special thanks to Eng. Tadros Gamal for the continuous support, guidance, and encouragement throughout the project development.

---

# 📌Project Goal

This project explores how multiple AI agents can collaborate together to create adaptive and interactive AI systems instead of relying on a single model pipeline.

The focus is on combining:

- Computer Vision
- NLP
- Generative AI
- Human Feedback Systems
- Multi-Agent Collaboration

---

# 📂 Project Structure

```bash
├── app.py
├── orchestrator.py
├── vision_agent.py
├── narrative_agent.py
├── critic_agent.py
└── requirements.txt
