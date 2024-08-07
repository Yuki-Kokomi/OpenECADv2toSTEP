SketchPlane0 = add_sketchplane(
	origin= [0., 0., 0.], normal= [ 0., -1.,  0.], x_axis= [ 1.,  0., -0.])
Loops0 = []
Curves0_0 = []
Line0_0_0 = add_line(start= [-50.8,   0. ], end= [0., 0.])
Line0_0_1 = add_line(start= [0., 0.], end= [ 0. , 50.8])
Line0_0_2 = add_line(start= [ 0. , 50.8], end= [-50.8,  50.8])
Line0_0_3 = add_line(start= [-50.8,  50.8], end= [-50.8,   0. ])
Loop0_0 = add_loop(Curves0_0)
Profile0 = add_profile(Loops0)
Sketch0 = add_sketch(sketch_plane= SketchPlane0, profile= Profile0)
Extrude0 = add_extrude(sketch= Sketch0,
	operation= 0, type= 0, extent_one= 50.8, extent_two= 0.)
SketchPlane1 = add_sketchplane_ref(
	Extrude0, origin= [25.4, 25.4], type= "line", line= Line0_0_2, angle= np.pi)
Loops1 = []
Curves1_0 = []
Circle1_0_0 = add_circle(center= [0., 0.], radius= 12.7)
Loop1_0 = add_loop(Curves1_0)
Profile1 = add_profile(Loops1)
Sketch1 = add_sketch(sketch_plane= SketchPlane1, profile= Profile1)
Extrude1 = add_extrude(sketch= Sketch1,
	operation= 2, type= 0, extent_one= -50.8, extent_two= 0.)
SketchPlane2 = add_sketchplane_ref(
	Extrude0, origin = [-25.4,  25.4], type = "sameplane", angle = -np.pi, reverse = True)
Loops2 = []
Curves2_0 = []
Circle2_0_0 = add_circle(center= [0., 0.], radius= 12.7)
Loop2_0 = add_loop(Curves2_0)
Profile2 = add_profile(Loops2)
Sketch2 = add_sketch(sketch_plane= SketchPlane2, profile= Profile2)
Extrude2 = add_extrude(sketch= Sketch2,
	operation= 1, type= 0, extent_one= 12.7, extent_two= 0.)
SketchPlane3 = add_sketchplane_ref(
	Extrude0, origin= [25.4, 25.4], type= "line", line= Line0_0_1, angle= -np.pi/2)
Loops3 = []
Curves3_0 = []
Line3_0_0 = add_line(start= [-12.7, -12.7], end= [ 12.7, -12.7])
Line3_0_1 = add_line(start= [ 12.7, -12.7], end= [12.7, 12.7])
Line3_0_2 = add_line(start= [12.7, 12.7], end= [-12.7,  12.7])
Line3_0_3 = add_line(start= [-12.7,  12.7], end= [-12.7, -12.7])
Loop3_0 = add_loop(Curves3_0)
Profile3 = add_profile(Loops3)
Sketch3 = add_sketch(sketch_plane= SketchPlane3, profile= Profile3)
Extrude3 = add_extrude(sketch= Sketch3,
	operation= 1, type= 0, extent_one= 12.7, extent_two= 0.)
