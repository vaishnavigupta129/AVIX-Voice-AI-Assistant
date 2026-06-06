# 🎙️ AVIX: Advanced Voice Interface Matrix

AVIX is an intelligent, context-aware voice assistant that bridges advanced cloud-based LLM architectures with native desktop operating systems. Powered by the Google Gemini SDK and high-fidelity Microsoft neural audio streams, AVIX responds dynamically while handling local hardware execution tasks.

---

## ✨ System Features
* **Stateful Conversational Context:** Built utilizing the modern `google-genai` system chats execution pattern to maintain historical conversational data across multiple turn-taking loops.
* **Premium Neural Audio Synthesis:** Synthesizes textual structures into realistic speech tokens utilizing `edge-tts` (`en-IN-PrabhatNeural`), creating a fluid human-like interaction.
* **Smart Intercept Matrix:** Intercepts runtime intents to execute instant platform-level browser automation protocols (routing directly to targeted profiles on GitHub, LinkedIn, or streaming services).
* **Calibrated Speech Recognition:** Live-calibrates system microphonic background frequencies before processing structural language translations through Google's Speech API.

---

## 🛠️ System Architecture & Workflow

1. **Audio Capture Layer:** Microphonic audio input is parsed and calibrated via `speech_recognition`.
2. **Evaluation & Intercept:** Commands matching system actions (like opening links or exiting) bypass cloud compute to run natively via `webbrowser`.
3. **Cognitive Logic Execution:** Conversational strings are routed securely through the `gemini-2.5-flash` model.
4. **Asynchronous Audio Pipelining:** Text answers are transformed into transient `.mp3` blocks by `edge-tts` and cleanly handled by `pygame.mixer` to eliminate system file-locking conflicts.

---

## 🚀 Local Deployment Setup

### 1. Configure Secrets
Create a `.env` file inside your project's local directory to protect your API keys:
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
