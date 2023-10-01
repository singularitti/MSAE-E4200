#!/usr/bin/env wolframscript
(* ::Package:: *)

Clear["Global`*"]
V=a (2z0-z1-z2)^2+(3a+b)(z1-z2)^2//Expand
D[V,z0]
D[V,z1]//Simplify
D[V,z2]//Simplify
