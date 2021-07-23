# PyTorch Java Demo

This repository is a demonstration of how to use PyTorch from Java.

## Setup

Download and unpack libtorch nightly (or 1.4 or greater).
From the pytorch.org homepage under "Quick Start Locally",
make sure "LibTorch" is the selected package.
Linux is supported as of version 1.4.
Mac is supported as of version 1.5.
Windows is supported as of version 1.9.
All are both supported in nightly builds.

Run `export LIBTORCH_HOME=/path/to/libtorch`.
The `build.gradle` file will use this to set `java.library.path`
when running the application.
If you are using PyTorch in your own environment,
`LIBTORCH_HOME` is not necessary.
Instead, you will need to set `java.library.path` to `/path/to/libtorch/lib`.

It might be necessary to set the JAVA_HOME environment variable.
On Mac, use `export JAVA_HOME=$(/usr/libexec/java_home)`.
On Windows, with GitHub bash, try `export JAVA_HOME=/c/Progra~1/Java/jdk-*`

On Mac, you might get security errors.
You must manually approve execution for each library under libtorch.
As a shortcut, `xattr -r -d /path/to/libtorch/lib` might work.

On Windows, you will probably need to run
`export PATH="$LIBTORCH_HOME/lib:$PATH"`.

If using a nightly build, run `export USE_LIBTORCH_NIGHTLY=1`.

Run `./gradlew run` to build and run the demo application.
It will load `demo-model.pt` and run it on some simple data.
[This notebook](TorchScriptForJavaDemo.ipynb) was used to generate the model.

More information about the Java API and TorchScript:
- [TorchScript tutorial](https://pytorch.org/tutorials/beginner/Intro_to_TorchScript_tutorial.html)
- [TorchScript reference](https://pytorch.org/docs/stable/jit.html)
- [Loading TorchScript in C++](https://pytorch.org/tutorials/advanced/cpp_export.html)
- [JavaDoc](https://pytorch.org/javadoc/)
- [PyTorch Android tutorial](https://pytorch.org/mobile/android/)
