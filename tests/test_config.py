import unittest
import mock

from yaabook.app_config import AppConfig
class ConfigTestCase(unittest.TestCase):
    @mock.patch('yaabook.app_config.configparser')
    @mock.patch('yaabook.app_config.isfile')
    def test_config_writes_file_if_no_file_exists(self, mock_isfile, mock_open):
        # shows that we are able to mock built in functions
        assert isinstance(mock_open, mock.MagicMock)
        # pretend there is no file
        mock_isfile.return_value = False
        default = {'default': {'name': 'john'}}
        conf = AppConfig('test', default)
        print(conf.appPath)
        mock_open.assert_called()
        mock_isfile.assert_called()
        assert isinstance(conf, AppConfig)
