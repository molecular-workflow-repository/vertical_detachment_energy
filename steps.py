from molflow import definitions as df


@df.requires_docker_image('docker.io/avirshup/moldesign-nwchem-0.7.4b1')
def minimize_singlet(mol, nsteps=None):
    import moldesign as mdt
    mol.charge = -1 * mdt.units.q_e
    params = dict(theory='uks',
                  functional='b3lyp',
                  basis='6-31g',
                  charge=-1 * mdt.units.q_e,
                  multiplicity=2)
    mol.set_energy_model(mdt.models.NWChemQM,
                         **params)
    traj = mol.minimize(nsteps=nsteps)
    return {'traj': traj,
            'mol': mol,
            'pdbstring':mol.write(format='pdb')}


@df.requires_docker_image('docker.io/avirshup/moldesign-nwchem-0.7.4b1')
def single_point_singlet(mol):
    import moldesign as mdt
    from moldesign import units as u

    mol.charge = 0 * mdt.units.q_e
    params = dict(theory='rks',
                  functional='b3lyp',
                  basis='6-31g')
    mol.set_energy_model(mdt.models.NWChemQM,
                         **params)
    mol.calculate()
    return {'mol': mol}


@df.requires_docker_image('docker.io/avirshup/moldesign-nwchem-0.7.4b1')
def get_results(singlet, doublet):
    from moldesign import units as u
    vde = singlet.potential_energy - doublet.potential_energy
    vde_json = vde.to(u.eV).to_json()
    vde_json['name'] = 'VDE'
    results = {'vde': (vde).to(u.eV).to_json(),
               'singlet_energy': singlet.potential_energy.to(u.eV).to_json(),
               'doublet_energy': doublet.potential_energy.to(u.eV).to_json(),
               'output_values': [vde_json]}
    return {'results': results}
