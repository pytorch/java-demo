package demo;

import org.pytorch.IValue;
import org.pytorch.Module;
import org.pytorch.Tensor;

import java.util.Arrays;

public class App {
  public static void main(String[] args) {
    Module mod = Module.load("demo-model.pt1");
    Tensor data =
        Tensor.fromBlob(
            new int[] {1, 2, 3, 4, 5, 6}, // data
            new long[] {2, 3} // shape
            );
    IValue result = mod.forward(IValue.from(data), IValue.from(3.0));
    Tensor output = result.toTensor();
    System.out.println("shape: " + Arrays.toString(output.shape()));
    System.out.println("data: " + Arrays.toString(output.getDataAsFloatArray()));

    // Workaround for https://github.com/facebookincubator/fbjni/issues/25
    System.exit(0);
  }
}
