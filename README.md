# I2C-12-bit-binary-counter

This repository will give the hardware and sample software for a counter that can be used on
most any device that needs accumulated counts.  I do not plan on updating it but welcome forks.

An I2C counter using the MCP23017 GPIO and two 74LS590 cascaded binary counters
This board I have designed uses two 74LS590 counters in series.  These 8 bit counters have a buffered output stored by an input and a clear counters  input.  They count on a positive going pulse*.  When the first counter in the series of two rolls over at 256 it triggers the second to count one.  The buffered outputs of these two chips are read by an MCP23017 GPIO expander.  Only four of the count buffer outputs from the second 74LS590 are used leaving four GPIOO from the MCP23017.  These are used one each for the CLR pins and the RCK (store buffer) pins, one to enable an LED so the count pulse can be seen and one left open. *The Hall effect sensor out is pulled high by a 1oK resistor and the LED count circuit. When the Hall Effect is triggered, it pulls the count low and when it inactivates again the input is again pulled high and the counter increments.   On the board I designed, I included two QWIIC connectors for daisy-chaining I2C devices and a more common 4 pin .1 centers connection point.  There are three address jumpers on the board bottom.The eagle files for the board can be downloaded from http:/hiddenridge.net/download/I2C_Counter.zip

The BOM for the board can be downloaded from http:/hiddenridge.net/download/oneboard.html
