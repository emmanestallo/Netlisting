* MOS Characterization

* Include model files
.include 22nm_cmos.pm
.options TEMP = 27

* Netlist parameters
vd drain 0 dc 0.6
vg gate 0 dc 0.6
mn0 drain gate 0 0 n_22n l=100n w=1u


.dc vg 0 1 0.001
.op

.print dc format=csv N(mn0:gm) N(mn0:vth) N(mn0:cgd) N(mn0:cgs) N(mn0:gds) i(vd) vg

.end
