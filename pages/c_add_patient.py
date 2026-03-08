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

    async def click_add_patient(self):
        await self.add_patient_button.click()

    async def fill_patient_details(self, patient_id, name, category, status, doctor, ward):
        await self.patient_id.fill(patient_id)
        await self.patient_name.fill(name)
        await self.category_dropdown.select_option(category)
        await self.patient_status_dropdown.select_option(status)
        await self.assigned_doctor.fill(doctor)
        await self.ward.fill(ward)
        await self.admit_patient_button.click()

