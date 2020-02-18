with import <nixpkgs> {};
mkShell {
  buildInputs = [
    poetry
    python38Full
  ];
}
