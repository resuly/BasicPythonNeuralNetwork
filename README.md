# BasicPythonNeuralNetwork
Only use Numpy to build a basic neural network.

This is inspired by 

http://iamtrask.github.io/2015/07/12/basic-python-network/
https://medium.com/technology-invention-and-more/how-to-build-a-simple-neural-network-in-9-lines-of-python-code-cc8f23647ca1

Original Sample:

<table>
  <tbody><tr>
    <th colspan="3">Inputs</th>
    <th >Output</th>
  </tr>
  <tr>
    <td >0</td>
    <td>0</td>
    <td>1</td>
    <td>0</td>
  </tr>
  <tr>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>0</td>
  </tr>
  <tr>
    <td>1</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
</tbody></table>

“Error Weighted Derivative” formula:

Adjust weight by = np.dot(input.T, error*SigmoidCurveGradient(output))
