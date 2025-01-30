class Patient:
    def _init_(self, name, age, has_diabetes, blood_pressure, cholesterol_level):
        self.name = name
        self.age = age
        self.has_diabetes = has_diabetes
        self.blood_pressure = blood_pressure  # Assuming systolic blood pressure
        self.cholesterol_level = cholesterol_level

    def assess_risk(self):
        risk_score = 0
        
        # Age-based risk
        if self.age > 60:
            risk_score += 2
        elif self.age > 40:
            risk_score += 1
        
        # Diabetes
        if self.has_diabetes:
            risk_score += 2
        
        # Blood pressure
        if self.blood_pressure >= 140:  # High blood pressure threshold (systolic)
            risk_score += 1
        
        # Cholesterol level
        if self.cholesterol_level >= 200:  # High cholesterol threshold
            risk_score += 1
        
        return risk_score
    
    
    # Example usage:
if _name_ == "_main_":
    # Create a patient instance
    patient1 = Patient("rosy", 24, False, 120, 150)
    
    # Assess risk
    risk_score = patient1.assess_risk()
    print(f"Risk score for {patient1.name}: {risk_score}")
