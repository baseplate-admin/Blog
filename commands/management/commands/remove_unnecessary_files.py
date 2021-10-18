import os
import json
import sys

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Remove unnecessary files generated from Whitenoise"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.json_data: object = self.__load_json()
        self.static_dir: str = os.path.join(settings.BASE_DIR, "static")

        self.count: int = 0

    @staticmethod
    def __load_json() -> object:
        try:
            return json.load(
                open(os.path.join(settings.BASE_DIR, "static", "staticfiles.json"))
            )
        except FileNotFoundError:
            print(
                f"\nThere is no 'staticfiles.json' in '{os.path.join(settings.BASE_DIR, 'static',)}' "
            )
            print("Did you type 'python manage.py collectstatic'\n")
            sys.exit()

    def __remove_and_add(self, path: str) -> None:
        try:
            os.remove(path)
            self.count += 1
        except FileNotFoundError:
            if os.path.isfile(path):
                self.count -= 1

    def handle(self, *args, **kwargs):
        for file in self.json_data["paths"]:
            self.__remove_and_add(os.path.join(self.static_dir, file))
            self.__remove_and_add(os.path.join(self.static_dir, f"{file}.br"))
            self.__remove_and_add(os.path.join(self.static_dir, f"{file}.gz"))

        print(
            f"\nRemoved : {self.count} files \n |> From '{os.path.join(settings.BASE_DIR, 'static')}' \n |> Using '{os.path.join(settings.BASE_DIR, 'static', 'staticfiles.json')}'\n"
        )
