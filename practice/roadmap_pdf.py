
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER
 
W, H = A4
 
TEAL       = colors.HexColor("#0F6E56")
TEAL_LIGHT = colors.HexColor("#E1F5EE")
TEAL_MID   = colors.HexColor("#9FE1CB")
PURPLE     = colors.HexColor("#3C3489")
PURPLE_L   = colors.HexColor("#EEEDFE")
AMBER      = colors.HexColor("#854F0B")
AMBER_L    = colors.HexColor("#FAEEDA")
CORAL      = colors.HexColor("#993C1D")
CORAL_L    = colors.HexColor("#FAECE7")
BLUE       = colors.HexColor("#185FA5")
BLUE_L     = colors.HexColor("#E6F1FB")
GRAY       = colors.HexColor("#5F5E5A")
GRAY_L     = colors.HexColor("#F1EFE8")
DARK       = colors.HexColor("#1A1A18")
WHITE      = colors.white
 
doc = SimpleDocTemplate(
    "Ahmad_Week2_Roadmap.pdf",
    pagesize=A4,
    leftMargin=18*mm, rightMargin=18*mm,
    topMargin=16*mm, bottomMargin=16*mm
)
 
styles = getSampleStyleSheet()
 
def S(name, **kw):
    return ParagraphStyle(name, **kw)
 
h1 = S("H1", fontSize=22, textColor=DARK, fontName="Helvetica-Bold",
        spaceAfter=4, leading=28)
h2 = S("H2", fontSize=15, textColor=TEAL, fontName="Helvetica-Bold",
        spaceAfter=3, leading=20)
h3 = S("H3", fontSize=12, textColor=DARK, fontName="Helvetica-Bold",
        spaceAfter=2, leading=16)
body = S("Body", fontSize=9.5, textColor=GRAY, fontName="Helvetica",
         spaceAfter=3, leading=14)
small = S("Small", fontSize=8.5, textColor=GRAY, fontName="Helvetica",
          spaceAfter=2, leading=12)
bold_body = S("BoldBody", fontSize=9.5, textColor=DARK, fontName="Helvetica-Bold",
              spaceAfter=2, leading=14)
code_s = S("Code", fontSize=8, textColor=colors.HexColor("#042C53"),
           fontName="Courier", spaceAfter=2, leading=12,
           backColor=BLUE_L, leftIndent=6, rightIndent=6,
           borderPad=4)
label = S("Label", fontSize=8, textColor=WHITE, fontName="Helvetica-Bold",
          leading=11)
sub = S("Sub", fontSize=8.5, textColor=GRAY, fontName="Helvetica-Oblique",
        spaceAfter=2, leading=12)
 
def hr(color=TEAL_MID, thickness=0.5):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=6, spaceBefore=6)
 
def badge(text, bg, fg=WHITE):
    data = [[Paragraph(text, S("b", fontSize=8, textColor=fg,
                                fontName="Helvetica-Bold", leading=10))]]
    t = Table(data, colWidths=[None])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("ROUNDEDCORNERS", [4]),
        ("LEFTPADDING", (0,0), (-1,-1), 7),
        ("RIGHTPADDING", (0,0), (-1,-1), 7),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
    ]))
    return t
 
def section_header(title, subtitle, color, light):
    data = [[
        Paragraph(title, S("sh", fontSize=13, textColor=color,
                            fontName="Helvetica-Bold", leading=17)),
        Paragraph(subtitle, S("ss", fontSize=8.5, textColor=color,
                               fontName="Helvetica", leading=12))
    ]]
    t = Table(data, colWidths=["55%", "45%"])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), light),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ROUNDEDCORNERS", [6]),
    ]))
    return t
 
