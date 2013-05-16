"""
Runs a command
[ssh]
formula = sprinter.formulas.command
hideoutput=true
setup=echo 'setting up...'
update=echo 'updating...'
destroy=echo 'destroying...'
"""

from sprinter.formulastandard import FormulaStandard
from sprinter import lib


class CommandFormula(FormulaStandard):

    def setup(self, feature_name, config):
        self.__run_command('setup', config)
        super(CommandFormula, self).setup(feature_name, config)

    def update(self, feature_name, source_config, target_config):
        self.__run_command('update', target_config)
        super(CommandFormula, self).update(feature_name, source_config, target_config)

    def destroy(self, feature_name, config):
        self.__run_command('destroy', config)
        super(CommandFormula, self).destroy(feature_name, config)

    def activate(self, feature_name, config):
        """ function to run when activating """
        self.__run_command('activate', config)
        super(CommandFormula, self).activate(feature_name, config)

    def deactivate(self, feature_name, config):
        """ tasks to run when deactivating """
        self.__run_command('deactivate', config)
        super(CommandFormula, self).deactivate(feature_name, config)

    def reload(self, feature_name, config):
        """ tasks to call when reloading """
        self.__run_command('reload', config)
        super(CommandFormula, self).reload(feature_name, config)

    def __run_command(self, command_type, config):
        if command_type in config:
            command = config[command_type] % self.environment.context()
            if not 'hideoutput' in config or config['hideoutput'].startswith('t'):
                self.logger.info("Running %s..." % command)
            lib.call(command)