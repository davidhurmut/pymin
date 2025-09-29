from minifier.core import minify
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit(1)
    infile, outfile = sys.argv[1], sys.argv[2]
    with open(infile, "r", encoding="utf-8") as f:
        code = f.read()
    minified = minify(code)
    with open(outfile, "w", encoding="utf-8") as f:
        f.write(minified)

if __name__ == "__main__":
    main()
