### FactoryBoy One-to-One Demo (a.k.a. *`factoryboy_oto_demo`)*
I've played around with how to to one-to-one Factory creation with FactoryBoy
a number of times. With the latest version of FactoryBoy (2.9.2), I got tired of
chasing down "how I did it in the past", and decided to build a demo repo.

**Note, this demo is current for `factory-boy==v2.9.2`. It should work for every
2.9.x release, but may need to be modified for future releases.**

#### Types
There are two types of one-to-one mappings exposed in this demo. I'll call the
first version **Simple One-to-One**. This is where a `ModelA` has a `PK` that
points at `ModelB`, and vice-versa.

The second version (does it have a name?, we'll call it **Complex One-to-One**)
is a joint form of One-to-One mapping and One-to-Many mapping. I.e. `ModelA` has
a `PK` to `ModelB`, while `ModelB` is mapped to a particular `ModelA`.

#### Example
##### Simple One-to-One
In this repository, I've got a `Musician` with a `Profile`. They point at each
other. That's it. In the SQL world, sometimes it's handy to point backwards.
That's all.

##### Complex One-to-One
In this repository, I've got a `Musician` who has composed `Song`s. On its face
this is a One-to-Many mapping. However, in this example, a musician also has a
`best_song` and a `worst_song`. Suddenly there are two One-to-One mappings.


#### Testing
Download this repository, create a virtualenv, install the package, and run
pytest.

```
git clone https://github.com/dfee/factoryboy_oto_demo
cd factoryboy_oto_demo
python -m venv env
source env/bin/activate
pip install -e .
pytest
```
