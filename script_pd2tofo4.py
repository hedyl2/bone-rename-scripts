import bpy

def rename_bones():
    
    dict = {
        # Torso
        'Hips': 'ValveBiped.Bip01_Pelvis',
        'Spine': 'ValveBiped.Bip01_Spine',
        'Spine1': 'ValveBiped.Bip01_Spine2',
        'Spine2': 'ValveBiped.Bip01_Spine4',
        'Neck': 'ValveBiped.Bip01_Neck1',
        'Head': 'ValveBiped.Bip01_Head1',
        # Left Leg
        'LeftUpLeg': 'ValveBiped.Bip01_L_Thigh',
        'LeftLeg': 'ValveBiped.Bip01_L_Calf',
        'LeftFoot': 'ValveBiped.Bip01_L_Foot',
        'LeftToeBase': 'ValveBiped.Bip01_L_Toe0',
        # Right Leg
        'RightUpLeg': 'ValveBiped.Bip01_R_Thigh',
        'RightLeg': 'ValveBiped.Bip01_R_Calf',
        'RightFoot': 'ValveBiped.Bip01_R_Foot',
        'RightToeBase': 'ValveBiped.Bip01_R_Toe0',
        # Left Arm
        'LeftShoulder': 'Arm_Collarbone_skin.L',
        'LeftArm': 'Arm_UpperTwist2_skin.L',
        'LeftForeArm': 'Arm_ForeArm1_skin.L',
        'LeftForeArmRoll': 'Arm_ForeArm3_skin.L',
        'LeftHand': 'Arm_Hand.L',
        # Right Arm
        'RightShoulder': 'Arm_Collarbone_skin.R',
        'RightArm': 'Arm_UpperTwist2_skin.R',
        'RightForeArm': 'Arm_ForeArm1_skin.R',
        'RightForeArmRoll': 'Arm_ForeArm3_skin.R',
        'RightHand': 'Arm_Hand.R',
        # Left Fingers
        'LeftHandThumb1': 'Arm_Finger11.L',
        'LeftHandThumb2': 'Arm_Finger12.L',
        'LeftHandThumb3': 'Arm_Finger13.L',
        'LeftHandIndex1': 'Arm_Finger21.L',
        'LeftHandIndex2': 'Arm_Finger22.L',
        'LeftHandIndex3': 'Arm_Finger23.L',
        'LeftHandMiddle1': 'Arm_Finger31.L',
        'LeftHandMiddle2': 'Arm_Finger32.L',
        'LeftHandMiddle3': 'Arm_Finger33.L',
        'LeftHandRing1': 'Arm_Finger41.L',
        'LeftHandRing2': 'Arm_Finger42.L',
        'LeftHandRing3': 'Arm_Finger43.L',
        'LeftHandPinky1': 'Arm_Finger51.L',
        'LeftHandPinky2': 'Arm_Finger52.L',
        'LeftHandPinky3': 'Arm_Finger53.L',
        # Right Fingers
        'RightHandThumb1': 'Arm_Finger11.R',
        'RightHandThumb2': 'Arm_Finger12.R',
        'RightHandThumb3': 'Arm_Finger13.R',
        'RightHandIndex1': 'Arm_Finger21.R',
        'RightHandIndex2': 'Arm_Finger22.R',
        'RightHandIndex3': 'Arm_Finger23.R',
        'RightHandMiddle1': 'Arm_Finger31.R',
        'RightHandMiddle2': 'Arm_Finger32.R',
        'RightHandMiddle3': 'Arm_Finger33.R',
        'RightHandRing1': 'Arm_Finger41.R',
        'RightHandRing2': 'Arm_Finger42.R',
        'RightHandRing3': 'Arm_Finger43.R',
        'RightHandPinky1': 'Arm_Finger51.R',
        'RightHandPinky2': 'Arm_Finger52.R',
        'RightHandPinky3': 'Arm_Finger53.R'

    }
    
    for b in bpy.context.object.data.bones:
        if b.name in dict.keys():
            b.name = dict[b.name]

rename_bones()