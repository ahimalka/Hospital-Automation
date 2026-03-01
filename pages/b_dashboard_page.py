class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.patients_tab = page.locator("//*[@id='dashboard']/div[2]/div[2]/div[2]/button[1]")
        self.laboratory_tab = page.locator("//*[@id='dashboard']/div[2]/div[2]/div[2]/button[2]")
        self.pharmacy_tab = page.locator("//*[@id='dashboard']/div[2]/div[2]/div[2]/button[3]")
        self.search_patient_input = page.locator("#searchInput")

    def click_patients(self):
        self.patients_tab.click()
        
    def click_labs(self):
        self.laboratory_tab.click()

    def click_pharmacy(self):
        self.pharmacy_tab.click()

    def search_patient(self, patient_id):
        self.search_patient_input.fill(patient_id)