def day_block(day_num, day_name, theme, sessions, win, color, light, mid):
    elems = []
    header_data = [[
        Paragraph(f"Day {day_num}", S("dn", fontSize=18, textColor=color,
                                       fontName="Helvetica-Bold", leading=22)),
        Paragraph(f"<b>{day_name}</b><br/><font size='8'>{theme}</font>",
                  S("dt", fontSize=10, textColor=DARK, fontName="Helvetica",
                    leading=14))
    ]]
    ht = Table(header_data, colWidths=[22*mm, None])
    ht.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,0), light),
        ("BACKGROUND", (1,0), (1,0), GRAY_L),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ROUNDEDCORNERS", [5]),
    ]))
    elems.append(ht)
    elems.append(Spacer(1, 5))
 
    for s in sessions:
        time_label, title, desc, code = s
        row = [[
            Paragraph(time_label, S("tl", fontSize=7.5, textColor=color,
                                     fontName="Helvetica-Bold", leading=10)),
            Paragraph(f"<b>{title}</b><br/>{desc}",
                      S("sd", fontSize=9, textColor=GRAY, fontName="Helvetica",
                        leading=13))
        ]]
        rt = Table(row, colWidths=[24*mm, None])
        rt.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (0,0), light),
            ("LEFTPADDING", (0,0), (-1,-1), 6),
            ("RIGHTPADDING", (0,0), (-1,-1), 6),
            ("TOPPADDING", (0,0), (-1,-1), 5),
            ("BOTTOMPADDING", (0,0), (-1,-1), 5),
            ("VALIGN", (0,0), (-1,-1), "TOP"),
            ("ROUNDEDCORNERS", [4]),
        ]))
        elems.append(rt)
        if code:
            elems.append(Paragraph(code, code_s))
        elems.append(Spacer(1, 4))
 
    win_data = [[Paragraph(f"Today's win: {win}",
                            S("w", fontSize=8.5, textColor=colors.HexColor("#085041"),
                              fontName="Helvetica-Bold", leading=12))]]
    wt = Table(win_data, colWidths=[None])
    wt.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), TEAL_LIGHT),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("ROUNDEDCORNERS", [4]),
    ]))
    elems.append(wt)
    elems.append(Spacer(1, 10))
    return elems
 
def parallel_block(title, items, color, light):
    content = f"<b>{title}</b><br/>"
    content += "<br/>".join([f"• {i}" for i in items])
    data = [[Paragraph(content, S("pb", fontSize=8.5, textColor=DARK,
                                   fontName="Helvetica", leading=13))]]
    t = Table(data, colWidths=[None])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), light),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("LINEAFTER", (0,0), (0,-1), 3, color),
        ("ROUNDEDCORNERS", [4]),
    ]))
    return t
 
story = []
 
cover_data = [[
    Paragraph("Ahmad's Week 2", S("ct", fontSize=26, textColor=WHITE,
                                    fontName="Helvetica-Bold", leading=32)),
    Paragraph("Gen AI Engineering Roadmap", S("cs", fontSize=13, textColor=TEAL_MID,
                                               fontName="Helvetica", leading=18)),
    Paragraph("Embeddings · RAG · Vector DBs · PDF Chatbot · Parallel Tracks",
              S("cd", fontSize=9, textColor=colors.HexColor("#9FE1CB"),
                fontName="Helvetica", leading=13)),
    Paragraph("Days 8–14 | Built specifically for a MERN developer going all-in on AI Engineering",
              S("ce", fontSize=8, textColor=colors.HexColor("#5DCAA5"),
                fontName="Helvetica-Oblique", leading=12)),
]]
ct = Table([[c] for c in cover_data[0]], colWidths=[None])
ct.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), TEAL),
    ("LEFTPADDING", (0,0), (-1,-1), 14),
    ("RIGHTPADDING", (0,0), (-1,-1), 14),
    ("TOPPADDING", (0,0), (0,0), 14),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,-1), (-1,-1), 14),
    ("ROUNDEDCORNERS", [8]),
]))
story.append(ct)
story.append(Spacer(1, 12))
 
stats = [
    ["7 Days", "2 Parallel Tracks", "2 Projects", "1 Deployed App"],
    ["daily schedule", "main + codebasics", "PDF chatbot + RAG", "live by Sunday"]
]
st = Table([
    [Paragraph(v, S("sv", fontSize=16, textColor=TEAL, fontName="Helvetica-Bold", leading=20)) for v in stats[0]],
    [Paragraph(v, S("sl", fontSize=8, textColor=GRAY, fontName="Helvetica", leading=11)) for v in stats[1]],
], colWidths=["25%","25%","25%","25%"])
st.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), GRAY_L),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ("ROUNDEDCORNERS", [6]),
    ("LINEAFTER", (0,0), (2,1), 0.5, colors.HexColor("#D3D1C7")),
]))
story.append(st)
story.append(Spacer(1, 12))
 
story.append(section_header(
    "Main Track — Gen AI Engineering",
    "90% of your daily time · Build real AI systems every day",
    TEAL, TEAL_LIGHT
))
story.append(Spacer(1, 8))
 
