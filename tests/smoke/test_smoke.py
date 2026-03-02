import pytest

from pages.a_login_page import LoginPage
from pages.b_dashboard_page import DashboardPage
from pages.c_add_patient import AddPatientPage
from playwright.sync_api import expect
import time

def test_smoke_flow(page, hospital_url):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    add_patient_page = AddPatientPage(page)

    page.goto(hospital_url)

    # assertion: make sure we are on the correct page
    expect(page).to_have_url("file:///C:/Users/97250/Desktop/Automation/hospital.html")

    login_page.login("nurse_admin", "clinical2026")

    # assertion: checking the presence of the logout button
    expect(page.locator(".btn-logout")).to_be_visible()

    dashboard_page.click_labs()
    dashboard_page.click_pharmacy()
    dashboard_page.click_patients()

    add_patient_page.click_add_patient()

    the_patient_id = "12345"
    add_patient_page.fill_patient_details(
        patient_id = the_patient_id,
        name="QA test",
        category="ICU",
        status="Stable",
        doctor="Dr. test",
        ward="Ward A"
    )
                        
    dashboard_page.search_patient("QA test")    
    # assertion: checking if the patient is in the search results
    expect(page.locator("#dataContainer")).to_contain_text(the_patient_id)

    
    time.sleep(5)

