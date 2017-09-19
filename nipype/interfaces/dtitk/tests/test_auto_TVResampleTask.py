# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import TVResampleTask


def test_TVResampleTask_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_arraysz=dict(argstr='-size %s',
    exists=True,
    mandatory=False,
    position=1,
    ),
    in_tensor=dict(argstr='-in %s',
    exists=True,
    mandatory=True,
    position=0,
    ),
    in_voxsz=dict(argstr='-vsize %s',
    exists=True,
    mandatory=False,
    position=2,
    ),
    out_path=dict(argstr='-out %s',
    exists=True,
    mandatory=False,
    name_source='in_volume',
    name_template='%s_resampled.nii.gz',
    position=3,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = TVResampleTask.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_TVResampleTask_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = TVResampleTask.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value