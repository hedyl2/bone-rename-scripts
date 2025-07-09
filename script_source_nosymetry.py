import bpy

def rename_bones():
    rename_map = {
        # Left Arm
        'ValveBiped.Bip01_Clavicle_L'   :   'ValveBiped.Bip01_L_Clavicle',
        'ValveBiped.Bip01_UpperArm_L'   :   'ValveBiped.Bip01_L_UpperArm',
        'ValveBiped.Bip01_Bicep_L'      :   'ValveBiped.Bip01_L_Bicep',
        'ValveBiped.Bip01_Forearm_L'    :   'ValveBiped.Bip01_L_Forearm',
        'ValveBiped.Bip01_Ulna_L'       :   'ValveBiped.Bip01_L_Ulna',
        'ValveBiped.Bip01_Wrist_L'      :   'ValveBiped.Bip01_L_Wrist',
        'ValveBiped.Bip01_Hand_L'       :   'ValveBiped.Bip01_L_Hand',

        # Right Arm
        'ValveBiped.Bip01_Clavicle_R'   :   'ValveBiped.Bip01_R_Clavicle',
        'ValveBiped.Bip01_UpperArm_R'   :   'ValveBiped.Bip01_R_UpperArm',
        'ValveBiped.Bip01_Bicep_R'      :   'ValveBiped.Bip01_R_Bicep',
        'ValveBiped.Bip01_Forearm_R'    :   'ValveBiped.Bip01_R_Forearm',
        'ValveBiped.Bip01_Ulna_R'       :   'ValveBiped.Bip01_R_Ulna',
        'ValveBiped.Bip01_Wrist_R'      :   'ValveBiped.Bip01_R_Wrist',
        'ValveBiped.Bip01_Hand_R'       :   'ValveBiped.Bip01_R_Hand',

        # Left Leg
        'ValveBiped.Bip01_Thigh_L'      :   'ValveBiped.Bip01_L_Thigh',
        'ValveBiped.Bip01_Calf_L'       :   'ValveBiped.Bip01_L_Calf',
        'ValveBiped.Bip01_Knee_L'       :   'ValveBiped.Bip01_L_Knee',
        'ValveBiped.Bip01_Foot_L'       :   'ValveBiped.Bip01_L_Foot',
        'ValveBiped.Bip01_Toe0_L'       :   'ValveBiped.Bip01_L_Toe0',

        # Right Leg
        'ValveBiped.Bip01_Thigh_R'      :   'ValveBiped.Bip01_R_Thigh',
        'ValveBiped.Bip01_Calf_R'       :   'ValveBiped.Bip01_R_Calf',
        'ValveBiped.Bip01_Knee_R'       :   'ValveBiped.Bip01_R_Knee',
        'ValveBiped.Bip01_Foot_R'       :   'ValveBiped.Bip01_R_Foot',
        'ValveBiped.Bip01_Toe0_R'       :   'ValveBiped.Bip01_R_Toe0',

        # Left Fingers
        'ValveBiped.Bip01_Finger0_L'    :   'ValveBiped.Bip01_L_Finger0',
        'ValveBiped.Bip01_Finger01_L'   :   'ValveBiped.Bip01_L_Finger01',
        'ValveBiped.Bip01_Finger02_L'   :   'ValveBiped.Bip01_L_Finger02',
        'ValveBiped.Bip01_Finger1_L'    :   'ValveBiped.Bip01_L_Finger1',
        'ValveBiped.Bip01_Finger11_L'   :   'ValveBiped.Bip01_L_Finger11',
        'ValveBiped.Bip01_Finger12_L'   :   'ValveBiped.Bip01_L_Finger12',
        'ValveBiped.Bip01_Finger2_L'    :   'ValveBiped.Bip01_L_Finger2',
        'ValveBiped.Bip01_Finger21_L'   :   'ValveBiped.Bip01_L_Finger21',
        'ValveBiped.Bip01_Finger22_L'   :   'ValveBiped.Bip01_L_Finger22',
        'ValveBiped.Bip01_Finger3_L'    :   'ValveBiped.Bip01_L_Finger3',
        'ValveBiped.Bip01_Finger31_L'   :   'ValveBiped.Bip01_L_Finger31',
        'ValveBiped.Bip01_Finger32_L'   :   'ValveBiped.Bip01_L_Finger32',
        'ValveBiped.Bip01_Finger4_L'    :   'ValveBiped.Bip01_L_Finger4',
        'ValveBiped.Bip01_Finger41_L'   :   'ValveBiped.Bip01_L_Finger41',
        'ValveBiped.Bip01_Finger42_L'   :   'ValveBiped.Bip01_L_Finger42',

        # Right Fingers
        'ValveBiped.Bip01_Finger0_R'    :   'ValveBiped.Bip01_R_Finger0',
        'ValveBiped.Bip01_Finger01_R'   :   'ValveBiped.Bip01_R_Finger01',
        'ValveBiped.Bip01_Finger02_R'   :   'ValveBiped.Bip01_R_Finger02',
        'ValveBiped.Bip01_Finger1_R'    :   'ValveBiped.Bip01_R_Finger1',
        'ValveBiped.Bip01_Finger11_R'   :   'ValveBiped.Bip01_R_Finger11',
        'ValveBiped.Bip01_Finger12_R'   :   'ValveBiped.Bip01_R_Finger12',
        'ValveBiped.Bip01_Finger2_R'    :   'ValveBiped.Bip01_R_Finger2',
        'ValveBiped.Bip01_Finger21_R'   :   'ValveBiped.Bip01_R_Finger21',
        'ValveBiped.Bip01_Finger22_R'   :   'ValveBiped.Bip01_R_Finger22',
        'ValveBiped.Bip01_Finger3_R'    :   'ValveBiped.Bip01_R_Finger3',
        'ValveBiped.Bip01_Finger31_R'   :   'ValveBiped.Bip01_R_Finger31',
        'ValveBiped.Bip01_Finger32_R'   :   'ValveBiped.Bip01_R_Finger32',
        'ValveBiped.Bip01_Finger4_R'    :   'ValveBiped.Bip01_R_Finger4',
        'ValveBiped.Bip01_Finger41_R'   :   'ValveBiped.Bip01_R_Finger41',
        'ValveBiped.Bip01_Finger42_R'   :   'ValveBiped.Bip01_R_Finger42',
    }

    for b in bpy.context.object.data.bones:
        if b.name in rename_map:
            b.name = rename_map[b.name]

rename_bones()
