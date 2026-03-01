class AddPatientPage:
    def __init__(self, page):
        self.page = page
        self.add_patient_button = page.locator("#addPatientBtn")
        self.patient_id = page.locator("#patientId")
        self.patient_name = page.locator("#patientName")
        self.category_dropdown = page.locator("#patientCategory")
        self.patient_status_dropdown = page.locator("#patientStatus")
        self.assigned_doctor = page.locator("#patientDoctor")
        self.ward = page.locator("#patientWard")
        self.admit_patient_button = page.locator("#submitPatientBtn")

    def click_add_patient(self):
        self.add_patient_button.click()

    def fill_patient_details(self, patient_id, name, category, status, doctor, ward):
        self.patient_id.fill(patient_id)
        self.patient_name.fill(name)
        self.category_dropdown.select_option(category)
        self.patient_status_dropdown.select_option(status)
        self.assigned_doctor.fill(doctor)
        self.ward.fill(ward)
        self.admit_patient_button.click()

