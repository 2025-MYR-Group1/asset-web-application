from sqlmodel import text


def test_db_connection_ok(real_engine):
	with real_engine.connect() as conn:
		result = conn.execute(text("SELECT 1"))
		assert result.scalar() == 1


def test_assets_crud_smoke_against_container(client_real):
	# create
	payload = {
		"category": "Monitor",
		"type": "LCD",
		"brand": "Dell",
		"name": "U2720Q",
		"supplier": "XYZ",
		"serial_no": "SN-CONTAINER-1",
		"invoice_no": "INV-C-001",
		"purchase_date": "2024-01-01",
		"warranty_start_date": "2024-01-01",
		"warranty_end_date": "2026-01-01",
		"location": "HQ",
		"assigned_campus": "Main",
		"assigned_department": "IT",
		"manager_name": "Lee",
		"status": "in_use",
		"depreciation": 0,
	}
	resp = client_real.post("/api/assets/add", json=payload)
	assert resp.status_code == 200
	asset_id = resp.json()["data"]["id"]

	# fetch
	resp = client_real.get(f"/api/assets/{asset_id}")
	assert resp.status_code == 200

	# delete
	resp = client_real.delete(f"/api/assets/{asset_id}")
	assert resp.status_code == 200


