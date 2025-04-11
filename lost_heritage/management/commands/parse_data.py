import json
from datetime import datetime
from pathlib import Path

from django.core.management.base import BaseCommand
from lost_heritage.models import LostObject


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z").date()
    except Exception:
        return None


class Command(BaseCommand):
    help = "Парсит JSON-файл с утраченной культурной собственностью"

    def handle(self, *args, **kwargs):
        file_path = Path("3.json")
        if not file_path.exists():
            self.stderr.write("Файл 3.json не найден.")
            return

        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)

        created, updated = 0, 0

        for item in data:
            general = item["data"]["general"]
            loss_info = general.get("lostRegister", [{}])[0]

            obj, created_flag = LostObject.objects.update_or_create(
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

            if created_flag:
                created += 1
            else:
                updated += 1

        self.stdout.write(self.style.SUCCESS(f"Создано: {created}, обновлено: {updated}"))
