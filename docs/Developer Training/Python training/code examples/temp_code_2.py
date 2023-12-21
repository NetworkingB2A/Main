
class OSPFRouter:
    def __init__(self, instance_id, area, router_id, is_dr = False, is_bdr = False):
        self.instance_id = instance_id
        self.area = area
        self.router_id = router_id
        self.is_dr = is_dr
        self.is_bdr = is_bdr
        self._neighbors = set()

    def __str__(self) -> str:
        return f''' 
OSPFRouter: 
    Instance ID: {self.instance_id}, 
    Area ID: {self.area}, 
    Router ID: {self.router_id}, 
    is dr: {self.is_dr}, 
    is bdr: {self.is_bdr}, 
    Neighbors: {self._neighbors}
'''

    def add_neighbor(self, new_neighbor):
        self._neighbors.add(new_neighbor)

    def remove_neighbor(self, removed_neighbor):
        self._neighbors.discard(removed_neighbor)


new_router = OSPFRouter(instance_id=42, area='0.0.0.0', router_id='10.220.88.29', is_dr = True)
print(new_router)
new_router.add_neighbor('10.220.88.28')
new_router.add_neighbor('10.220.88.30')
new_router.add_neighbor('10.220.88.31')
new_router.add_neighbor('10.220.88.32')
new_router.add_neighbor('10.220.88.33')
new_router.add_neighbor('10.220.88.34')
new_router.add_neighbor('10.220.88.35')
new_router.add_neighbor('neighbor_3')
new_router.add_neighbor('neighbor_3')
print(new_router)
new_router.remove_neighbor('neighbor_3')
new_router.remove_neighbor('neighbor_4')
print(new_router)