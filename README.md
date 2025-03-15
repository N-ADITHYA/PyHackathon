# Smart Voice Assistant (Offline AI)


This is an **AI-powered voice assistant** that works completely **offline**. It can:
-  Recognize voice commands
-  Understand intent using NLP (spaCy)
-  Chat using a local AI model (DistilGPT-2)
-  Perform tasks (tell time, jokes, set alarms, open YouTube)

## How to Use
### **Clone the Repository**
```sh
git clone https://github.com/N-ADITHYA/PyHackathon.git
cd Hackathon_22BTRCO006
```

### **Set Up the Environment**
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate    # Windows
```

### **Install Dependencies**
```sh
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### **Run the Assistant**
```sh
python src/main.py
```

