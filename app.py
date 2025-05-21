import requests
import json

def getMedicine(medicine_name):
    """
    Get information for a medicine.
    """
    #use https://api.fda.gov/drug/event.json?limit=1 this API to get information about the medicine
    url = f"https://api.fda.gov/drug/event.json?search=patient.drug.medicinalproduct:{medicine_name}&limit=1"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    if not data.get("results"):
        return None
    medicine_info = data["results"][0]
    # Extract relevant information
    medicine_info = {
        "medicinal_product": medicine_info.get("patient", {}).get("drug", [{}])[0].get("medicinalproduct"),
        "indication": medicine_info.get("patient", {}).get("drug", [{}])[0].get("indication"),
        "reaction": medicine_info.get("patient", {}).get("reaction", [{}])[0].get("reactionmeddrapt"),
        "seriousness": medicine_info.get("seriousness"),
        "report_date": medicine_info.get("receivedate"),
    }
    # Convert to JSON string
    medicine_info_json = json.dumps(medicine_info, indent=4)
    return medicine_info_json   