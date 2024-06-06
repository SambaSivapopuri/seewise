from django.test import TestCase
from .models import Machine, ProductionLog
from rest_framework.test import APIClient

class OEECalculationTestCase(TestCase):
    def setUp(self):
        self.machine = Machine.objects.create(machine_name='Test Machine', machine_serial_no='12345')
        ProductionLog.objects.create(
            cycle_no='CN001', unique_id='UID001', material_name='Material1',
            machine=self.machine, start_time='2024-06-06T08:00:00Z', end_time='2024-06-06T08:05:00Z', duration=5.0)
        self.client = APIClient()

    def test_get_oee(self):
        response = self.client.get('/oee/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('oee', response.data)

    def test_filter_oee(self):
        response = self.client.get(f'/oee/filter/?machine_id={self.machine.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('oee', response.data)