days = [
    (8, "Embeddings — how text becomes numbers",
     "The concept that unlocks everything in AI",
     [
         ("Morning 1.5hrs", "Install + understand embeddings conceptually",
          "Watch: 'Embeddings explained' — Andrej Karpathy YouTube (15 min). Read: platform.openai.com/docs/guides/embeddings first section.",
          "pip install sentence-transformers numpy chromadb"),
         ("Evening 1.5hrs", "Write your first embedding call + cosine similarity",
          "Compare text meaning with numbers. Try Urdu vs English sentences.",
          "from sentence_transformers import SentenceTransformer\nmodel = SentenceTransformer('all-MiniLM-L6-v2')\ntexts = ['I love Python', 'Python is great', 'I eat biryani']\nembeddings = model.encode(texts)"),
         ("Night 30min", "Experiment + GitHub commit",
          "Compare: 'AI Engineer' vs 'ML Engineer'. Push: 'Day 8 — embeddings and cosine similarity'", None),
     ],
     "You understand embeddings and can compare text meaning in code. Foundation of every RAG system.",
     TEAL, TEAL_LIGHT, TEAL_MID
    ),
    (9, "ChromaDB — your first vector database",
     "Store and retrieve embeddings locally",
     [
         ("Morning 1.5hrs", "Setup ChromaDB + store your first vectors",
          "Create a collection, add documents with embeddings, query by semantic similarity.",
          "import chromadb\nclient = chromadb.PersistentClient(path='./chroma_db')\ncollection = client.get_or_create_collection('knowledge_base')"),
         ("Evening 1.5hrs", "Persistent DB + add your own facts",
          "Add 10 facts about yourself — skills, projects, experience. Query with 5 different questions. Delete a doc and re-query.",
          None),
         ("Night 30min", "Read ChromaDB docs + push",
          "Read: docs.trychroma.com — Getting Started. Push to GitHub.", None),
     ],
     "Working local vector database. You can store and retrieve meaning, not just text.",
     TEAL, TEAL_LIGHT, TEAL_MID
    ),
    (10, "RAG from scratch — no LangChain",
     "Build the pipeline manually so you actually understand it",
     [
         ("Morning 1.5hrs", "Understand + build RAG manually",
          "4 steps: INGEST chunks → EMBED → STORE in vector DB → QUERY → RETRIEVE → GENERATE. Build WITHOUT LangChain first.",
          "def ask(query):\n    chunks = retrieve(query)   # get relevant docs\n    return generate(query, chunks)  # LLM answers using context"),
         ("Evening 1.5hrs", "Add chunking — split long text properly",
          "Chunk a text file, ingest it, query it. Try chunk sizes 100 vs 300 words. See how answer quality changes.",
          "def chunk_text(text, chunk_size=200, overlap=50):\n    words = text.split()\n    return [' '.join(words[i:i+chunk_size])\n            for i in range(0, len(words), chunk_size-overlap)]"),
         ("Night 30min", "Push + read",
          "Read: python.langchain.com/docs/tutorials/rag — just read tonight, don't code yet.", None),
     ],
     "You built RAG from scratch. You understand every piece. Most people just use LangChain and have no idea what's inside.",
     PURPLE, PURPLE_L, colors.HexColor("#CECBF6")
    ),
    (11, "LangChain — now speed it up",
     "Use the framework now that you understand what it's doing",
     [
         ("Morning 1.5hrs", "Install LangChain + rebuild RAG in 20 lines",
          "Compare to your Day 10 code — same result, 5x less code. Now you appreciate what LangChain does.",
          "pip install langchain langchain-community langchain-groq chromadb"),
         ("Evening 1.5hrs", "LangChain document loaders + text splitters",
          "Load a text file → split → store → query. Install pypdf and try loading a real PDF file.",
          "from langchain.text_splitter import RecursiveCharacterTextSplitter\nsplitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)"),
         ("Night 30min", "Push + DeepLearning.AI course",
          "Start: deeplearning.ai/short-courses — 'LangChain for LLM Application Development'. Do first 2 lessons tonight.", None),
     ],
     "You can build RAG both manually and with LangChain. You know when to use which.",
     PURPLE, PURPLE_L, colors.HexColor("#CECBF6")
    ),
    (12, "PDF chatbot — your week 2 project",
     "Upload any PDF and chat with it — full stack",
     [
         ("Morning 2hrs", "Build the Python backend — FastAPI + RAG",
          "FastAPI endpoint: POST /upload processes PDF → chunks → embeds → stores. POST /ask queries and returns answer.",
          "pip install fastapi uvicorn python-multipart pypdf langchain-groq\nuvicorn main:app --reload"),
         ("Evening 2hrs", "Build the React frontend",
          "Use AI freely for the UI. Focus on: PDF upload area, progress indicator showing chunk count, chat interface (same as week 1), disable input until PDF uploaded.",
          None),
         ("Night 30min", "Test everything locally",
          "Upload your own CV as a PDF. Ask: 'What is Ahmad's experience?' Verify the answer is accurate.", None),
     ],
     "Working PDF chatbot on localhost. Upload any PDF — CV, contract, textbook — and chat with it.",
     AMBER, AMBER_L, colors.HexColor("#FAC775")
    ),
    (13, "Polish + deploy live",
     "Nothing counts until it is live on the internet",
     [
         ("Morning 2hrs", "Add one impressive feature",
          "Pick one: show which page the answer came from / auto-generate 3 questions after upload / 'summarise this PDF' button.",
          None),
         ("Evening 2hrs", "Deploy — Railway + Vercel",
          "pip freeze > requirements.txt. Add Procfile. Deploy FastAPI to Railway (add GROQ_API_KEY). Deploy React to Vercel. Test live end to end.",
          "web: uvicorn main:app --host 0.0.0.0 --port $PORT"),
         ("Night 30min", "Write README + record demo",
          "Proper README with screenshots + live link. Record 30-second demo: upload PDF, ask 3 questions, show streaming answers.", None),
     ],
     "Live deployed PDF chatbot. This is a real product you can show clients and charge for.",
     AMBER, AMBER_L, colors.HexColor("#FAC775")
    ),
    (14, "Week 2 wrap-up + LinkedIn + prep week 3",
     "Document, share, and plan ahead",
     [
         ("Morning 1.5hrs", "LinkedIn week 2 post + screen recording",
          "Hook: 'I just built something that would have cost $50k from an agency 3 years ago.' Attach demo recording. Tag @Groq.",
          None),
         ("Evening 1.5hrs", "Preview week 3 — AI agents",
          "Read: Anthropic blog 'What are AI agents'. Watch: LangGraph intro by Harrison Chase (20 min YouTube).",
          "pip install langgraph tavily-python crewai"),
         ("Night 30min", "Week 2 checklist",
          "Embeddings ✓ | ChromaDB ✓ | RAG scratch ✓ | LangChain ✓ | PDF chatbot deployed ✓ | LinkedIn + GitHub updated ✓", None),
     ],
     "Week 2 complete. You went from zero RAG knowledge to a deployed PDF chatbot. Week 3 — agents. This is where it gets insane.",
     CORAL, CORAL_L, colors.HexColor("#F5C4B3")
    ),
]
 
