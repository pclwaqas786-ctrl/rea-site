# REA Website 🔬 — Reverse Engineer Anything

Streamlit website about the REA reverse-engineering tool (github.com/morluto/rea).
Educational purpose: seekhna ke apps andar se kaise kaam karti hain.
Tamam maloomat REA ke asal README se li gayi hain.

## Chalana (local)

```bash
cd ~/workspace/rea-site
./run.sh
```

Browser me kholo: http://localhost:8504

## Sections

1. **Hero** — REA kya hai (short, honest, no hype) + real stats (307K+ stars, MIT, npm rea-agents)
2. **Features** — kya-kya analyze kar sakta hai (README ke table se: native binaries, JS/Electron, websites, Android APKs, .NET, SQLite, Go/Rust, network captures, firmware)
3. **Kaise kaam karta hai** — reverse engineering ke 4 bunyadi concepts (static vs dynamic analysis, disassembly/decompilation, strings/symbols/IPC, evidence-based findings) + REA ka asal flow
4. **App X-Ray** — interactive demo: app ka naam + wazahat do, AI uski likely architecture samjhata hai (educational andaza). Needs GEMINI_API_KEY.
5. **Showcases** — DX-Ball, Notion, TH04 (README se)
6. **Install guide** — `npx rea-agents setup`, requirements, terminal commands (README se)
7. **Disclaimer** — imandari wali baat (seekhne ke liye, chori ke liye nahi)

## Key

`GEMINI_API_KEY` (sirf App X-Ray demo ke liye) `~/workspace/veo-studio/.env` se auto-load hoti hai.
Key kabhi code me nahi hai, kabhi print nahi hoti.

## Streamlit Cloud deploy

1. Is folder ko GitHub repo me push karo (`app.py`, `requirements.txt`; `.venv/` mat karo).
2. share.streamlit.io → New app.
3. Secrets me: `GEMINI_API_KEY = "tumhari-key"` (sirf X-Ray ke liye zaroori).
