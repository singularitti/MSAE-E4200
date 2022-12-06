#!/usr/bin/env wolframscript
(* ::Package:: *)

Clear["Global`*"]

kappa = {{2, -1, -1}, {-1, 2, -1}, {-1, -1, 2}};

sq3 = 1 / Sqrt[3]; p = Exp[I 2 Pi / 3]; q = Exp[I 4 Pi / 3];

v1 = sq3 {1, 1, 1};

v2 = sq3 {1, p, q};

v3 = sq3 {1, q, p};

v1 . kappa . v1

v2 . kappa . v2 //
ExpToTrig //
FullSimplify

v3 . kappa . v3 //
ExpToTrig //
FullSimplify

v2 . kappa . v3 //
ExpToTrig //
FullSimplify

v3 . kappa . v2 //
ExpToTrig //
FullSimplify

U = Transpose[{v1, v2, v3}]

Conjugate[Transpose[U]] . kappa . U // FullSimplify

Conjugate[Transpose[U]] . U // FullSimplify
