# aliases: notebooks

a [bluer Jupyter Notebook](../../assets/template.ipynb).

```bash
@notebooks \
	build \
	[<notebook-name>]
 . build <notebook-name>.
@notebooks \
	code \
	[<notebook-name>]
 . code <notebook-name>.
@notebooks \
	connect \
	[ip=<1-2-3-4>,setup]
 . connect to jupyter notebook on ec2:<1-2-3-4>.
@notebooks \
	create | touch \
	<notebook-name> | <path>/<notebook-name> | notebook
 . create <notebook-name>.
@notebooks \
	host \
	[setup]
 . host jupyter notebook on ec2.
@notebooks \
	open \
	[<notebook-name> | notebook] \
	[<args>]
 . open <notebook-name>.
```
