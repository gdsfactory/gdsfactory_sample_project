__version__ = "0.0.0"

from cspdk.si220 import PDK
from doroutes.bundles import add_bundle_astar

PDK.routing_strategies["doroute_astar"] = add_bundle_astar
