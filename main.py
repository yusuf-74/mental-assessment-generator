import tkinter as tk
from tkinter import messagebox
from openai import OpenAI
import subprocess

# Function to perform operation on inputs
def operate_on_inputs():
    try:
        # Retrieve input values from text fields
        text_diagnosis = diagnosis.get("1.0", "end").strip()  # Get all text from line 1
        text_history_of_trauma = history_of_trauma.get("1.0", "end").strip()
        text_symptoms = symptoms.get("1.0", "end").strip()
        text_history_of_problem = history_of_problem.get("1.0", "end").strip()
        text_treatment_plan = treatment_plan.get("1.0", "end").strip()

        # generate comprehensive mental health assessment
        messagebox.showinfo("Generating the file please wait")
        
        client = OpenAI(api_key='')
        completion = client.chat.completions.create(
            model="gpt-4o",
            n=1,
            temperature=0.8,
            messages=[
                {"role": "system", "content": \
"""
You are a comprehensive mental health assessment generator You have to generate the assessment based on the provided data 
DON'T ADD MADE UP DATA JUST THE PROVIDED DATA.
"""},
                {
                    "role": "user",
                    "content": \
f"""
THIS IS EXAMPLE OF ASSESSMENT WITH THIS DATA
Diagnosis: depression 
History of trauma: CT has witnessed parents fighting.
Symptoms : trouble sleeping, overthinking doubting self.
History of problem: 1 year
Treatment plan: to reduce overthinking and improve sleeping.

**PSYCHIATRIC OUTPATIENT CLINIC**  
123 Main Street  
Anywhere, US 12345-6789  

**Complete Evaluation: Psychiatrist**

**Date of Exam:** 10/21/2024  
**Time of Exam:** 6:45 PM  

**Patient Name:** CT  

### **Diagnosis:**
- Depression

### **History of Trauma:**
- CT has witnessed frequent conflict between their parents, which may have contributed to the current depressive symptoms.

### **Current Symptoms:**
- **Trouble sleeping:** CT reports difficulties in falling asleep and staying asleep.
- **Overthinking:** CT experiences excessive rumination, which leads to persistent worry.
- **Self-doubt:** CT frequently questions their self-worth and abilities.

### **History of the Problem:**
- The symptoms have been present for approximately one year.

### **Treatment Plan:**
1. **Reduce Overthinking:** Cognitive techniques will be introduced to help manage and reduce overthinking patterns.
2. **Improve Sleep:** A sleep hygiene routine will be developed to improve sleep quality and reduce insomnia symptoms.

---

this one was great but it has a lot of made up data please STICK WITH THE PROVIDED DATA AS FOLLOWS 
Diagnosis: {text_diagnosis} 
History of trauma: {text_history_of_trauma}
Symptoms : {text_symptoms}
History of problem: {text_history_of_problem}
Treatment plan: {text_treatment_plan}
START
"""
                }
            ]
        )
        
        with open('assessment.md', 'w') as f:
            f.write(completion.choices[0].message.content)
        
        # convert md to pdf
        subprocess.run(["mdpdf","-o","assessment.pdf","assessment.md"])
        
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid text.")


root = tk.Tk()
root.title("Tkinter Expandable Text Fields")
root.geometry("500x900")
root.configure(bg="#f0f0f0")


label_font = ('Arial', 12, 'bold')
text_font = ('Arial', 11)
padding_options = {'padx': 10, 'pady': 5}


tk.Label(root, text="Diagnosis:", font=label_font, bg="#f0f0f0").grid(row=0, column=0, sticky="e", **padding_options)
diagnosis = tk.Text(root, font=text_font, height=2, width=40) 
diagnosis.grid(row=0, column=1, sticky="nsew", **padding_options)

tk.Label(root, text="History of trauma:", font=label_font, bg="#f0f0f0").grid(row=1, column=0, sticky="e", **padding_options)
history_of_trauma = tk.Text(root, font=text_font, height=2, width=40)
history_of_trauma.grid(row=1, column=1, sticky="nsew", **padding_options)

tk.Label(root, text="Symptoms:", font=label_font, bg="#f0f0f0").grid(row=2, column=0, sticky="e", **padding_options)
symptoms = tk.Text(root, font=text_font, height=2, width=40)
symptoms.grid(row=2, column=1, sticky="nsew", **padding_options)

tk.Label(root, text="History of problem:", font=label_font, bg="#f0f0f0").grid(row=3, column=0, sticky="e", **padding_options)
history_of_problem = tk.Text(root, font=text_font, height=2, width=40)
history_of_problem.grid(row=3, column=1, sticky="nsew", **padding_options)

tk.Label(root, text="Treatment plan:", font=label_font, bg="#f0f0f0").grid(row=4, column=0, sticky="e", **padding_options)
treatment_plan = tk.Text(root, font=text_font, height=2, width=40)
treatment_plan.grid(row=4, column=1, sticky="nsew", **padding_options)


submit_button = tk.Button(root, text="Submit", font=('Arial', 12), bg="#4CAF50", fg="white", command=operate_on_inputs)
submit_button.grid(row=5, column=0, columnspan=2, pady=20)

root.grid_columnconfigure(1, weight=1)  
for i in range(5):
    root.grid_rowconfigure(i, weight=1)  

root.mainloop()
