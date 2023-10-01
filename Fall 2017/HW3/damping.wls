#!/usr/bin/env wolframscript
(* ::Package:: *)

Clear["Global`*"]
s=FullSimplify[(x/.DSolve[{m x''[t]+g x'[t]==-k x[t]+f0 Cos[w t],x'[0]==x0,x[0]==v0},x,t][[1]])[t]]
Manipulate[Plot[{(E^(-(((g+Sqrt[g^2-4 k m]) t)/(2 m))) (f0 ((1+E^((Sqrt[g^2-4 k m] t)/m)) Sqrt[g^2-4 k m] (-k+m w^2)-(-1+E^((Sqrt[g^2-4 k m] t)/m)) g (k+m w^2))+(g^2 w^2+(k-m w^2)^2) (-g v0+Sqrt[g^2-4 k m] v0+E^((Sqrt[g^2-4 k m] t)/m) Sqrt[g^2-4 k m] v0-2 m x0+E^((Sqrt[g^2-4 k m] t)/m) (g v0+2 m x0))+2 E^(((g+Sqrt[g^2-4 k m]) t)/(2 m)) f0 Sqrt[g^2-4 k m] ((k-m w^2) Cos[t w]+g w Sin[t w])))/(2 Sqrt[g^2-4 k m] (g^2 w^2+(k-m w^2)^2)),0.1UnitStep[t]Cos[w t]},{t,0,t0},PlotLegends->{"x(t)","0.1 F(t)"}],{f0,1,1},{g,0,1},{k,16,16},{m,1,1},{t0,10,1000},{v0,-2,2},{w,0,20},{x0,-2,2}]
