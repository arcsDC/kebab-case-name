import unittest
import sys
import os
import importlib.util

class TestFiveMResource(unittest.TestCase):
    def setUp(self):
        self.resource_root = os.path.join(os.path.dirname(__file__), '..')
        self.manifest_path = os.path.join(self.resource_root, 'fxmanifest.lua')
        self.config_path = os.path.join(self.resource_root, 'config.lua')
        self.server_path = os.path.join(self.resource_root, 'server.lua')
        self.client_path = os.path.join(self.resource_root, 'client.lua')

    def test_manifest_exists(self):
        self.assertTrue(os.path.exists(self.manifest_path), "fxmanifest.lua is missing")

    def test_config_exists(self):
        self.assertTrue(os.path.exists(self.config_path), "config.lua is missing")

    def test_server_script_exists(self):
        self.assertTrue(os.path.exists(self.server_path), "server.lua is missing")

    def test_client_script_exists(self):
        self.assertTrue(os.path.exists(self.client_path), "client.lua is missing")

    def test_manifest_structure(self):
        with open(self.manifest_path, 'r') as f:
            content = f.read()
            self.assertIn('fx_version', content)
            self.assertIn('game', content)
            self.assertIn('lua54', content)
            self.assertIn('server_scripts', content)
            self.assertIn('client_scripts', content)

    def test_config_structure(self):
        with open(self.config_path, 'r') as f:
            content = f.read()
            self.assertIn('Config', content)
            self.assertIn('Permissions', content)
            self.assertIn('EvidenceTypes', content)

    def test_server_logic(self):
        with open(self.server_path, 'r') as f:
            content = f.read()
            self.assertIn('RegisterNetEvent', content)
            self.assertIn('CreateThread', content)
            self.assertIn('MySQL.query', content)

    def test_client_logic(self):
        with open(self.client_path, 'r') as f:
            content = f.read()
            self.assertIn('RegisterNetEvent', content)
            self.assertIn('CreateThread', content)
            self.assertIn('exports', content)

if __name__ == '__main__':
    unittest.main()
