{ pkgs, lib, config, inputs, ... }:

{
  # https://devenv.sh/basics/
  env.GREET = "Flask Named Entity Finder";

  # https://devenv.sh/packages/
  packages = [

  ];

  # https://devenv.sh/scripts/
  scripts.hello.exec = "echo *** Hello from $GREET! ***";

  enterShell = ''
    hello
  '';

  # https://devenv.sh/tests/
  enterTest = ''
    echo "*** Installing Named Entity Finder as package ***"
    pip install -e .
    echo "*** Running Python tests ***"
    python -m pytest
  '';

  # https://devenv.sh/services/
  # services.postgres.enable = true;

  # https://devenv.sh/languages/
  languages.python = {
    enable = true;
    venv.enable = true;
    venv.requirements = ''
      flask
      parameterized
      pytest
      selenium
      spacy
    '';
  };

  # https://devenv.sh/pre-commit-hooks/
  # pre-commit.hooks.shellcheck.enable = true;

  # https://devenv.sh/processes/
  # processes.ping.exec = "ping example.com";

  # See full reference at https://devenv.sh/reference/options/
}
