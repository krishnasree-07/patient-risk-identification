class CancerPatient:
    def _init_(self, name, age, gender, family_history, tumor_size_cm, has_metastasis):
        self.name = name
        self.age = age
        self.gender = gender
        self.family_history = family_history  # True or False
        self.tumor_size_cm = tumor_size_cm
        self.has_metastasis = has_metastasis  # True or False

    def assess_risk(self):
        risk_score = 0
        
        # Age-based risk
        if self.age > 60:
            risk_score += 2
        elif self.age > 40:
            risk_score += 1
        
        # Family history of cancer
        if self.family_history:
            risk_score += 2
        
        # Tumor size
        if self.tumor_size_cm > 5:
            risk_score += 1
        
        # Metastasis
        if self.has_metastasis:
            risk_score += 3
        
        return risk_score

# Example usage:
if _name_ == "_main_":
    # Create a cancer patient instance
    patient1 = CancerPatient("sanju", 19, "Female", False, 4, True)
    
    # Assess risk
    risk_score = patient1.assess_risk()
    print(f"Risk score for {patient1.name}: {risk_score}")
