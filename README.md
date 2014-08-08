# Gang
[![Build Status](https://travis-ci.org/aspyatkin/gang.svg?branch=master)](https://travis-ci.org/aspyatkin/gang)  
Python dictionary with dot-style access

```python
from gang import subclass_object

d = dict(hello="world", lorem=list(dict(ipsum="dolor"), dict(sit="amet")))

g = subclass_object(d)

print(g.hello)  # world
print(g.lorem[0].ipsum)  # dolor
print(g.lorem[1].sit)  # amet
```

Another example
```python
from gang import subclass_object

grades = dict(
    Math=dict(
        all=[5,5,5,5],
        avg=5.0
    ),
    Biology=dict(
        all=[4,4,5,5],
        avg=4.5
    )
)

t = subclass_object(grades)

for klass, grades in t.iteritems():
    print('{0}\n  All: {1}\n  Average: {2:f}'.format(
        klass,
        str(grades.all),
        grades.avg
    ))
    
# Output
# Biology
#   All: [4, 4, 5, 5]
#   Average: 4.500000
# Math
#   All: [5, 5, 5, 5]
#   Average: 5.000000
```

_subclass\_object_ returns _GangDict_ or _GangList_, which are inherited from _dict_ and _list_. So you can use all method for standard dictionaries and lists.

Note that transformation to subclassed dict or list is "lazy". In the example above, the list in `d['lorem']` is not transformed until you call `g.lorem`. Unfortunately, it is not cached also. So each call to `g.lorem` will make new transformation. This can affect performance seriously.

I find this method useful to work with big config files in JSON or YAML.
If you don't want to deal with lots of `config['some_value_1']['some_value_2']...` and make code more readable, you can give it a try.
