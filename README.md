# strongtypes
Enforce strong types on Python function calls

The strongtypes module is an experiment to explore
how parameter type checking could work without
polluting function bodies with extraneous checks.

This quickly evolved to function decorators, which
is a nonintrusive way to feasibly implement this.
The @prototype decorator moves type checking away from
the function body, and can be easily removed once
code is tested.

There are some limitations, like handling named
arguments, or arbitrary lists. The current implementation
enforces types only on a fixed number of parameters.
