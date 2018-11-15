#!/usr/bin/env wolframscript
(* ::Package:: *)

(* ::Input:: *)
(*a1={Sqrt[3]/2,1/2};a2={Sqrt[3]/2,-1/2};*)


(* ::Input:: *)
(*{b1,b2}=Inverse[{a1,a2}//Transpose];*)


(* ::Input:: *)
(*mapPointToBrillouinZone[Point[{k1_,k2_}]]:=Point[Transpose[{b1,b2}].{k1,k2}]*)


(* ::Input:: *)
(*nearestKPoints=Map[Point,{{0,1},{1,1},{1,0},{0,-1},{-1,-1},{-1,0}}];*)


(* ::Input:: *)
(*mapPointsToBrillouinZone[x:{__Point}]:=Map[First,Map[mapPointToBrillouinZone,x]]*)


(* ::Input:: *)
(*nearestKPointsPolygon=mapPointsToBrillouinZone[nearestKPoints]//Polygon*)


(* ::Input:: *)
(*k=Point[{1,-1}/3/2+{1,1}/2]//mapPointToBrillouinZone*)


(* ::Input:: *)
(*cn[t_]:={{Cos[t],-Sin[t]},{Sin[t],Cos[t]}}*)


(* ::Input:: *)
(*FBZ=Polygon[Map[cn,{0,Pi/3,2 Pi/3,Pi,4 Pi/3,5 Pi/3}].First[k]];*)


(* ::Input:: *)
(*plot[Point[{k1_,k2_}]]:=Graphics[{{Red,nearestKPointsPolygon},{Yellow,FBZ},mapPointToBrillouinZone[Point[{k1,k2}]]}]*)


(* ::Input:: *)
(*plot[x:{Point[{_,_}]...}]:=Graphics[{{Red,nearestKPointsPolygon},{Yellow,FBZ},Point[mapPointsToBrillouinZone[x]]}]*)


(* ::Input:: *)
(*basis1={{1/3,0},{1/2,0}};*)


(* ::Input:: *)
(*basis2={{0,1/3},{0,1/2}};*)


(* ::Input:: *)
(*gen=Table[Table[m basis1[[i]]+n basis2[[j]],{m,-3,3},{n,-3,3}],{i,1,2},{j,1,2}]//Flatten[#,3]&;*)


(* ::Input:: *)
(*Append[gen,{0,0}]//Map[Point,#]&//plot*)


(* ::Input:: *)
(*plot[Table[m{1/3,0}+n{0,1/3},{m,-2,2},{n,-2,2}]//Flatten[#,1]&//Map[Point,#]&]*)


(* ::Input:: *)
(*plot[{{0,0},{1/3,0},{0,1/3},{1/3,1/3},{-1/3,-1/3},{-1/3,0},{0,-1/3},{2/3,1/3},{1/3,2/3},{1/3,-1/3},{-1/3,1/3},{-1/3,-2/3},{-2/3,-1/3}}//Map[Point,#]&]*)
