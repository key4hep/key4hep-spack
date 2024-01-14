# This will delete unused (from example from a previous failed installation) specs that
# are no longer in the current installation
spack -e . python -c 'from spack.cmd import uninstall; uninstall.do_uninstall([x for x in spack.store.STORE.db.query_local() if not any(x.satisfies(y) for y in spack.environment.active_environment().all_specs_generator())], False)'
