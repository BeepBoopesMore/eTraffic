# Subnetting tool for your office / part of vlan etc managing while eTraffic has everything pretty much

import eTraffic
from eTraffic import Router
from eTrafficUtils import Office




router = Router("10.0.0.1","Musk","password","Cisco")
clock = router.clock
version = router.version
router.setup_NTP("10.0.0.1",)