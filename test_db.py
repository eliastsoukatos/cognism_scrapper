from src.utils.database import save_to_db


test_data = {
    "Name": "Test",
    "Last_Name": "User",
    "Mobile_Phone": "1234567890",
    "Email": "test@example.com",
    "Role": "Tester",
    "City": "Test City",
    "State": "TS",
    "Country": "Testland",
    "Timezone": "UTC",
    "LinkedIn_URL": "https://linkedin.com/in/test",
    "Company_Name": "TestCorp",
    "Website": "https://testcorp.com",
    "Employees": "100",
    "Founded": "2020",
    "Segment": "Tech",
    "Timestamp": "2024-02-01 12:00:00",
    "Cognism_URL": "https://cognism.com/test"
}

save_to_db(test_data)  # ✅ Manually insert test data
