
import streamlit as st
import pandas as pd
import datetime

# Beispielübungen
training_plan = {
    "Push A": [("Schrägbankdrücken (LH)", 4, "8–10"), ("Flachbankdrücken (KH)", 3, "10–12")],
    "Pull A": [("Klimmzüge", 4, "6–10"), ("Langhantelrudern", 4, "8–10")],
    "Legs A": [("Kniebeugen", 4, "8–10"), ("Wadenheben", 3, "15–20")],
    "Push B": [("Flachbankdrücken (LH)", 4, "6–8"), ("Schulterdrücken (SZ)", 3, "8–10")],
    "Pull B": [("Klimmzüge eng", 4, "6–10"), ("Hammercurls", 3, "10–12")],
    "Legs B": [("Kreuzheben (KH)", 4, "10–12"), ("Beinheben", 3, "12–15")]
}

st.set_page_config(page_title="TrainLog App", layout="centered")
st.title("📋 TrainLog – Dein Push/Pull/Legs Plan")

# Trainingstag auswählen
selected_day = st.selectbox("Wähle deinen Trainingstag:", list(training_plan.keys()))
st.subheader(f"📆 {selected_day} – Übungen")

# Tabelle vorbereiten
entries = []
today = datetime.date.today().strftime("%Y-%m-%d")

for idx, (exercise, sets, reps) in enumerate(training_plan[selected_day]):
    st.markdown(f"### {exercise} ({sets} Sätze x {reps})")
    weight = st.text_input(f"Gewicht (kg) – {exercise}", key=f"w_{idx}")
    reps_done = st.text_input(f"Wdh. geschafft – {exercise}", key=f"r_{idx}")
    note = st.text_input(f"Notizen – {exercise}", key=f"n_{idx}")
    entries.append({
        "Datum": today,
        "Tag": selected_day,
        "Übung": exercise,
        "Sätze": sets,
        "Ziel-Wdh.": reps,
        "Gewicht (kg)": weight,
        "Wdh. geschafft": reps_done,
        "Notiz": note
    })

# Speichern
if st.button("💾 Training speichern"):
    df = pd.DataFrame(entries)
    filename = f"{selected_day.replace(' ', '_')}_{today}.csv"
    df.to_csv(filename, index=False)
    st.success(f"Training gespeichert als {filename}")
