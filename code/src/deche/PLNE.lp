\ Model PLNE
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  x[0,0] + x[1,0] + x[2,0] + x[3,0] + x[0,1] + x[1,1] + x[2,1] + x[3,1]
   + x[0,2] + x[1,2] + x[2,2] + x[3,2] + x[0,3] + x[1,3] + x[2,3] + x[3,3]
   + x[0,4] + x[1,4] + x[2,4] + x[3,4]
Subject To
 linecontraintre[0,0,1]: y[0,0,1] + y[0,1,1] + y[0,2,1] <= 3
 colonecontraintre[0,0,1]: z[0,0,1] <= 1
 colonecontraintre[0,0,2]: z[0,0,2] <= 1
 colonecontraintre[1,0,1]: z[1,0,1] <= 1
 colonecontraintre[1,0,2]: z[1,0,2] <= 1
 linecontraintre[2,0,1]: y[2,0,1] <= 1
 linecontraintre[2,0,2]: y[2,0,2] <= 1
 linecontraintre[2,0,3]: y[2,0,3] <= 1
 colonecontraintre[2,0,1]: z[2,0,1] <= 1
 colonecontraintre[2,0,2]: z[2,0,2] <= 1
 linecontraintre[3,0,1]: y[3,0,1] + y[3,1,1] + y[3,2,1] <= 3
 colonecontraintre[3,0,1]: z[3,0,1] <= 1
 colonecontraintre[3,0,2]: z[3,0,2] <= 1
 linecontraintre[0,1,1]: y[0,1,1] + y[0,2,1] + y[0,3,1] <= 3
 colonecontraintre[0,1,1]: z[0,1,1] <= 1
 colonecontraintre[1,1,1]: z[1,1,1] <= 1
 linecontraintre[2,1,1]: y[2,1,1] <= 1
 linecontraintre[2,1,2]: y[2,1,2] <= 1
 linecontraintre[2,1,3]: y[2,1,3] <= 1
 colonecontraintre[2,1,1]: z[2,1,1] <= 1
 linecontraintre[3,1,1]: y[3,1,1] + y[3,2,1] + y[3,3,1] <= 3
 colonecontraintre[3,1,1]: z[3,1,1] <= 1
 linecontraintre[0,2,1]: y[0,2,1] + y[0,3,1] + y[0,4,1] <= 3
 colonecontraintre[0,2,1]: z[0,2,1] <= 1
 colonecontraintre[0,2,2]: z[0,2,2] + z[1,2,2] <= 2
 colonecontraintre[1,2,1]: z[1,2,1] <= 1
 colonecontraintre[1,2,2]: z[1,2,2] + z[2,2,2] <= 2
 linecontraintre[2,2,1]: y[2,2,1] <= 1
 linecontraintre[2,2,2]: y[2,2,2] <= 1
 linecontraintre[2,2,3]: y[2,2,3] <= 1
 colonecontraintre[2,2,1]: z[2,2,1] <= 1
 colonecontraintre[2,2,2]: z[2,2,2] + z[3,2,2] <= 2
 linecontraintre[3,2,1]: y[3,2,1] + y[3,3,1] + y[3,4,1] <= 3
 colonecontraintre[3,2,1]: z[3,2,1] <= 1
 colonecontraintre[3,2,2]: z[3,2,2] <= 2
 linecontraintre[0,3,1]: y[0,3,1] + y[0,4,1] <= 3
 colonecontraintre[0,3,1]: z[0,3,1] <= 1
 colonecontraintre[1,3,1]: z[1,3,1] <= 1
 linecontraintre[2,3,1]: y[2,3,1] <= 1
 linecontraintre[2,3,2]: y[2,3,2] <= 1
 linecontraintre[2,3,3]: y[2,3,3] <= 1
 colonecontraintre[2,3,1]: z[2,3,1] <= 1
 linecontraintre[3,3,1]: y[3,3,1] + y[3,4,1] <= 3
 colonecontraintre[3,3,1]: z[3,3,1] <= 1
 linecontraintre[0,4,1]: y[0,4,1] <= 3
 colonecontraintre[0,4,1]: z[0,4,1] + z[1,4,1] <= 2
 colonecontraintre[1,4,1]: z[1,4,1] + z[2,4,1] <= 2
 linecontraintre[2,4,1]: y[2,4,1] <= 1
 linecontraintre[2,4,2]: y[2,4,2] <= 1
 linecontraintre[2,4,3]: y[2,4,3] <= 1
 colonecontraintre[2,4,1]: z[2,4,1] + z[3,4,1] <= 2
 linecontraintre[3,4,1]: y[3,4,1] <= 3
 colonecontraintre[3,4,1]: z[3,4,1] <= 2
 Q12[2,0,1]: y[2,0,1] + y[2,1,2] <= 1
 Q12[2,0,2]: y[2,0,2] + y[2,1,3] <= 1
 Q12[2,1,1]: y[2,1,1] + y[2,2,2] <= 1
 Q12[2,1,2]: y[2,1,2] + y[2,2,3] <= 1
 Q12[2,2,1]: y[2,2,1] + y[2,3,2] <= 1
 Q12[2,2,2]: y[2,2,2] + y[2,3,3] <= 1
 Q12[2,3,1]: y[2,3,1] + y[2,4,2] <= 1
 Q12[2,3,2]: y[2,3,2] + y[2,4,3] <= 1
 coloneedalitedesxi[0,0,1]: - x[0,0] + [ y[0,0,1] * z[0,0,1]
   + y[0,0,1] * z[0,0,2] ] = 0
 coloneedalitedesxi[1,0,1]: - x[1,0] = 0
 coloneedalitedesxi[2,0,1]: - x[2,0] + [ y[2,0,1] * z[2,0,1]
   + y[2,0,1] * z[2,0,2] + y[2,0,2] * z[2,0,1] + y[2,0,2] * z[2,0,2]
   + y[2,0,3] * z[2,0,1] + y[2,0,3] * z[2,0,2] ] = 0
 coloneedalitedesxi[3,0,1]: - x[3,0] + [ y[3,0,1] * z[3,0,1]
   + y[3,0,1] * z[3,0,2] ] = 0
 coloneedalitedesxi[0,1,1]: - x[0,1] + [ y[0,1,1] * z[0,1,1] ] = 0
 coloneedalitedesxi[1,1,1]: - x[1,1] = 0
 coloneedalitedesxi[2,1,1]: - x[2,1] + [ y[2,1,1] * z[2,1,1]
   + y[2,1,2] * z[2,1,1] + y[2,1,3] * z[2,1,1] ] = 0
 coloneedalitedesxi[3,1,1]: - x[3,1] + [ y[3,1,1] * z[3,1,1] ] = 0
 coloneedalitedesxi[0,2,1]: - x[0,2] + [ y[0,2,1] * z[0,2,1]
   + y[0,2,1] * z[0,2,2] ] = 0
 coloneedalitedesxi[1,2,1]: - x[1,2] = 0
 coloneedalitedesxi[2,2,1]: - x[2,2] + [ y[2,2,1] * z[2,2,1]
   + y[2,2,1] * z[2,2,2] + y[2,2,2] * z[2,2,1] + y[2,2,2] * z[2,2,2]
   + y[2,2,3] * z[2,2,1] + y[2,2,3] * z[2,2,2] ] = 0
 coloneedalitedesxi[3,2,1]: - x[3,2] + [ y[3,2,1] * z[3,2,1]
   + y[3,2,1] * z[3,2,2] ] = 0
 coloneedalitedesxi[0,3,1]: - x[0,3] + [ y[0,3,1] * z[0,3,1] ] = 0
 coloneedalitedesxi[1,3,1]: - x[1,3] = 0
 coloneedalitedesxi[2,3,1]: - x[2,3] + [ y[2,3,1] * z[2,3,1]
   + y[2,3,2] * z[2,3,1] + y[2,3,3] * z[2,3,1] ] = 0
 coloneedalitedesxi[3,3,1]: - x[3,3] + [ y[3,3,1] * z[3,3,1] ] = 0
 coloneedalitedesxi[0,4,1]: - x[0,4] + [ y[0,4,1] * z[0,4,1] ] = 0
 coloneedalitedesxi[1,4,1]: - x[1,4] = 0
 coloneedalitedesxi[2,4,1]: - x[2,4] + [ y[2,4,1] * z[2,4,1]
   + y[2,4,2] * z[2,4,1] + y[2,4,3] * z[2,4,1] ] = 0
 coloneedalitedesxi[3,4,1]: - x[3,4] + [ y[3,4,1] * z[3,4,1] ] = 0
