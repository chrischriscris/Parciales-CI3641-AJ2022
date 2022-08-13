all: preg4

preg4: src/main.rs
	cargo build --release
	mv target/release/preg4 .

newplot: genplot.py
	preg4 > out
	python genplot.py out

clean:
	rm preg4