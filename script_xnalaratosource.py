import bpy

def rename_bones():
    
    dict = {
        # Torso
        'pelvis': 'ValveBiped.Bip01_Pelvis',
        'spine lower': 'ValveBiped.Bip01_Spine',
            # There is no equivalent of Bip01_Spine1, you will have to make it
        'spine middle': 'ValveBiped.Bip01_Spine2',
        'spine upper': 'ValveBiped.Bip01_Spine4',
        'head neck lower': 'ValveBiped.Bip01_Neck1',
        'head neck upper': 'ValveBiped.Bip01_Head1',
        # Left Arm
        'arm left shoulder 1': 'ValveBiped.Bip01_L_Clavicle',
        'arm left shoulder 2': 'ValveBiped.Bip01_L_UpperArm',
        'arm left elbow': 'ValveBiped.Bip01_L_Forearm',
        'arm left wrist ctr': 'ValveBiped.Bip01_L_Ulna',
        'arm left wrist': 'ValveBiped.Bip01_L_Hand',
        # Right Arm
        'arm right shoulder 1': 'ValveBiped.Bip01_R_Clavicle',
        'arm right shoulder 2': 'ValveBiped.Bip01_R_UpperArm',
        'arm right elbow': 'ValveBiped.Bip01_R_Forearm',
        'arm right wrist ctr': 'ValveBiped.Bip01_R_Ulna',
        'arm right wrist': 'ValveBiped.Bip01_R_Hand',
        # Left Leg
        'leg left thigh ctr': 'ValveBiped.Bip01_L_Gluteus',
        'leg left thigh': 'ValveBiped.Bip01_L_Thigh',
        'leg left knee ctr': 'ValveBiped.Bip01_L_Knee',
        'leg left knee': 'ValveBiped.Bip01_L_Calf',
        'leg left ankle': 'ValveBiped.Bip01_L_Foot',
        'leg left toe': 'ValveBiped.Bip01_L_Toe0',
        # Right Leg
        'leg right thigh ctr': 'ValveBiped.Bip01_R_Gluteus',
        'leg right thigh': 'ValveBiped.Bip01_R_Thigh',
        'leg right knee ctr': 'ValveBiped.Bip01_R_Knee',
        'leg right knee': 'ValveBiped.Bip01_R_Calf',
        'leg right ankle': 'ValveBiped.Bip01_R_Foot',
        'leg right toe': 'ValveBiped.Bip01_R_Toe0',
        # Left Fingers
        'arm left finger 1 a': 'ValveBiped.Bip01_L_Finger0',
        'arm left finger 1 b': 'ValveBiped.Bip01_L_Finger01',
        'arm left finger 1 c': 'ValveBiped.Bip01_L_Finger02',
        'arm left finger 2 a': 'ValveBiped.Bip01_L_Finger1',
        'arm left finger 2 b': 'ValveBiped.Bip01_L_Finger11',
        'arm left finger 2 c': 'ValveBiped.Bip01_L_Finger12',
        'arm left finger 3 a': 'ValveBiped.Bip01_L_Finger2',
        'arm left finger 3 b': 'ValveBiped.Bip01_L_Finger21',
        'arm left finger 3 c': 'ValveBiped.Bip01_L_Finger22',
        'arm left finger 4 a': 'ValveBiped.Bip01_L_Finger3',
        'arm left finger 4 b': 'ValveBiped.Bip01_L_Finger31',
        'arm left finger 4 c': 'ValveBiped.Bip01_L_Finger32',
        'arm left finger 5 a': 'ValveBiped.Bip01_L_Finger4',
        'arm left finger 5 b': 'ValveBiped.Bip01_L_Finger41',
        'arm left finger 5 c': 'ValveBiped.Bip01_L_Finger42',
        # Right Fingers
        'arm right finger 1 a': 'ValveBiped.Bip01_R_Finger0',
        'arm right finger 1 b': 'ValveBiped.Bip01_R_Finger01',
        'arm right finger 1 c': 'ValveBiped.Bip01_R_Finger02',
        'arm right finger 2 a': 'ValveBiped.Bip01_R_Finger1',
        'arm right finger 2 b': 'ValveBiped.Bip01_R_Finger11',
        'arm right finger 2 c': 'ValveBiped.Bip01_R_Finger12',
        'arm right finger 3 a': 'ValveBiped.Bip01_R_Finger2',
        'arm right finger 3 b': 'ValveBiped.Bip01_R_Finger21',
        'arm right finger 3 c': 'ValveBiped.Bip01_R_Finger22',
        'arm right finger 4 a': 'ValveBiped.Bip01_R_Finger3',
        'arm right finger 4 b': 'ValveBiped.Bip01_R_Finger31',
        'arm right finger 4 c': 'ValveBiped.Bip01_R_Finger32',
        'arm right finger 5 a': 'ValveBiped.Bip01_R_Finger4',
        'arm right finger 5 b': 'ValveBiped.Bip01_R_Finger41',
        'arm right finger 5 c': 'ValveBiped.Bip01_R_Finger42',
        # Left Fingers
        'arm left finger 1a': 'ValveBiped.Bip01_L_Finger0',
        'arm left finger 1b': 'ValveBiped.Bip01_L_Finger01',
        'arm left finger 1c': 'ValveBiped.Bip01_L_Finger02',
        'arm left finger 2a': 'ValveBiped.Bip01_L_Finger1',
        'arm left finger 2b': 'ValveBiped.Bip01_L_Finger11',
        'arm left finger 2c': 'ValveBiped.Bip01_L_Finger12',
        'arm left finger 3a': 'ValveBiped.Bip01_L_Finger2',
        'arm left finger 3b': 'ValveBiped.Bip01_L_Finger21',
        'arm left finger 3c': 'ValveBiped.Bip01_L_Finger22',
        'arm left finger 4a': 'ValveBiped.Bip01_L_Finger3',
        'arm left finger 4b': 'ValveBiped.Bip01_L_Finger31',
        'arm left finger 4c': 'ValveBiped.Bip01_L_Finger32',
        'arm left finger 5a': 'ValveBiped.Bip01_L_Finger4',
        'arm left finger 5b': 'ValveBiped.Bip01_L_Finger41',
        'arm left finger 5c': 'ValveBiped.Bip01_L_Finger42',
        # Right Fingers
        'arm right finger 1a': 'ValveBiped.Bip01_R_Finger0',
        'arm right finger 1b': 'ValveBiped.Bip01_R_Finger01',
        'arm right finger 1c': 'ValveBiped.Bip01_R_Finger02',
        'arm right finger 2a': 'ValveBiped.Bip01_R_Finger1',
        'arm right finger 2b': 'ValveBiped.Bip01_R_Finger11',
        'arm right finger 2c': 'ValveBiped.Bip01_R_Finger12',
        'arm right finger 3a': 'ValveBiped.Bip01_R_Finger2',
        'arm right finger 3b': 'ValveBiped.Bip01_R_Finger21',
        'arm right finger 3c': 'ValveBiped.Bip01_R_Finger22',
        'arm right finger 4a': 'ValveBiped.Bip01_R_Finger3',
        'arm right finger 4b': 'ValveBiped.Bip01_R_Finger31',
        'arm right finger 4c': 'ValveBiped.Bip01_R_Finger32',
        'arm right finger 5a': 'ValveBiped.Bip01_R_Finger4',
        'arm right finger 5b': 'ValveBiped.Bip01_R_Finger41',
        'arm right finger 5c': 'ValveBiped.Bip01_R_Finger42',


    }
    
    for b in bpy.context.object.data.bones:
        if b.name in dict.keys():
            b.name = dict[b.name]

rename_bones()