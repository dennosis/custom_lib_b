from sicrediutils import phone_numbers, read_xml
from sicrediextractors.utils.dicts import recursive_extrator_dict


class XmlExtarctor:
    def __init__(
        self,
        path: str,
    ) -> None:
        self.path = path
        self.xml_dict = read_xml(path)

    def get_phones(
        self,
    ):
        phones = recursive_extrator_dict(self.xml_dict, phone_numbers)

        return phones
