import unittest
import os
from urllib.request import pathname2url
from floodestimation import db
from floodestimation import loaders
from floodestimation import settings
from floodestimation.entities import Catchment


class TestLoaders(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        settings.OPEN_HYDROLOGY_JSON_URL = 'file:' + pathname2url(os.path.abspath('./floodestimation/fehdata_test.json'))
        cls.session = db.Session()

    def test_load_catchment(self):
        catchment = loaders.load_catchment('floodestimation/tests/data/17002.CD3')
        self.assertEqual(17002, catchment.id)
        self.assertEqual(3, len(catchment.amax_records))

    def test_load_catchment_without_amax(self):
        catchment = loaders.load_catchment('floodestimation/tests/data/170021.CD3')
        self.assertEqual([], catchment.amax_records)

    def test_save_catchments_to_db(self):
        loaders.gauged_catchments_to_db(self.session)
        expected = ['Ardlethen', "Curry's Bridge", 'Dudgeon Bridge', 'Headswood', 'Inverugie', 'Leven']
        result = [location for (location, ) in self.session.query(Catchment.location).order_by(Catchment.location)]
        self.assertEqual(expected, result)
        self.session.rollback()

