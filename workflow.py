from molflow import definitions as df


workflow = df.Workflow(name='vertical_detachment_energy')

class VerticalDetachmentEnergy(df.Workflow):
    name = 'vertical_detachment_energy'

    inputs = {'mol': df.WorkflowInput(type=df.SMALL_MOLECULE_INPUT_TYPES,
                                      description='Small molecule input (<50 atoms)'),
              'charge': df.WorkflowInput(type=int,
                                         description='Molecular charge in closed-shell state')}

    def define_workflow(self):
        molecule = self.convert()


workflow.add_input('molecule',
                   type=df.SMALL_MOLECULE_INPUT_TYPES,
                   description='Input molecule in a supported format')
workflow.add_input('charge',
                   type='int',
                   description='Molecular charge in the initial (closed-shell) state',
                   default=0)