Bounds
Binaries
 x[0,0] y[0,0,1] z[0,0,1] z[0,0,2] x[1,0] z[1,0,1] z[1,0,2] x[2,0] y[2,0,1]
 y[2,0,2] y[2,0,3] z[2,0,1] z[2,0,2] x[3,0] y[3,0,1] z[3,0,1] z[3,0,2]
 x[0,1] y[0,1,1] z[0,1,1] x[1,1] z[1,1,1] x[2,1] y[2,1,1] y[2,1,2] y[2,1,3]
 z[2,1,1] x[3,1] y[3,1,1] z[3,1,1] x[0,2] y[0,2,1] z[0,2,1] z[0,2,2] x[1,2]
 z[1,2,1] z[1,2,2] x[2,2] y[2,2,1] y[2,2,2] y[2,2,3] z[2,2,1] z[2,2,2]
 x[3,2] y[3,2,1] z[3,2,1] z[3,2,2] x[0,3] y[0,3,1] z[0,3,1] x[1,3] z[1,3,1]
 x[2,3] y[2,3,1] y[2,3,2] y[2,3,3] z[2,3,1] x[3,3] y[3,3,1] z[3,3,1] x[0,4]
 y[0,4,1] z[0,4,1] x[1,4] z[1,4,1] x[2,4] y[2,4,1] y[2,4,2] y[2,4,3]
 z[2,4,1] x[3,4] y[3,4,1] z[3,4,1]
End