for d in days:
    story.extend(day_block(*d))
 
story.append(hr())
story.append(Spacer(1, 4))
 
story.append(section_header(
    "Parallel Track — Codebasics Foundation",
    "30 min/day only · Never blocks your main track",
    PURPLE, PURPLE_L
))
story.append(Spacer(1, 8))
 
parallel_items = [
    ("Day 8–9: Advanced Python patterns",
     ["Watch Codebasics Python videos 17–22: Inheritance, Generators, Iterators",
      "These patterns appear in LangChain internals — good to recognise them",
      "Do NOT spend more than 30 min — just watch, don't build exercises yet"],
     PURPLE, PURPLE_L),
    ("Day 10–11: NLP fundamentals — why embeddings work",
     ["Watch Codebasics NLP playlist: Tokenization, stemming, lemmatization",
      "Watch: Word2Vec explained — this is the ancestor of modern embeddings",
      "Count vectorizer + TF-IDF — understand WHY semantic search is better"],
     BLUE, BLUE_L),
    ("Day 12–13: List comprehensions + Decorators + Lambda",
     ["Codebasics Python videos 23–27: Decorators, Multithreading concepts",
      "Practice: rewrite 3 of your existing Python functions using list comprehensions",
      "30 min only — these come naturally as you build more"],
     TEAL, TEAL_LIGHT),
    ("Day 14: Soft skills — LinkedIn engagement strategy",
     ["Comment meaningfully on 5 AI-related LinkedIn posts today",
      "Follow: Andrej Karpathy, Harrison Chase, Jerry Liu on X and LinkedIn",
      "Subscribe: The Rundown AI newsletter (therundown.ai) — 5 min daily AI news"],
     AMBER, AMBER_L),
]
 
for title, items, color, light in parallel_items:
    story.append(parallel_block(title, items, color, light))
    story.append(Spacer(1, 6))
 
story.append(hr())
story.append(Spacer(1, 4))
 
