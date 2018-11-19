import json

from unittest import TestCase
from kafka2hdfs import mapValues


class Testekafka2hdfs(TestCase):

    def test_parser(self):
        # fiz pra validar test unit
        self.assertEqual(mapValues(element=(1, 2)), 2)
