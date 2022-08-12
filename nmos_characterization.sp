* gm/Id simulation
* public domain

.param ll=22n vg=1 vd=0.7 vdd=1.1
.inc 22nm_cmos.pm

vg vg 0 {vg}
vdn dn 0 {vd}
vdp dp 0 {-vd}
egn gn 0 vg 0 1
egp gp 0 vg 0 -1

mn dn gn 0 0 n_22n w=1u l=ll
mp dp gp 0 0 p_22n w=1u l=ll

.probe dc v(*) i(*)
.control
set filetype binary
set appendwrite
save all @mn[gm] @mn[id] @mn[cgs] @mn[cgg] @mn[cgd] @mn[gds] @mn[w] @mn[l]
+        @mp[gm] @mp[id] @mp[cgs] @mp[cgg] @mp[cgd] @mp[gds] @mp[w] @mp[l]
foreach tx_len 22n 40n 60n 80n 100n
alter @mn[l] = $tx_len
alter @mp[l] = $tx_len
* Vgs sweep
dc vg 0 1 0.01
write gmid.txt
end
.endc

.end