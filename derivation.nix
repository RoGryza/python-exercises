{ pkgs, lib, poetry2nix, python3, ... }:
with lib;
let
  env = poetry2nix.mkPoetryEnv {
    python = python3;
    poetrylock = ./poetry.lock;
  };
  filterSrc = name: _: let baseName = baseNameOf name; in !(baseName == ".git" || baseName == "build");
in

pkgs.stdenv.mkDerivation {
  name = "aulas.rogryza.me";

  src = cleanSourceWith { src = ./.; filter = filterSrc; };
  dontMakeSourcesWriteable = 1;

  buildPhase = ''${env}/bin/python build.py'';
  installPhase = ''mkdir -p $out/static && cp -a build/* $out/static'';
}
