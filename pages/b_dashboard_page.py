class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.patients_tab = page.locator("//*[@id='dashboard']/div[2]/div[2]/div[2]/button[1]")
        self.laboratory_tab = page.locator("//*[@id='dashboard']/div[2]/div[2]/div[2]/button[2]")
        self.pharmacy_tab = page.locator("//*[@id='dashboard']/div[2]/div[2]/div[2]/button[3]")
        self.search_patient_input = page.locator("#searchInput")

    async def click_patients(self):
        await self.patients_tab.click()
        
    async def click_labs(self):
        await self.laboratory_tab.click()

    async def click_pharmacy(self):
        await self.pharmacy_tab.click()

    async def search_patient(self, patient_id):
        await self.search_patient_input.fill(patient_id)

    async def click_logout(self):
        await self.page.locator(".btn-logout").click()