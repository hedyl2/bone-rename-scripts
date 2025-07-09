import bpy

def rename_bones():
    
    dict = {
        # Torso
        'Hips': 'ValveBiped.Bip01_Pelvis',
        'Spine': 'ValveBiped.Bip01_Spine',
        'Spine1': 'ValveBiped.Bip01_Spine1',
        'Spine2': 'ValveBiped.Bip01_Spine2',
        'Spine3': 'ValveBiped.Bip01_Spine4',
        'Neck1': 'ValveBiped.Bip01_Neck1',
        'Head': 'ValveBiped.Bip01_Head1',
        # Left Arm
        'LeftShoulder': 'ValveBiped.Bip01_L_Clavicle',
        'LeftArmTwist1': 'ValveBiped.Bip01_L_UpperArm',
        'LeftArmTwist2': 'ValveBiped.Bip01_Bicep_L',
        'LeftForeArm': 'ValveBiped.Bip01_L_Forearm',
        'LeftForeArmTwist2': 'ValveBiped.Bip01_Ulna_L',
        'LeftForeArmTwist1': 'ValveBiped.Bip01_Ulna_2_L',
        'LeftHand': 'ValveBiped.Bip01_L_Hand',
        # Right Arm
        'RightShoulder': 'ValveBiped.Bip01_R_Clavicle',
        'RightArmTwist1': 'ValveBiped.Bip01_R_UpperArm',
        'RightArmTwist2': 'ValveBiped.Bip01_Bicep_R',
        'RightForeArm': 'ValveBiped.Bip01_R_Forearm',
        'RightForeArmTwist2': 'ValveBiped.Bip01_Ulna_R',
        'RightForeArmTwist1': 'ValveBiped.Bip01_Ulna_2_R',
        'RightHand': 'ValveBiped.Bip01_R_Hand',
        # Left Leg
        'LeftUpLegTwist1': 'ValveBiped.Bip01_L_Thigh',
        'LeftUpLegTwist2': 'ValveBiped.Bip01_L_Quadricep',
        'LeftLegTwist2': 'ValveBiped.Bip01_L_Calf',
        'LeftFoot': 'ValveBiped.Bip01_L_Foot',
        'LeftToeBase': 'ValveBiped.Bip01_L_Toe0',
        'LeftKneePatella': 'ValveBiped.Bip01_L_Knee',
        # Right Leg
        'RightUpLegTwist1': 'ValveBiped.Bip01_R_Thigh',
        'RightUpLegTwist2': 'ValveBiped.Bip01_R_Quadricep',
        'RightLegTwist2': 'ValveBiped.Bip01_R_Calf',
        'RightFoot': 'ValveBiped.Bip01_R_Foot',
        'RightToeBase': 'ValveBiped.Bip01_R_Toe0',
        'RightKneePatella': 'ValveBiped.Bip01_R_Knee',
        # Left Fingers
        'LeftHandThumb1': 'ValveBiped.Bip01_L_Finger0',
        'LeftHandThumb2': 'ValveBiped.Bip01_L_Finger01',
        'LeftHandThumb3': 'ValveBiped.Bip01_L_Finger02',
        'LeftHandIndex1': 'ValveBiped.Bip01_L_Finger1',
        'LeftHandIndex2': 'ValveBiped.Bip01_L_Finger11',
        'LeftHandIndex3': 'ValveBiped.Bip01_L_Finger12',
        'LeftHandMiddle1': 'ValveBiped.Bip01_L_Finger2',
        'LeftHandMiddle2': 'ValveBiped.Bip01_L_Finger21',
        'LeftHandMiddle3': 'ValveBiped.Bip01_L_Finger22',
        'LeftHandRing1': 'ValveBiped.Bip01_L_Finger3',
        'LeftHandRing2': 'ValveBiped.Bip01_L_Finger31',
        'LeftHandRing3': 'ValveBiped.Bip01_L_Finger32',
        'LeftHandPinky1': 'ValveBiped.Bip01_L_Finger4',
        'LeftHandPinky2': 'ValveBiped.Bip01_L_Finger41',
        'LeftHandPinky3': 'ValveBiped.Bip01_L_Finger42',
        # Right Fingers
        'RightHandThumb1': 'ValveBiped.Bip01_R_Finger0',
        'RightHandThumb2': 'ValveBiped.Bip01_R_Finger01',
        'RightHandThumb3': 'ValveBiped.Bip01_R_Finger02',
        'RightHandIndex1': 'ValveBiped.Bip01_R_Finger1',
        'RightHandIndex2': 'ValveBiped.Bip01_R_Finger11',
        'RightHandIndex3': 'ValveBiped.Bip01_R_Finger12',
        'RightHandMiddle1': 'ValveBiped.Bip01_R_Finger2',
        'RightHandMiddle2': 'ValveBiped.Bip01_R_Finger21',
        'RightHandMiddle3': 'ValveBiped.Bip01_R_Finger22',
        'RightHandRing1': 'ValveBiped.Bip01_R_Finger3',
        'RightHandRing2': 'ValveBiped.Bip01_R_Finger31',
        'RightHandRing3': 'ValveBiped.Bip01_R_Finger32',
        'RightHandPinky1': 'ValveBiped.Bip01_R_Finger4',
        'RightHandPinky2': 'ValveBiped.Bip01_R_Finger41',
        'RightHandPinky3': 'ValveBiped.Bip01_R_Finger42'

    }
    
    for b in bpy.context.object.data.bones:
        if b.name in dict.keys():
            b.name = dict[b.name]

rename_bones()