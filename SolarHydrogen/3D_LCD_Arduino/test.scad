
pcb_wid = 190;
pcb_len = 100;
pcb_thk = 1.6;

color("green") 
translate( [-50, -35, -10]) cube( [pcb_wid, pcb_len, pcb_thk]);

color("gray")
translate( [45, -30, 0])
scale( [25.4, 25.4, 25.4])
import("LCDKeypadShield.stl", 10);

color("#8080ff")
translate( [0, 0, 3])
rotate( [-90, 0, -90])
import("Arduino-UNO.stl", 10);
