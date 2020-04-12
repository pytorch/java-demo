# PyTorch Java Demo

This repository is a demonstration of how to use PyTorch from Java.

## Setup

Download and unpack libtorch nightly (or 1.4 or greater).
From the pytorch.org homepage under "Quick Start Locally",
make sure "LibTorch" is the selected package.
Linux is supported as of version 1.4.  Mac is supported as of version 1.5.
Linux and Mac are both supported in nightly builds.
Windows is not supported at this time.

Run `export LIBTORCH_HOME=/path/to/libtorch`.
The `build.gradle` file will use this to set `java.library.path`
when running the application.
If you are using PyTorch in your own environment,
`LIBTORCH_HOME` is not necessary.
Instead, you will need to set `java.library.path` to `/path/to/libtorch/lib`.

If using a nightly build, you also need to run this command `export USE_LIBTORCH_NIGHTLY=1`.

Run `./gradlew run` to build and run the demo application.
It will load `demo-model.pt` and run it on some simple data.

Note: For macOS users, if you run into OS security issue regarding  "libpytorch_jni.dylib" run `xattr -r -d /path/to/libtorch/lib` to resolve that OS issue and then `./gradlew run` to build and run the demo application.

[This notebook](TorchScriptForJavaDemo.ipynb) was used to generate the model.

More information about the Java API and TorchScript:
- [TorchScript tutorial](https://pytorch.org/tutorials/beginner/Intro_to_TorchScript_tutorial.html)
- [TorchScript reference](https://pytorch.org/docs/stable/jit.html)
- [Loading TorchScript in C++](https://pytorch.org/tutorials/advanced/cpp_export.html)
- [PyTorch-style JavaDoc](https://pytorch.org/docs/stable/packages.html)
- [Standard JavaDoc](https://pytorch.org/javadoc/1.4.0/)
- [PyTorch Android tutorial](https://pytorch.org/mobile/android/)
