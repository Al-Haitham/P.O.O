evenements = {
"event1": {"nom": "Conférence", "participants": {"Ali", "Sara"}},
"event2": {"nom": "Atelier", "participants": {"Zineb", "Sara","Ali"}},
"event3": {"nom": "Hackathon", "participants": {"Sara"}}
}

#Q1
print("Event 1 : ",evenements['event1']['participants'])

#Q2
evenements['event2']['participants'].add("Omar")
print("Event 2 : ",evenements['event2']['participants'])

#Q3
print("participans commun entre event.1 et event.2: ",evenements["event1"]["participants"] & evenements["event2"]["participants"])

#Q4
print("participans differens entre event.2 et event.3: ",evenements["event2"]["participants"] ^ evenements["event3"]["participants"])

#Q5
print("participans commun entre event.2 et event.3: ",evenements["event2"]["participants"] & evenements["event3"]["participants"])

#Q6
print("tout les noms des events: ",*(set(e for e in evenements.keys())))

#Q7
print([e for e in evenements.keys() if "Ali" in evenements[e]["participants"]])

#Q8
print([e for e in evenements.keys() if len(evenements[e]["participants"])>1])

#Q9
print(*((f"{e}:{len(evenements[e]["participants"])}") for e in evenements.keys()),sep=" - ")

#Q10
participants=[p for e in evenements.keys() for p in evenements[e]['participants']]
print(participants)
print(*(set((p,participants.count(p)) for p in participants if participants.count(p)>=2)),sep=" - ")