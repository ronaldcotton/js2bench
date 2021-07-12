<center>

# js2bench
## JetStream2 Benchmark Automation in Python

[![License](https://img.shields.io/github/license/yilber/readme-boilerplate.svg)](https://github.com/Yilber/readme-boilerplate/blob/master/LICENSE)

>Windows and MacOS Selenium + Chromedriver Automation to run JetStream2 browser benchmarks using automation.  Works on completely from command line, allows multiple iterations, displays results as well as saves results in .json format.  64 different benchmark datapoints and a final synthetic benchmark is captured.  For more information about the benchmarks, read the [in-depth analysis](https://browserbench.org/JetStream2.0/in-depth.html) for details for the JetStream2 Benchmark Suite.

</center>

## Requirements

* Compatible version of Chrome installed
* Python 3.4 - 3.9 (Tested on Python 3.8.10 and 3.9.2)
* Chromedriver placed in same folder as js2bench.py (MacOS Users, control click chromedriver and open to allow app to run) - download appropriate version from https://chromedriver.chromium.org/downloads

## Download from Git

```sh
$ git clone https://github.com/roncotton/js2bench.git
$ cd js2bench
```

## Execution

(MacOS Users, use ```python3``` in place of ```python``` below.)
>1. (optional - recommended) Setup some type of virtual environment for the project depending on preference.
>2. From terminal: ```pip install -r requirements.txt```
>3. ```python -m js2bench.py``` (Wait several minutes for benchmark to complete)
>4. (optional parameters) ```-h``` or ```-help``` (for help) & ```-i``` or ```-iterations``` (+ number for number of iterations)  

## Example Output (on MacOS)

```
python3 js2bench.py
System Information (saved at /Users/roncotton/Documents/JetStream2/sysinfo.json):
{'OS': 'MacOS', 'Chrome Version': '91.0.4472.114 ', 'MacOS Version': '10.16', 'Python Version': '3.9.2'}
-- iteration 1 --
Benchmark Information (saved at /Users/roncotton/Documents/JetStream2/results1.json)
{'WSL': 0.448, 'UniPoker': 123.764, 'uglify-js-wtb': 12.362, 'typescript': 6.13, 'tsf-wasm': 27.778, 'tagcloud-SP': 126.252, 'string-unpack-code-SP': 227.546, 'stanford-crypto-sha256': 322.062, 'stanford-crypto-pbkdf2': 284.717, 'stanford-crypto-aes': 188.908, 'splay': 108.209, 'segmentation': 12.429, 'richards-wasm': 23.984, 'richards': 335.531, 'regexp': 164.0, 'regex-dna-SP': 286.785, 'raytrace': 236.394, 'quicksort-wasm': 181.369, 'prepack-wtb': 14.615, 'pdfjs': 55.474, 'OfflineAssembler': 46.726, 'octane-zlib': 14.887, 'octane-code-load': 455.473, 'navier-stokes': 302.767, 'n-body-SP': 419.218, 'multi-inspector-code-load': 219.119, 'ML': 33.573, 'mandreel': 47.186, 'lebab-wtb': 23.981, 'json-stringify-inspector': 81.091, 'json-parse-inspector': 71.463, 'jshint-wtb': 21.096, 'HashSet-wasm': 18.959, 'hash-map': 203.14, 'gcc-loops-wasm': 9.537, 'gbemu': 38.319, 'gaussian-blur': 143.93, 'float-mm.c': 6.795, 'FlightPlanner': 268.556, 'first-inspector-code-load': 106.564, 'espree-wtb': 19.808, 'earley-boyer': 240.174, 'delta-blue': 474.266, 'date-format-xparb-SP': 84.101, 'date-format-tofte-SP': 82.47, 'crypto-sha1-SP': 117.88, 'crypto-md5-SP': 107.203, 'crypto-aes-SP': 259.702, 'crypto': 476.358, 'coffeescript-wtb': 13.022, 'chai-wtb': 46.521, 'cdjs': 22.918, 'Box2D': 103.121, 'bomb-workers': 6.804, 'Basic': 242.486, 'base64-SP': 101.654, 'babylon-wtb': 20.536, 'Babylon': 220.495, 'async-fs': 55.819, 'Air': 164.925, 'ai-astar': 188.264, 'acorn-wtb': 18.089, '3d-raytrace-SP': 187.371, '3d-cube-SP': 172.303, '!Benchmark_Score': 71.432}
Benchmark Score: 71.432
```

## TODO

* Add Linux Compatibility
* Testing Framework

## Scaffolding

```text
├── js2bench.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Bugs

If you have questions, feature requests or a bug you want to report, please click [here](https://github.com/ronaldcotton/js2bench/issues) to file an issue.

## Author

* [**Ronald Cotton**](https://github.com/ronaldcotton)

## Version History

* 1.21.193 - added MacOS Support
* 1.0      - initial release

## Business Inquiry

For Python Automation for your company, feel free to email me at roncotton @ gmail dot com with the subject line of "Business Inquiry."

## License

Copyright (c) 2021 Ron Cotton

Usage is provided under the MIT License. See [LICENSE](https://github.com/ronaldcotton/js2bench//LICENSE) for the full details.

## References
* https://arstechnica.com/gadgets/2020/11/google-chrome-is-available-as-an-apple-m1-native-app-today/
