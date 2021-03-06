# _*_ coding: utf-8 _*_

"""
inst_save.py by xianhu
"""

import sys
import logging
from ..utilities import extract_error_info


class Saver(object):
    """
    class of Saver, must include function working()
    """

    def __init__(self, save_pipe=sys.stdout):
        """
        constructor
        """
        self._save_pipe = save_pipe     # default: sys.stdout, also can be a file handler
        return

    def working(self, url: str, keys: object, item: (list, tuple)) -> bool:
        """
        working function, must "try, except" and don't change the parameters and return
        :return save_result: True or False
        """
        logging.debug("%s start: keys=%s, url=%s", self.__class__.__name__, keys, url)

        try:
            save_result = self.item_save(url, keys, item)
        except Exception as excep:
            save_result = False
            logging.error("%s error: %s, keys=%s, url=%s", self.__class__.__name__, extract_error_info(excep), keys, url)

        logging.debug("%s end: save_result=%s, url=%s", self.__class__.__name__, save_result, url)
        return save_result

    def item_save(self, url: str, keys: object, item: (list, tuple)) -> bool:
        """
        save the item of a url, you can rewrite this function, parameters and return refer to self.working()
        """
        self._save_pipe.write("\t".join([str(col) for col in item]) + "\n")
        self._save_pipe.flush()
        return True
