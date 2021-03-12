""" pip install anastruct """


from anastruct import SystemElements


ss = SystemElements()

x = 325
W = 1350  # load on the WHOLE structure


ss.add_element([[0, 0], [x, 0]])
ss.add_element([[x, 0], [2 * x, 0]])
ss.add_element([[2 * x, 0], [815, 0]])
ss.add_element([[815, 0], [2 * x, 255]])
ss.add_element([[x, 255], [2 * x, 255]])
ss.add_element([[0, 255], [x, 255]])
ss.add_element([[x, 255], [x, 0]])
ss.add_element([[x, 0], [2 * x, 255]])
ss.add_element([[x, 0], [0, 255]])
ss.add_element([[2 * x, 0], [2 * x, 255]])

ss.add_support_fixed(node_id=1)
ss.add_support_fixed(node_id=7)
ss.point_load(node_id=4, Fy=-W / 2)
ss.solve()


"""Uncomment the code below to see:
---------------------------------------------------"""

"""The applied load"""
# ss.show_structure(scale=0.6)

"""External reactions and bending moments"""
# ss.show_reaction_force(scale=0.6)

"""Axial Forces"""
# ss.show_axial_force(scale=0.6)

"""Shear forces"""
# ss.show_shear_force(scale=0.6)

"""Bending Moments"""
# ss.show_bending_moment(scale=0.6)

"""Displacements"""
# ss.show_displacement(scale=0.6)

"""All of the graphs above"""
# ss.show_results(scale=0.6)
