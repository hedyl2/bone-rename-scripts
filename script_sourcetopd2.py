import bpy

def rename_bones():
    
    dict = {
        # Torso
        'ValveBiped.Bip01_Pelvis': 'Hips',
        'ValveBiped.Bip01_Spine': 'Spine',
        'ValveBiped.Bip01_Spine2': 'Spine1',
        'ValveBiped.Bip01_Spine4': 'Spine2',
        'ValveBiped.Bip01_Neck1': 'Neck',
        'ValveBiped.Bip01_Head1': 'Head',
        # Left Arm
        'ValveBiped.Bip01_L_Clavicle': 'LeftShoulder',
        'ValveBiped.Bip01_L_UpperArm': 'LeftArm',
        'ValveBiped.Bip01_L_Forearm': 'LeftForeArm',
        'ValveBiped.Bip01_L_Ulna': 'LeftForeArmRoll',
        'ValveBiped.Bip01_L_Hand': 'LeftHand',
        # Right Arm
        'ValveBiped.Bip01_R_Clavicle': 'RightShoulder',
        'ValveBiped.Bip01_R_UpperArm': 'RightArm',
        'ValveBiped.Bip01_R_Forearm': 'RightForeArm',
        'ValveBiped.Bip01_R_Ulna': 'RightForeArmRoll',
        'ValveBiped.Bip01_R_Hand': 'RightHand',
        # Left Leg
        'ValveBiped.Bip01_L_Thigh': 'LeftUpLeg',
        'ValveBiped.Bip01_L_Calf': 'LeftLeg',
        'ValveBiped.Bip01_L_Foot': 'LeftFoot',
        'ValveBiped.Bip01_L_Toe0': 'LeftToeBase',
        # Right Leg
        'ValveBiped.Bip01_R_Thigh': 'RightUpLeg',
        'ValveBiped.Bip01_R_Calf': 'RightLeg',
        'ValveBiped.Bip01_R_Foot': 'RightFoot',
        'ValveBiped.Bip01_R_Toe0': 'RightToeBase',
        # Left Fingers
        'ValveBiped.Bip01_L_Finger0': 'LeftHandThumb1',
        'ValveBiped.Bip01_L_Finger01': 'LeftHandThumb2',
        'ValveBiped.Bip01_L_Finger02': 'LeftHandThumb3',
        'ValveBiped.Bip01_L_Finger1': 'LeftHandIndex1',
        'ValveBiped.Bip01_L_Finger11': 'LeftHandIndex2',
        'ValveBiped.Bip01_L_Finger12': 'LeftHandIndex3',
        'ValveBiped.Bip01_L_Finger2': 'LeftHandMiddle1',
        'ValveBiped.Bip01_L_Finger21': 'LeftHandMiddle2',
        'ValveBiped.Bip01_L_Finger22': 'LeftHandMiddle3',
        'ValveBiped.Bip01_L_Finger3': 'LeftHandRing1',
        'ValveBiped.Bip01_L_Finger31': 'LeftHandRing2',
        'ValveBiped.Bip01_L_Finger32': 'LeftHandRing3',
        'ValveBiped.Bip01_L_Finger4': 'LeftHandPinky1',
        'ValveBiped.Bip01_L_Finger41': 'LeftHandPinky2',
        'ValveBiped.Bip01_L_Finger42': 'LeftHandPinky3',
        # Right Fingers
        'ValveBiped.Bip01_R_Finger0': 'RightHandThumb1',
        'ValveBiped.Bip01_R_Finger01': 'RightHandThumb2',
        'ValveBiped.Bip01_R_Finger02': 'RightHandThumb3',
        'ValveBiped.Bip01_R_Finger1': 'RightHandIndex1',
        'ValveBiped.Bip01_R_Finger11': 'RightHandIndex2',
        'ValveBiped.Bip01_R_Finger12': 'RightHandIndex3',
        'ValveBiped.Bip01_R_Finger2': 'RightHandMiddle1',
        'ValveBiped.Bip01_R_Finger21': 'RightHandMiddle2',
        'ValveBiped.Bip01_R_Finger22': 'RightHandMiddle3',
        'ValveBiped.Bip01_R_Finger3': 'RightHandRing1',
        'ValveBiped.Bip01_R_Finger31': 'RightHandRing2',
        'ValveBiped.Bip01_R_Finger32': 'RightHandRing3',
        'ValveBiped.Bip01_R_Finger4': 'RightHandPinky1',
        'ValveBiped.Bip01_R_Finger41': 'RightHandPinky2',
        'ValveBiped.Bip01_R_Finger42': 'RightHandPinky3'

    }
    
    for b in bpy.context.object.data.bones:
        if b.name in dict.keys():
            b.name = dict[b.name]

rename_bones()