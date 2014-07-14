# Gang
Python dictionary with dot-style access

```
from gang import subclass_object

d = dict(hello="world", lorem=list(dict(ipsum="dolor"), dict(sit="amet")))

g = subclass_object(d)

print(g.hello)  # world
print(g.lorem[0].ipsum)  # dolor
print(g.lorem[1].sit)  # amet
```

_subclass\_object_ return _GangDict_ or _GangList_, which are inherited from _dict_ and _list_. So you can use all method for standard dictionaries and lists.

Note that transformation to subclassed dict or list is "lazy". In the example above, the list in `d['lorem']` is not transformed until you call `g.lorem`. Unfortunately, it is not cached also. So each call to `g.lorem` will make new transformation. This can affect performance seriously.

I find this method useful to work with big config files in JSON or YAML.
If you don't want to deal with lots of `config['some_value_1']['some_value_2']...` and make code more readable, you can give it a try.