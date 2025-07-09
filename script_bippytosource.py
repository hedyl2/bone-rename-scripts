import bpy

def rename_bones():
    
    dict = {
        # Torso
        'bip_pelvis': 'ValveBiped.Bip01_Pelvis',
        'bip_spine_0': 'ValveBiped.Bip01_Spine',
        'bip_spine_1': 'ValveBiped.Bip01_Spine1',
        'bip_spine_2': 'ValveBiped.Bip01_Spine1',
        'bip_spine_3': 'ValveBiped.Bip01_Spine4',
        'bip_neck': 'ValveBiped.Bip01_Neck1',
        'bip_head': 'ValveBiped.Bip01_Head1',
        # Left Arm
        'bip_collar_L': 'ValveBiped.Bip01_L_Clavicle',
        'bip_upperArm_L': 'ValveBiped.Bip01_L_UpperArm',
        'bip_lowerArm_L': 'ValveBiped.Bip01_L_Forearm',
        'handHelperBone_L_jnt': 'ValveBiped.Bip01_L_Ulna',
        'bip_hand_L': 'ValveBiped.Bip01_L_Hand',
        # Right Arm
        'bip_collar_R': 'ValveBiped.Bip01_R_Clavicle',
        'bip_upperArm_R': 'ValveBiped.Bip01_R_UpperArm',
        'bip_lowerArm_R': 'ValveBiped.Bip01_R_Forearm',
        'handHelperBone_R_jnt': 'ValveBiped.Bip01_R_Ulna',
        'bip_hand_R': 'ValveBiped.Bip01_R_Hand',
        # Left Leg
        'bip_hip_L': 'ValveBiped.Bip01_L_Thigh',
        'bip_knee_L': 'ValveBiped.Bip01_L_Calf',
        'bip_foot_L': 'ValveBiped.Bip01_L_Foot',
        'bip_toe_L': 'ValveBiped.Bip01_L_Toe0',
        # Right Leg
        'RightUpLeg': 'ValveBiped.Bip01_R_Thigh',
        'RightLeg': 'ValveBiped.Bip01_R_Calf',
        'RightFoot': 'ValveBiped.Bip01_R_Foot',
        'RightToeBase': 'ValveBiped.Bip01_R_Toe0',
        # Left Fingers
        'bip_thumb_0_L': 'ValveBiped.Bip01_L_Finger0',
        'bip_thumb_1_L': 'ValveBiped.Bip01_L_Finger01',
        'bip_thumb_2_L': 'ValveBiped.Bip01_L_Finger02',
        'bip_index_0_L': 'ValveBiped.Bip01_L_Finger1',
        'bip_index_1_L': 'ValveBiped.Bip01_L_Finger11',
        'bip_index_2_L': 'ValveBiped.Bip01_L_Finger12',
        'bip_middle_0_L': 'ValveBiped.Bip01_L_Finger2',
        'bip_middle_1_L': 'ValveBiped.Bip01_L_Finger21',
        'bip_middle_2_L': 'ValveBiped.Bip01_L_Finger22',
        'bip_Ling_0_L': 'ValveBiped.Bip01_L_Finger3',
        'bip_Ling_1_L': 'ValveBiped.Bip01_L_Finger31',
        'bip_Ling_2_L': 'ValveBiped.Bip01_L_Finger32',
        'bip_pinky_0_L': 'ValveBiped.Bip01_L_Finger4',
        'bip_pinky_1_L': 'ValveBiped.Bip01_L_Finger41',
        'bip_pinky_2_L': 'ValveBiped.Bip01_L_Finger42',
        # Right Fingers
        'bip_thumb_0_R': 'ValveBiped.Bip01_R_Finger0',
        'bip_thumb_1_R': 'ValveBiped.Bip01_R_Finger01',
        'bip_thumb_2_R': 'ValveBiped.Bip01_R_Finger02',
        'bip_index_0_R': 'ValveBiped.Bip01_R_Finger1',
        'bip_index_1_R': 'ValveBiped.Bip01_R_Finger11',
        'bip_index_2_R': 'ValveBiped.Bip01_R_Finger12',
        'bip_middle_0_R': 'ValveBiped.Bip01_R_Finger2',
        'bip_middle_1_R': 'ValveBiped.Bip01_R_Finger21',
        'bip_middle_2_R': 'ValveBiped.Bip01_R_Finger22',
        'bip_ring_0_R': 'ValveBiped.Bip01_R_Finger3',
        'bip_ring_1_R': 'ValveBiped.Bip01_R_Finger31',
        'bip_ring_2_R': 'ValveBiped.Bip01_R_Finger32',
        'bip_pinky_0_R': 'ValveBiped.Bip01_R_Finger4',
        'bip_pinky_1_R': 'ValveBiped.Bip01_R_Finger41',
        'bip_pinky_2_R': 'ValveBiped.Bip01_R_Finger42'

    }
    
    for b in bpy.context.object.data.bones:
        if b.name in dict.keys():
            b.name = dict[b.name]

rename_bones()