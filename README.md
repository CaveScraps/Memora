# Memora

Memora is a simple program designed to turn a raspberry pi into a digital photo frame.

## Installation
```bash
#Clone the repo and move into it.
git clone git@github.com:CaveScraps/Memora.git
cd Memora

#Give the setup script and program itself permission to run.
chmod +x setup.sh main.py

#Run the setup, this can take a little while.
./setup.sh
```

## Usage

Dump your images into the `images/` folder then
```bash
#Run the program.
./main.py
```

A fullscreen window will open and display the images placed in the `images/` folder,
to exit fullscreen hit `q` with the window in focus.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Github actions must pass on your changeset before merging will be considered.

## License

[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
