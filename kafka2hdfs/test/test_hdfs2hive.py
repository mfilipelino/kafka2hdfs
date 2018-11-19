import json

from unittest import TestCase
from hdfs2hive import mapRows


class Testekafka2hdfs(TestCase):

    def setUp(self):
        file_ = open('test/payload.json', 'r')
        self.json_string = file_.read()

    def test_map_json(self):
        json_parser = mapRows(self.json_string)
       # json_dict = json.loads(json_parser)
        self.assertIn('scope', json_parser)
