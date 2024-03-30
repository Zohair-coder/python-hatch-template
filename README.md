Template for a typical hatch project.

Upgrade version of the project using:

```
hatch version [major|minor|micro]
```

Build the project using:

```
hatch build -c
```

Publish the project using:

```
hatch publish [-r <main|test>]
```

To run the tests, first install pytest:
    
```
pip install pytest
```

Then install the project in editable mode:

```
pip install -e .
```

Then run the tests:

```

And finally, run the tests:

```
pytest tests
```