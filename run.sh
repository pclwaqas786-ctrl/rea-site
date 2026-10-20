#!/bin/bash
# REA website launcher — port 8504
cd "$(dirname "$0")"
if [ ! -d .venv ]; then
  python3 -m venv .venv
  TMPDIR=~/workspace/.tmp .venv/bin/pip install -q -r requirements.txt
fi
if [ -f ~/workspace/veo-studio/.env ]; then
  set -a; source ~/workspace/veo-studio/.env; set +a
fi
if [ -z "$GEMINI_API_KEY" ]; then
  echo "NOTE: GEMINI_API_KEY nahi mili — website chalegi, lekin 'App X-Ray' demo kaam nahi karega."
  echo "Key ke liye ~/workspace/veo-studio/.env me GEMINI_API_KEY dalo ya Streamlit secrets istemal karo."
fi
exec .venv/bin/streamlit run app.py --server.port 8504
