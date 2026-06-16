from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client =OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

def ExtractJobInfo(job):
    response = client.chat.completions.create(
      model="llama-3.1-8b-instant",
      messages=[
         {
            "role":"system",
            "content":"""
    Extract job information and return ONLY valid JSON.
    Do not include markdown, explanations, or extra text.

    Format:
    {
      "title":"",
      "income":"",
      "location":"",
      "techStack":[]
    }
    """},
         {
            "role":"user",
            "content":job

         }
      ]
   )
    return response.choices[0].message.content

jobdescription = """TechNova Solutions, a fast-growing software company headquartered in Lahore with a hybrid work model, is seeking a Senior Full-Stack Engineer to join its product development team. The selected candidate will primarily work from Lahore but may occasionally collaborate with teams in Berlin and London. This position offers a compensation package ranging from PKR 350,000 to PKR 550,000 per month, along with annual performance bonuses and health benefits. Applicants should have at least 4 years of experience building scalable web applications and be proficient in a modern JavaScript ecosystem that includes React, Next.js, Node.js, Express.js, TypeScript, and MongoDB. Experience with PostgreSQL, Docker, AWS, CI/CD pipelines, and GitHub Actions will be considered a strong advantage. The engineer will be responsible for designing REST APIs, optimizing database performance, mentoring junior developers, and collaborating with UI/UX designers, product managers, and DevOps engineers to deliver high-quality software solutions for international clients. While the role is officially titled "Senior Full-Stack Engineer," candidates with experience in MERN-stack development, cloud-native architectures, and microservices will be given preference during the hiring process."""
result = json.loads(ExtractJobInfo(jobdescription))
print(result)
print(f"\nTitle: {result['title']}")
print(f"Remote: {result['location']}")
print(f"Skills needed: {', '.join(result['techStack'])}")

         