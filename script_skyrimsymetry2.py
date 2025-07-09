import bpy

def rename_bones():
    rename_dict = {
        # Torso
        'NPC Pelvis': 'NPC Pelvis',
        'NPC Spine': 'NPC Spine',
        'NPC Spine1': 'NPC Spine1',
        'NPC Spine2': 'NPC Spine2',
        'NPC Neck': 'NPC Neck',
        'NPC Head': 'NPC Head',
        # Left Arm
        'NPC L Clavicle': 'NPC Clavicle.L',
        'NPC L UpperArm': 'NPC UpperArm.L',
        'NPC L Forearm': 'NPC Forearm.L',
        'NPC L Hand': 'NPC Hand.L',
        # Right Arm
        'NPC R Clavicle': 'NPC Clavicle.R',
        'NPC R UpperArm': 'NPC UpperArm.R',
        'NPC R Forearm': 'NPC Forearm.R',
        'NPC R Hand': 'NPC Hand.R',
        # Left Leg
        'NPC L Thigh': 'NPC Thigh.L',
        'NPC L Calf': 'NPC Calf.L',
        'NPC L Foot': 'NPC Foot.L',
        'NPC L Toe0': 'NPC Toe0.L',
        # Right Leg
        'NPC R Thigh': 'NPC Thigh.R',
        'NPC R Calf': 'NPC Calf.R',
        'NPC R Foot': 'NPC Foot.R',
        'NPC R Toe0': 'NPC Toe0.R',
        # Left Fingers
        'NPC L Finger00': 'NPC Finger00.L',
        'NPC L Finger01': 'NPC Finger01.L',
        'NPC L Finger02': 'NPC Finger02.L',
        'NPC L Finger10': 'NPC Finger10.L',
        'NPC L Finger11': 'NPC Finger11.L',
        'NPC L Finger12': 'NPC Finger12.L',
        'NPC L Finger20': 'NPC Finger20.L',
        'NPC L Finger21': 'NPC Finger21.L',
        'NPC L Finger22': 'NPC Finger22.L',
        'NPC L Finger30': 'NPC Finger30.L',
        'NPC L Finger31': 'NPC Finger31.L',
        'NPC L Finger32': 'NPC Finger32.L',
        'NPC L Finger40': 'NPC Finger40.L',
        'NPC L Finger41': 'NPC Finger41.L',
        'NPC L Finger42': 'NPC Finger42.L',
        # Right Fingers
        'NPC R Finger00': 'NPC Finger00.R',
        'NPC R Finger01': 'NPC Finger01.R',
        'NPC R Finger02': 'NPC Finger02.R',
        'NPC R Finger10': 'NPC Finger10.R',
        'NPC R Finger11': 'NPC Finger11.R',
        'NPC R Finger12': 'NPC Finger12.R',
        'NPC R Finger20': 'NPC Finger20.R',
        'NPC R Finger21': 'NPC Finger21.R',
        'NPC R Finger22': 'NPC Finger22.R',
        'NPC R Finger30': 'NPC Finger30.R',
        'NPC R Finger31': 'NPC Finger31.R',
        'NPC R Finger32': 'NPC Finger32.R',
        'NPC R Finger40': 'NPC Finger40.R',
        'NPC R Finger41': 'NPC Finger41.R',
        'NPC R Finger42': 'NPC Finger42.R',
        # Helpers
        'NPC L UpperarmTwist1': 'NPC UpperarmTwist1.L',
        'NPC L UpperarmTwist2': 'NPC UpperarmTwist2.L',
        'NPC L ForearmTwist1': 'NPC ForearmTwist1.L',
        'NPC L ForearmTwist2': 'NPC ForearmTwist2.L',
        'NPC R UpperarmTwist1': 'NPC UpperarmTwist1.R',
        'NPC R UpperarmTwist2': 'NPC UpperarmTwist2.R',
        'NPC R ForearmTwist1': 'NPC ForearmTwist1.R',
        'NPC R ForearmTwist2': 'NPC ForearmTwist2.R',
    }
    
    for b in bpy.context.object.data.bones:
        if b.name in rename_dict:
            b.name = rename_dict[b.name]

rename_bones()