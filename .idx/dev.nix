{ pkgs, ... }: {

  # Specification of the preferred Nixpkgs channel for package management.
  channel = "stable-23.11";  # Alternatively, consider using "unstable" for cutting-edge updates.

  # Package search can be facilitated via the Nix package repository at https://search.nixos.org/packages
  packages = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.sudo                    # Add sudo to the development environment
  ];

  # Defines environment variables for your workspace—customize as necessary.
  env = {};

  idx = {
    # To extend functionality, browse https://open-vsx.org/ for desired extensions and use the "publisher.id" format.
    extensions = [
      "ms-python.debugpy"
      "ms-python.python"
      "esbenp.prettier-vscode"
    ];

    # Used to show previews of projects
    previews = {
      enable = false;
      previews = {
        # Not needed for this project.
      };
    };

    # Lifecycle hooks for workspace management
    workspace = {
      # Hook triggered upon initial workspace creation.
      onCreate = {
        default.openFiles = [ "src/main.py" ];
      };

      # Hook triggered each time the workspace is started or restarted.
      onStart = {
        # No activation logic needed
      };
    };
  };
}
