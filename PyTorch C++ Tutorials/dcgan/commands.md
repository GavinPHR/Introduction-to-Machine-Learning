Commands to run to build the code in `build` directory:
```
mkdir build
cd build
cmake -DCMAKE_PREFIX_PATH=/Users/peng/Desktop/libtorch ..
cmake --build . --config Release
```
Replace my path to libtorch with your absolute path to libtorch
