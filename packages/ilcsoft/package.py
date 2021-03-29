from datetime import datetime
import os
import platform
import llnl.util.tty as tty
import spack.architecture as architecture
from spack.main import get_version
import spack.user_environment as uenv
from spack.pkg.k4.Ilcsoftpackage import k4_add_latest_commit_as_dependency 
from spack.pkg.k4.Ilcsoftpackage import k4_generate_setup_script 
from spack.pkg.k4.Ilcsoftpackage import Key4hepPackage


class Ilcsoft(BundlePackage, Key4hepPackage):
    """Bundle package to install Ilcsoft"""
    
    homepage = 'https://cern.ch/key4hep'

    ##################### versions ########################
    #######################################################
    ###  nightly builds
    # builds the HEAD of each package for which 
    # k4_add_latest_commit_as_dependency is called below
    version('master')
    # this version can be extended with additional version
    # fields to differentiate it, like 'master-2020-10-10'
    #
    ### stable builds
    # builds the latest release of each package
    # the preferred usage is to use the date as version, like:
    version(datetime.today().strftime('%Y-%m-%d'))
    #version('2020-10-06') # example, no need to add here.
    # more complex version configurations should be added in an
    # environment

    # this bundle package installs a custom setup script, so
    # need to add the install phase (which normally does not
    # exist for a bundle package)
    phases = ['install']

    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))

    ############################### key4hep ###############
    #######################################################
    

    depends_on("guinea-pig")
    # todo: figure out the api for the cern gitlab instance
    #depends_on('guinea-pig@master', when="@master")

    depends_on('whizard +lcio +openloops hepmc=2')
    # todo: figure out the api for the whizard gitlab instance
    #depends_on('whizard@master +lcio +openloops hepmc=2', when="@master")

    depends_on("k4lcioreader")
    k4_add_latest_commit_as_dependency("k4lcioreader", "key4hep/k4LCIOReader", when="@master")

    depends_on("k4simdelphes")
    k4_add_latest_commit_as_dependency("k4simdelphes", "key4hep/k4SimDelphes", when="@master",
				 giturl="https://api.github.com/repos/%s/commits/main")

    depends_on("delphes")
    k4_add_latest_commit_as_dependency("delphes", "delphes/delphes", when="@master")


    ############################### ilcsoft ###############
    #######################################################
    depends_on('aidatt')
    k4_add_latest_commit_as_dependency("aidatt", "aidasoft/aidatt", when="@master")

    depends_on('cedviewer')
    k4_add_latest_commit_as_dependency("cedviewer", "ilcsoft/cedviewer", when="@master")

    depends_on('conformaltracking')
    k4_add_latest_commit_as_dependency("conformaltracking", "ilcsoft/conformaltracking", when="@master")

    depends_on('clicperformance')
    k4_add_latest_commit_as_dependency("clicperformance", "ilcsoft/clicperformance", when="@master")

    depends_on('clupatra')
    k4_add_latest_commit_as_dependency("clupatra", "ilcsoft/clupatra", when="@master")

    depends_on('ced')
    k4_add_latest_commit_as_dependency("ced", "ilcsoft/ced", when="@master")

    depends_on('ddkaltest')
    k4_add_latest_commit_as_dependency("ddkaltest", "ilcsoft/ddkaltest", when="@master")

    depends_on('ddmarlinpandora')
    k4_add_latest_commit_as_dependency("ddmarlinpandora", "ilcsoft/ddmarlinpandora", when="@master")

    depends_on('fcalclusterer')
    k4_add_latest_commit_as_dependency("fcalclusterer", "fcalsw/fcalclusterer", when="@master")

    depends_on('forwardtracking')
    k4_add_latest_commit_as_dependency("forwardtracking", "ilcsoft/forwardtracking", when="@master")

    depends_on('garlic')
    k4_add_latest_commit_as_dependency("garlic", "ilcsoft/garlic", when="@master")

    depends_on('k4marlinwrapper')
    k4_add_latest_commit_as_dependency("k4marlinwrapper", "key4hep/k4marlinwrapper", when="@master")

    depends_on('generalbrokenlines')
    k4_add_latest_commit_as_dependency("generalbrokenlines", "GeneralBrokenLines/GeneralBrokenLines", when="@master")

    depends_on('gear')
    k4_add_latest_commit_as_dependency("gear", "ilcsoft/gear", when="@master")

    depends_on('ilcutil')
    k4_add_latest_commit_as_dependency("ilcutil", "ilcsoft/ilcutil", when="@master")

    depends_on('ildperformance')
    k4_add_latest_commit_as_dependency("ildperformance", "ilcsoft/ildperformance", when="@master")

    depends_on('kaldet')
    k4_add_latest_commit_as_dependency("kaldet", "ilcsoft/kaldet", when="@master")

    depends_on('kitrackmarlin')
    k4_add_latest_commit_as_dependency("kitrackmarlin", "ilcsoft/kitrackmarlin", when="@master")

    depends_on('kaltest')
    k4_add_latest_commit_as_dependency("kaltest", "ilcsoft/kaltest", when="@master")

    depends_on('kitrack')
    k4_add_latest_commit_as_dependency("kitrack", "ilcsoft/kitrack", when="@master")

    depends_on('lcfiplus')
    k4_add_latest_commit_as_dependency("lcfiplus", "lcfiplus/lcfiplus", when="@master")

    depends_on('lctuple')
    k4_add_latest_commit_as_dependency("lctuple", "ilcsoft/lctuple", when="@master")

    depends_on('lcfivertex')
    k4_add_latest_commit_as_dependency("lcfivertex", "ilcsoft/lcfivertex", when="@master")

    depends_on('lich')
    k4_add_latest_commit_as_dependency("lich", "danerdaner/lich", when="@master")

    depends_on('lccd')
    k4_add_latest_commit_as_dependency("lccd", "ilcsoft/lccd", when="@master")

    depends_on('lcio')
    k4_add_latest_commit_as_dependency("lcio", "ilcsoft/lcio", when="@master")

    depends_on('lcgeo')
    k4_add_latest_commit_as_dependency("lcgeo", "ilcsoft/lcgeo", when="@master")

    depends_on('marlin')
    k4_add_latest_commit_as_dependency("marlin", "ilcsoft/marlin", when="@master")

    depends_on('marlinutil')
    k4_add_latest_commit_as_dependency("marlinutil", "ilcsoft/marlinutil", when="@master")

    depends_on('marlinpandora')
    k4_add_latest_commit_as_dependency("marlinpandora", "pandorapfa/marlinpandora", when="@master")

    depends_on("marlindd4hep")
    k4_add_latest_commit_as_dependency("marlindd4hep", "ilcsoft/marlindd4hep", when="@master")

    depends_on('marlinreco')
    k4_add_latest_commit_as_dependency("marlinreco", "ilcsoft/marlinreco", when="@master")

    depends_on('marlinfastjet')
    k4_add_latest_commit_as_dependency("marlinfastjet", "ilcsoft/marlinfastjet", when="@master")

    depends_on('marlinkinfit')
    k4_add_latest_commit_as_dependency("marlinkinfit", "ilcsoft/marlinkinfit", when="@master")

    depends_on('marlinkinfitprocessors')
    k4_add_latest_commit_as_dependency('marlinkinfitprocessors', 'ilcsoft/marlinkinfitprocessors', when='@master')

    depends_on('marlintrkprocessors')
    k4_add_latest_commit_as_dependency("marlintrkprocessors", "ilcsoft/marlintrkprocessors", when="@master")

    depends_on('marlintrk')
    k4_add_latest_commit_as_dependency("marlintrk", "ilcsoft/marlintrk", when="@master")

    depends_on('overlay')
    k4_add_latest_commit_as_dependency("overlay", "ilcsoft/overlay", when="@master")

    depends_on('pandoraanalysis')
    k4_add_latest_commit_as_dependency("pandoraanalysis", "PandoraPFA/LCPandoraAnalysis", when="@master")

    depends_on('pandorapfa')
    #k4_add_latest_commit_as_dependency("pandorapfa", "pandorapfa/pandorapfa", when="@master")


    depends_on('physsim')
    k4_add_latest_commit_as_dependency("physsim", "ilcsoft/physsim", when="@master")

    depends_on("raida")
    k4_add_latest_commit_as_dependency("raida", "ilcsoft/raida", when="@master")

    depends_on('sio')
    k4_add_latest_commit_as_dependency("sio", "ilcsoft/sio", when="@master")




    ##################### developer tools #################
    #######################################################
    depends_on("cmake")
    depends_on("ninja")

    ##################### conflicts #######################
    #######################################################
    conflicts("%gcc@8.3.1",
              msg="There are known issues with compilers from redhat's devtoolsets" \
              "which are therefore not supported." \
              "See https://root-forum.cern.ch/t/devtoolset-gcc-toolset-compatibility/38286")


    def setup_run_environment(self, spack_env):
        # set locale to avoid certain issues with xerces-c
        # (see https://github.com/key4hep/key4hep-spack/issues/170)
        spack_env.set("LC_ALL", "C")


    def install(self, spec, prefix):
      """ Create bash setup script in prefix."""
      # first, log spack version to build-out
      tty.msg('* **Spack:**', get_version())
      tty.msg('* **Python:**', platform.python_version())
      tty.msg('* **Platform:**', architecture.Arch(
          architecture.platform(), 'frontend', 'frontend'))
      # get all dependency specs, including compiler
      with spack.store.db.read_transaction():
               specs = [dep for dep in spec.traverse(order='post')]
               try: 
                   gcc_spec = spack.cmd.disambiguate_spec(str(spec.compiler), 
                                                          None,
                                                          first=True)
                   gcc_specs = [dep for dep in gcc_spec.traverse( order='post')]
                   specs = specs + gcc_specs
               except:
                   tty.warn("No spec found for " + str(spec.compiler) +
                            ". Assuming it is a system compiler,"
                            "not adding it to the setup.")
      # record all changes to the environment by packages in the stack
      env_mod = spack.util.environment.EnvironmentModifications()
      for _spec in specs:
          env_mod.extend(uenv.environment_modifications_for_spec(_spec))
          env_mod.prepend_path(uenv.spack_loaded_hashes_var, _spec.dag_hash())
      # transform to bash commands, and write to file
      cmds = k4_generate_setup_script(env_mod)
      with open(os.path.join(prefix, "setup.sh"), "w") as f:
        f.write(cmds)
        # optionally add a symlink (location configurable via environment variable
        # K4_LATEST_SETUP_PATH. Step will be skipped if it is empty)
        try:
          symlink_path = os.environ.get("ILCSOFT_LATEST_SETUP_PATH", "")
          if symlink_path:
              # make sure that the path exists, create if not
              if not os.path.exists(os.path.dirname(symlink_path)):
                os.makedirs(os.path.dirname(symlink_path))
              # make sure that an existing file will be overwritten,
              # even if it is a symlink (for which 'exists' is false!)
              if os.path.exists(symlink_path) or os.path.islink(symlink_path):
                os.remove(symlink_path)
              os.symlink(os.path.join(prefix, "setup.sh"), symlink_path)
        except:
          tty.warn("Could not create symlink")
