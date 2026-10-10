import json
student = {
 "id": 101,
 "name": "Asha",
 "skills": ["Python", "SQL"]
}
text = json.dumps(student,indent=2)
print(text)
restored = json.loads(text)
print(restored)