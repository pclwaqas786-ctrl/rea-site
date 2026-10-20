"""REA website (Streamlit) — Reverse Engineer Anything ka taaruf, educational.

Maloomat morluto/rea ke asal README se li gayi hain (koi daawa ghara nahi).
"""
import os

import requests
import streamlit as st

st.set_page_config(page_title="REA — Reverse Engineer Anything", page_icon="🔬", layout="wide")

GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"


def get_key():
    key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not key:
        try:
            key = st.secrets.get("GEMINI_API_KEY", "").strip()
        except Exception:
            key = ""
    return key


def get_model():
    return os.environ.get("GEMINI_MODEL", "gemini-3.8-flash").strip() or "gemini-3.8-flash"


# ---------------- HERO ----------------
st.title("🔬 REA — Reverse Engineer Anything")
st.subheader("Ek MCP jo AI agents ko apps ke andar dekhne ki taqat deta hai — app ke behavior se lekar binary level tak.")
c1, c2, c3, c4 = st.columns(4)
c1.metric("GitHub Stars", "307K+")
c2.metric("Forks", "77K+")
c3.metric("License", "MIT")
c4.metric("npm", "rea-agents")
st.caption("Source: github.com/morluto/rea (README se li gayi maloomat)")
st.divider()

st.write(
    "**Seedha matlab:** Koi app pasand aayi aur samajhna hai ke uska koi feature andar se kaise kaam karta hai? "
    "REA tumhare AI agent ko woh tools deta hai jin se wo app ko **baghair source code ke** inspect kar sake — "
    "kaise kaam karta hai samjhaye, **saboot (evidence)** dikhaye, aur tumhare project ke liye wesa feature bana ke de. "
    "Analysis tumhari apni machine par hoti hai."
)
st.info("💡 Is website ka maqsad **seekhna** hai — samajhna ke apps andar se kaise banti aur kaam karti hain.")

# ---------------- FEATURES ----------------
st.header("⚙️ REA kya-kya analyze kar sakta hai")
st.caption("Neeche wali list REA ke README ke 'What you can analyze' table se hai.")

