import json
from datetime import datetime
from pathlib import Path
from lost_heritage.models import LostObject


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z").date()
    except Exception:
        return None


def run():
    file_path = Path("3.json")
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        general = item["data"]["general"]
        loss_info = general.get("lostRegister", [{}])[0]
        
        LostObject.objects.update_or_create(
            native_id=item["nativeId"],
            defaults={
                "register_number": general.get("registerNumber", ""),
                "name": general.get("name", "").strip(),
                "description": general.get("description", ""),
                "identifying_characteristics": general.get("identifyingCharacteristics", ""),
                "material": general.get("description", "").split("Материал:")[-1].split("\r\n")[0] if "Материал:" in general.get("description", "") else "",
                "origin_place": general.get("name", "").split("Школа / Место издания:")[-1].strip() if "Школа / Место издания:" in general.get("name", "") else "",
                "register_type": general.get("registerType", {}).get("name", ""),
                "registration_date": general.get("registrationDate", "")[:10],
                "loss_place_description": loss_info.get("lossPlaceDescription", ""),
                "rnom_register_number": loss_info.get("RNOMRegisterNumber", ""),
                "dokm_base_document": loss_info.get("DOKMBaseDocument", ""),
                "category": loss_info.get("category", ""),
                "museum": loss_info.get("collection", ""),
                "creator": loss_info.get("creator", ""),
                "date_creator": parse_date(loss_info.get("dateCreator", "")),
            }
        )
