from customliba import extract_phone_numbers, read_xml
from customlibb.module_bb.utils_bba import recursive_extrator_dict


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
        phones = recursive_extrator_dict(self.xml_dict, extract_phone_numbers)

        return phones