story.append(section_header(
    "Week 2 Resources",
    "Everything you need — free unless marked",
    TEAL, TEAL_LIGHT
))
story.append(Spacer(1, 8))
 
res_data = [
    ["Type", "Resource", "What to do"],
    ["Free course", "DeepLearning.AI — LangChain for LLM Apps", "Do every notebook. Andrew Ng + Harrison Chase."],
    ["Free course", "DeepLearning.AI — Building RAG Systems", "Hands-on. Very practical. Essential this week."],
    ["Docs", "python.langchain.com/docs/tutorials/rag", "Official RAG tutorial. Read fully on Day 11 night."],
    ["YouTube", "Sam Witteveen — RAG tutorials", "Best practical RAG coding channel. Watch his playlist."],
    ["Tool (free)", "ChromaDB — docs.trychroma.com", "Local vector DB. Getting Started section."],
    ["Tool (free)", "sentence-transformers library", "pip install sentence-transformers — free embeddings."],
    ["Platform", "Railway.app", "Free tier. Deploy your FastAPI backend here."],
    ["Platform", "Vercel.com", "Free tier. Deploy React frontend. Connect GitHub repo."],
    ["YouTube", "Andrej Karpathy — Intro to LLMs", "1-hour talk. Best conceptual foundation. Watch Day 14."],
]
 
rt = Table(res_data, colWidths=["22%", "40%", "38%"])
rt.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), TEAL),
    ("TEXTCOLOR", (0,0), (-1,0), WHITE),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,0), 8.5),
    ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
    ("FONTSIZE", (0,1), (-1,-1), 8),
    ("TEXTCOLOR", (0,1), (-1,-1), GRAY),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, GRAY_L]),
    ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#D3D1C7")),
    ("LEFTPADDING", (0,0), (-1,-1), 7),
    ("RIGHTPADDING", (0,0), (-1,-1), 7),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("ROUNDEDCORNERS", [4]),
]))
story.append(rt)
story.append(Spacer(1, 12))
 
story.append(section_header(
    "Week 2 GitHub commit checklist",
    "Push something every single day",
    CORAL, CORAL_L
))
story.append(Spacer(1, 8))
 
commits = [
    ["Day", "File to push", "Commit message"],
    ["Day 8", "day8_embeddings.py", "Day 8 — embeddings and cosine similarity"],
    ["Day 9", "day9_chromadb.py", "Day 9 — ChromaDB local vector database"],
    ["Day 10", "day10_rag_scratch.py", "Day 10 — RAG pipeline built from scratch"],
    ["Day 11", "day11_langchain_rag.py", "Day 11 — RAG with LangChain and document loaders"],
    ["Day 12", "pdf_chatbot/backend/main.py", "Day 12 — PDF chatbot FastAPI backend"],
    ["Day 13", "pdf_chatbot/ (full)", "Day 13 — PDF chatbot deployed live [link]"],
    ["Day 14", "README.md update", "Week 2 complete — PDF chatbot shipped"],
]
 
ct2 = Table(commits, colWidths=["12%", "35%", "53%"])
ct2.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), CORAL),
    ("TEXTCOLOR", (0,0), (-1,0), WHITE),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,0), 8.5),
    ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
    ("FONTSIZE", (0,1), (-1,-1), 8),
    ("TEXTCOLOR", (0,1), (-1,-1), GRAY),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, CORAL_L]),
    ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#D3D1C7")),
    ("LEFTPADDING", (0,0), (-1,-1), 7),
    ("RIGHTPADDING", (0,0), (-1,-1), 7),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("ROUNDEDCORNERS", [4]),
]))
story.append(ct2)
story.append(Spacer(1, 12))
 
final_data = [[Paragraph(
    "<b>Week 2 in one sentence:</b> You go from calling AI APIs to building a complete AI system "
    "that understands documents — and you deploy it live for the world to use.",
    S("final", fontSize=10, textColor=colors.HexColor("#04342C"),
      fontName="Helvetica", leading=15)
)]]
ft = Table(final_data, colWidths=[None])
ft.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), TEAL_LIGHT),
    ("LEFTPADDING", (0,0), (-1,-1), 14),
    ("RIGHTPADDING", (0,0), (-1,-1), 14),
    ("TOPPADDING", (0,0), (-1,-1), 12),
    ("BOTTOMPADDING", (0,0), (-1,-1), 12),
    ("ROUNDEDCORNERS", [6]),
    ("LINEBEFORE", (0,0), (0,-1), 3, TEAL),
]))
story.append(ft)
 
doc.build(story)
print("PDF generated successfully")
 