#!/usr/bin/env wolframscript
(* ::Package:: *)

a1 = {Sqrt[3] / 2, 1 / 2}; a2 = {Sqrt[3] / 2, -1 / 2};

{b1, b2} = Inverse[{a1, a2} // Transpose];

mapPointToBrillouinZone[Point[{k1_, k2_}]] :=
    Point[Transpose[{b1, b2}] . {k1, k2}]

nearestKPoints = Map[Point, {{0, 1}, {1, 1}, {1, 0}, {0, -1}, {-1, -1
    }, {-1, 0}}];

mapPointsToBrillouinZone[x : {__Point}] :=
    Map[First, Map[mapPointToBrillouinZone, x]]

nearestKPointsPolygon = mapPointsToBrillouinZone[nearestKPoints] // Polygon

k = Point[{1, -1} / 3 / 2 + {1, 1} / 2] // mapPointToBrillouinZone

cn[t_] :=
    {{Cos[t], -Sin[t]}, {Sin[t], Cos[t]}}

FBZ = Polygon[Map[cn, {0, Pi / 3, 2 Pi / 3, Pi, 4 Pi / 3, 5 Pi / 3}] 
    . First[k]];

plot[Point[{k1_, k2_}]] :=
    Graphics[{{Red, nearestKPointsPolygon}, {Yellow, FBZ}, mapPointToBrillouinZone[
        Point[{k1, k2}]]}]

plot[x : {Point[{_, _}]...}] :=
    Graphics[{{Red, nearestKPointsPolygon}, {Yellow, FBZ}, Point[mapPointsToBrillouinZone[
        x]]}]

basis1 = {{1 / 3, 0}, {1 / 2, 0}};

basis2 = {{0, 1 / 3}, {0, 1 / 2}};

gen = Table[Table[m basis1[[i]] + n basis2[[j]], {m, -3, 3}, {n, -3, 
    3}], {i, 1, 2}, {j, 1, 2}] // Flatten[#, 3]&;

Append[gen, {0, 0}] //
Map[Point, #]& //
plot

plot[
    Table[m {1 / 3, 0} + n {0, 1 / 3}, {m, -2, 2}, {n, -2, 2}] //
    Flatten[#, 1]& //
    Map[Point, #]&
]

plot[{{0, 0}, {1 / 3, 0}, {0, 1 / 3}, {1 / 3, 1 / 3}, {-1 / 3, -1 / 3
    }, {-1 / 3, 0}, {0, -1 / 3}, {2 / 3, 1 / 3}, {1 / 3, 2 / 3}, {1 / 3, 
    -1 / 3}, {-1 / 3, 1 / 3}, {-1 / 3, -2 / 3}, {-2 / 3, -1 / 3}} // Map[
    Point, #]&]
