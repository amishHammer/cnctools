# cnctools

Depends on pygcode https://github.com/fragmuffin/pygcode

## max-cords.py

Pull the min and max axis co-ordinates out of a file to see if it will run within the machine working envelope.

```shell
python2.7 max-cords.py ../g-code/part.gcode
```

Output

```
Min X: -0.690800
Max X: 17.052400
Min Y: -3.568900
Max Y: 0.515300
Min Z: 0.000000
Max Z: 3.700000
X Travel: 17.743200
Y Travel: 4.084200
Z Travel: 3.700000
```