targets = [
    ("💻 Native binaries", "Pseudocode, assembly, strings, symbols, calls aur references. Zaroorat: Hopper, Ghidra ya IDA."),
    ("🌐 JavaScript / Electron apps", "Modules, imports, source maps, routes, IPC. Zaroorat: Node.js + npm. Static analysis ke liye koi heavy engine nahi chahiye."),
    ("🕸️ Websites", "Page structure, scripts, network observations, screenshots. Zaroorat: Chrome-family browser."),
    ("📱 Android APKs", "Manifest, classes, decompiled methods. Zaroorat: headless JADX + JDK."),
    ("🧩 .NET assemblies", "Metadata, CIL instructions. Static only — kuch install karne ki zaroorat nahi."),
    ("🗄️ SQLite databases", "Tables, columns, indexes, triggers. Local snapshot par kaam karta hai."),
    ("🦀 Go / Rust binaries", "Compiler version, modules, dependencies — built-in static inspection, Go/Rust install nahi chahiye."),
    ("📡 Network captures", "Requests, responses, payloads — HAR ya Fiddler SAZ files se."),
    ("🔧 Firmware", "Regions, extraction, native-analysis handoff. Zaroorat: Binwalk/Unblob (Linux)."),
]
for i in range(0, len(targets), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        if i + j < len(targets):
            title, desc = targets[i + j]
            col.write(f"**{title}**")
            col.caption(desc)

st.divider()

# ---------------- HOW IT WORKS (educational) ----------------
st.header("🎓 Kaise kaam karta hai — reverse engineering seekho")
st.write("REA ka flow samajhne ke liye pehle 4 bunyadi concepts:")

with st.expander("1️⃣ Static analysis vs Dynamic analysis"):
    st.write(
        "**Static analysis** = app ko chalaye baghair uski files parhna (jaise kitaab ka index dekhna). "
        "REA JavaScript aur .NET apps ko chalaye baghair parh leta hai.\n\n"
        "**Dynamic analysis** = app ko chala ke uska bartao dekhna (jaise kisi ko kaam karte dekhna). "
        "REA process capture aur runtime tools se ye karta hai — tumhari permission se, tumhari machine par."
    )
with st.expander("2️⃣ Disassembly aur Decompilation"):
    st.write(
        "Compiled app machine code (0/1 jaisi hidayat) me hoti hai. **Disassembly** usay assembly zaban me badalta hai "
        "(mushkil lekin parhne layak), **decompilation** usay C-jaisi pseudocode me badalta hai (zyada samajh aane wali). "
        "REA native binaries ke liye Hopper/Ghidra/IDA istemal karta hai."
    )
with st.expander("3️⃣ Strings, Symbols aur IPC"):
    st.write(
        "**Strings** = app ke andar chhupe text (error messages, URLs) — aksar raaz khol dete hain. "
        "**Symbols** = functions ke naam. **IPC** (Inter-Process Communication) = Electron apps me alag hisson ke darmiyan guftagu — "
        "Notion wali showcase me REA ne clipboard bridge isi se trace kiya tha."
    )
with st.expander("4️⃣ Evidence-based findings"):
    st.write(
        "REA ka usool: har daawa **saboot ke sath**. Agent ko sirf 'ye aisa hai' nahi milta — code reference, "
        "file location aur **limitations** (kya pata nahi chal saka) bhi milti hain. Yehi ise andazon se alag karta hai."
    )

st.write("**REA ka asal flow (README se):**")
st.write("1. Tum agent se kehte ho: *'Notes app me search kaise kaam karta hai, saboot dikhao, mere project ke liye wesa feature banao.'*")
st.write("2. Agent REA ko MCP ke zariye bulata hai → REA target ko inspect karke relevant code trace karta hai.")
st.write("3. REA findings + evidence wapas deta hai → agent samjhata hai, sawal-jawab karta hai, implementation likh kar test karta hai.")
st.write("Terminal se bhi wohi kaam: `npx -y rea-agents@latest analyze-javascript-application /path/to/app --json`")

st.divider()

# ---------------- APP X-RAY (interactive demo) ----------------
st.header("🔎 App X-Ray — interactive demo")
st.write("Kisi app ka naam aur 1-line wazahat likho — AI (educational andaze me) batayega ke wo andar se **kaise bani ho sakti hai**.")

app_name = st.text_input("App ka naam", placeholder="masalan: Foodpanda")
app_desc = st.text_input("1 line me kya karti hai", placeholder="masalan: khana order karne wali app")

XRAY_SYSTEM = (
    "Tum ek reverse-engineering teacher ho. Student ne ek app ka naam aur wazahat di hai. "
    "Hamesha ROMAN URDU me jawab do (Urdu script nahi, Devanagari to bilkul nahi). "
    "Samjhao ke aisi app andar se kaise bani ho sakti hai: (1) mumkinah tech stack, (2) ahem components "
    "(masalan database, API, payment), (3) ek mashhoor feature kaise kaam karta hoga, "
    "(4) reverse engineer kya-kya dekhega (strings, network calls, database schema). "
    "Imandari se wazeh karo ke YE ANDAZA HAI — haqeeqat asal code dekhne par pata chalti hai. "
    "Jawab short aur phone-friendly rakho, headings ke sath."
)


def xray(name, desc):
    key = get_key()
    if not key:
        return "⚠️ GEMINI_API_KEY set nahi hai — App X-Ray ke liye key chahiye. Baqi website baghair key ke chalti hai."
    try:
        r = requests.post(
            GEMINI_URL,
            headers={"Authorization": f"Bearer {key}"},
            json={
                "model": get_model(),
                "messages": [
                    {"role": "system", "content": XRAY_SYSTEM},
                    {"role": "user", "content": f"App: {name}\nWazahat: {desc}\nIs app ka andar-ka-haal (likely architecture) samjhao."},
                ],
                "max_tokens": 800,
                "temperature": 0.7,
            },
            timeout=90,
        )
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"⚠️ X-Ray nahi ho saka: {e}"


if st.button("🔎 X-Ray karo", disabled=not (app_name and app_desc)):
    with st.spinner("App ka andar-ka-haal nikala ja raha hai..."):
        st.markdown(xray(app_name, app_desc))

st.divider()

# ---------------- SHOWCASES ----------------
st.header("🏆 Real showcases (README se)")
s1, s2, s3 = st.columns(3)
s1.write("**🎮 DX-Ball**")
s1.caption("Purani game ke sound-pan calculation ko dobara tameer kiya.")
s2.write("**📝 Notion**")
s2.caption("Electron app ke clipboard bridge ko trace kiya.")
s3.write("**👾 TH04**")
s3.caption("DOS game ke bullet-ring calculation ko recover kiya.")
st.caption("Tafseel: rea.tools par showcases section.")

st.divider()

# ---------------- INSTALL GUIDE ----------------
st.header("💾 Install guide (README se)")
st.write("**Zaroorat:** Node.js 22.x (>=22.19), 24.x (>=24.11) ya 26+, plus npm.")
st.code("npx rea-agents setup", language="bash")
st.write(
    "Ye command tumhare agent ko choose karne deti hai (Claude Code, Codex, Cursor, Gemini CLI, Grok Build waghera), "
    "phir REA ka MCP server aur workflow instructions laga deti hai. Baad me agent restart karo."
)
st.write("**Terminal se direct use:**")
st.code("npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json", language="bash")
st.write("**Mustaqil install:**")
st.code("npm install --global rea-agents\nrea --help", language="bash")
st.write("**Update:** `rea update` (ya npx walon ke liye `npx rea-agents@latest setup` dobara).")
st.caption("Linux par Ghidra/JADX/firmware tools ke liye procps-compatible `ps` PATH me hona chahiye — tafseel docs/installation.md me.")

st.divider()

# ---------------- DISCLAIMER ----------------
st.header("⚖️ Imandari wali baat")
st.write(
    "Reverse engineering **seekhne** ke liye powerful hai — apni apps samajhna, purane software ko bachana, "
    "security research. Lekin doosron ki mehnat chura ke bechna ya paid features muft me hasil karna iska maqsad nahi. "
    "REA ke README me bhi disclaimer hai. Hamesha apni ya ijazat-shuda targets par istemal karo, aur licenses ka ehtram karo."
)
st.caption("Website: rea.tools · GitHub: github.com/morluto/rea · License: MIT")
