SketchPlane0 = add_sketchplane(
	origin= [0., 0., 0.], normal= [ 0., -1.,  0.], x_axis= [ 1.,  0., -0.])
Loops0 = []
Curves0_0 = []
Circle0_0_0 = add_circle(center= [0., 0.], radius= 41.7551)
Loop0_0 = add_loop(Curves0_0)
Profile0 = add_profile(Loops0)
Sketch0 = add_sketch(sketch_plane= SketchPlane0, profile= Profile0)
Extrude0 = add_extrude(sketch= Sketch0,
	operation= 0, type= 0, extent_one= 107.9331, extent_two= 0.)
SketchPlane1 = add_sketchplane_ref(
	Extrude0, origin = [-0., -0.], type = "extent_one")
Loops1 = []
Curves1_0 = []
Circle1_0_0 = add_circle(center= [0., 0.], radius= 28.914)
Loop1_0 = add_loop(Curves1_0)
Profile1 = add_profile(Loops1)
Sketch1 = add_sketch(sketch_plane= SketchPlane1, profile= Profile1)
Extrude1 = add_extrude(sketch= Sketch1,
	operation= 1, type= 0, extent_one= 126.1059, extent_two= 0.)
SketchPlane2 = add_sketchplane_ref(
	Extrude1, origin = [-0., -0.], type = "extent_one")
Loops2 = []
Curves2_0 = []
Circle2_0_0 = add_circle(center= [0., 0.], radius= 21.4466)
Loop2_0 = add_loop(Curves2_0)
Profile2 = add_profile(Loops2)
Sketch2 = add_sketch(sketch_plane= SketchPlane2, profile= Profile2)
Extrude2 = add_extrude(sketch= Sketch2,
	operation= 2, type= 0, extent_one= -265.6521, extent_two= 0.)
SketchPlane3 = add_sketchplane_ref(
	Extrude1, origin = [-0., -0.], type = "extent_one")
Loops3 = []
Curves3_0 = []
Circle3_0_0 = add_circle(center= [0., 0.], radius= 54.4952)
Loop3_0 = add_loop(Curves3_0)
Curves3_1 = []
Circle3_1_0 = add_circle(center= [0., 0.], radius= 28.914)
Loop3_1 = add_loop(Curves3_1)
Profile3 = add_profile(Loops3)
Sketch3 = add_sketch(sketch_plane= SketchPlane3, profile= Profile3)
Extrude3 = add_extrude(sketch= Sketch3,
	operation= 0, type= 0, extent_one= -30.4578, extent_two= 0.)
