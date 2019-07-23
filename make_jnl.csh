#!/bin/csh
set dfile=$argv[1]
set var=$argv[2]
set n=$argv[3]
set date=$argv[4]
set time=$argv[5]
set lon=$argv[6]
set lat=$argv[7]
set lev=$argv[8]
set tyid=$argv[9]
set output=ferret_go.jnl

#set lev="(0,400,40)"
#set tyid="1013"

echo "use $dfile" > $output
echo "go tymap.jnl $date $time $lon $lat $var $lev " '"'./OUTPUT/ty${tyid}_${var}_$n'"' >> $output
echo "quit" >> $output


