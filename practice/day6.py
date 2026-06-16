#Cv analyzer


from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client =OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

def ExtractJobInfo(jobdescription,userSkills):
    response = client.chat.completions.create(
      model="llama-3.1-8b-instant",
      messages=[
         {
            "role":"system",
            "content":"""You are an AI CV Matching Assistant that evaluates a user's skills and job description against predefined job role standards in the tech industry.

Your job is NOT only to compare text directly. Instead, you must:

1. Identify the most relevant JOB ROLE from the job description (e.g., MERN Stack Developer, Frontend Developer, Backend Developer, Full Stack Developer, DevOps Engineer, etc.)
2. Compare the user's skills against the STANDARD SKILL REQUIREMENTS of that role
3. Also compare against any additional requirements found in the job description
4. Generate a structured evaluation report

You must act like an ATS (Applicant Tracking System) used by companies.

---

📌 INPUT YOU WILL RECEIVE:
- Job Description (free text)
- User Skills (list or text)

---

📌 YOUR PROCESS:
1. Extract job role from job description
2. Map it to standard industry role expectations:
   - MERN Stack Developer → React, Node.js, Express, MongoDB, JavaScript, REST APIs, Git, etc.
   - Frontend Developer → React/Vue, HTML, CSS, JavaScript, UI/UX, etc.
   - Backend Developer → Node.js, databases, APIs, authentication, etc.
3. Compare user skills with:
   - Required role skills (industry standard)
   - Skills mentioned in job description
4. Calculate match score based on:
   - Core skill match (most important)
   - Optional/bonus skills
   - Missing critical skills

---

📦 OUTPUT FORMAT (STRICT JSON ONLY):
{
  "detected_role": "",
  "match_score": 0-100,
  "matching_skills": [],
  "missing_skills": [],
  "skill_gap_level": "low | medium | high",
  "recommendation": ""
}

---

🧠 SCORING RULES:
- 0–30 = Not suitable
- 31–60 = Needs improvement
- 61–80 = Good match
- 81–100 = Strong match

Core skills matter more than optional tools.

---

⚠️ IMPORTANT RULES:
- Output ONLY valid JSON
- No explanations, no markdown, no extra text
- Do NOT hallucinate skills that are not reasonable for the role
- Be realistic like a real recruiter ATS system"""},
         {
            "role":"user",
            "content":f"""
     Job desscription:{jobdescription}
     User Skills : {userSkills}

"""

         }
      ]
   )
    content = response.choices[0].message.content
    # Safety: strip markdown backticks if model adds them
    content = content.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    return content

jobdescription = input("Give job description: ")
userSkills=input("User skills: ")


result = json.loads(ExtractJobInfo(jobdescription, userSkills))
print(result)
print(f"\nRole: {result['detected_role']}")
print(f"Match Score: {result['match_score']}")
print(f"matching_skills: {', '.join(result['matching_skills'])}")
print(f"missing_skills: {', '.join(result['missing_skills'])}")
print(f"recommendation: {result['recommendation']}")