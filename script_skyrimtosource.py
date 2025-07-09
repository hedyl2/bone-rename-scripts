import bpy

def rename_bones():
    
    dict = {
        # Torso
        'NPC Pelvis': 'ValveBiped.Bip01_Pelvis',
        'NPC Spine': 'ValveBiped.Bip01_Spine',
        'NPC Spine1': 'ValveBiped.Bip01_Spine2',
        'NPC Spine2': 'ValveBiped.Bip01_Spine4',
        'NPC Head': 'ValveBiped.Bip01_Head1',
        # Left Arm
        'NPC Clavicle.L': 'ValveBiped.Bip01_L_Clavicle',
        'NPC UpperArm.L': 'ValveBiped.Bip01_L_UpperArm',
        'NPC L Forearm [LLar]': 'ValveBiped.Bip01_L_Forearm',
        'NPC L Hand [LHnd]': 'ValveBiped.Bip01_L_Hand',
        # Right Arm
        'NPC R Clavicle [RClv]': 'ValveBiped.Bip01_R_Clavicle',
        'NPC R UpperArm [RUar]': 'ValveBiped.Bip01_R_UpperArm',
        'CME R Forearm [RLar]': 'ValveBiped.Bip01_R_Forearm',
        'NPC R Hand [RHnd]': 'ValveBiped.Bip01_R_Hand',
        # Left Leg
        'NPC L Thigh [LThg]': 'ValveBiped.Bip01_L_Thigh',
        'NPC L Calf [LClf]': 'ValveBiped.Bip01_L_Calf',
        'NPC L Foot [Lft ]': 'ValveBiped.Bip01_L_Foot',
        'NPC L Toe0 [LToe]': 'ValveBiped.Bip01_L_Toe0',
        # Right Leg
        'NPC R Thigh [RThg]': 'ValveBiped.Bip01_R_Thigh',
        'NPC R Calf [RClf]': 'ValveBiped.Bip01_R_Calf',
        'NPC R Foot [Rft ]': 'ValveBiped.Bip01_R_Foot',
        'NPC R Toe0 [RToe]': 'ValveBiped.Bip01_R_Toe0',
        # Left Fingers
        'NPC L Finger00 [LF00]': 'ValveBiped.Bip01_L_Finger0',
        'NPC L Finger01 [LF01]': 'ValveBiped.Bip01_L_Finger01',
        'NPC L Finger02 [LF02]': 'ValveBiped.Bip01_L_Finger02',
        'NPC L Finger10 [LF10]': 'ValveBiped.Bip01_L_Finger1',
        'NPC L Finger11 [LF11]': 'ValveBiped.Bip01_L_Finger11',
        'NPC L Finger12 [LF12]': 'ValveBiped.Bip01_L_Finger12',
        'NPC L Finger20 [LF20]': 'ValveBiped.Bip01_L_Finger2',
        'NPC L Finger21 [LF21]': 'ValveBiped.Bip01_L_Finger21',
        'NPC L Finger22 [LF22]': 'ValveBiped.Bip01_L_Finger22',
        'NPC L Finger30 [LF30]': 'ValveBiped.Bip01_L_Finger3',
        'NPC L Finger31 [LF31]': 'ValveBiped.Bip01_L_Finger31',
        'NPC L Finger32 [LF32]': 'ValveBiped.Bip01_L_Finger32',
        'NPC L Finger40 [LF40]': 'ValveBiped.Bip01_L_Finger4',
        'NPC L Finger41 [LF41]': 'ValveBiped.Bip01_L_Finger41',
        'NPC L Finger42 [LF42]': 'ValveBiped.Bip01_L_Finger42',
        # Right Fingers
        'NPC R Finger00 [RF00]': 'ValveBiped.Bip01_R_Finger0',
        'NPC R Finger01 [RF01]': 'ValveBiped.Bip01_R_Finger01',
        'NPC R Finger02 [RF02]': 'ValveBiped.Bip01_R_Finger02',
        'NPC R Finger10 [RF10]': 'ValveBiped.Bip01_R_Finger1',
        'NPC R Finger11 [RF11]': 'ValveBiped.Bip01_R_Finger11',
        'NPC R Finger12 [RF12]': 'ValveBiped.Bip01_R_Finger12',
        'NPC R Finger20 [RF20]': 'ValveBiped.Bip01_R_Finger2',
        'NPC R Finger21 [RF21]': 'ValveBiped.Bip01_R_Finger21',
        'NPC R Finger22 [RF22]': 'ValveBiped.Bip01_R_Finger22',
        'NPC R Finger30 [RF30]': 'ValveBiped.Bip01_R_Finger3',
        'NPC R Finger31 [RF31]': 'ValveBiped.Bip01_R_Finger31',
        'NPC R Finger32 [RF32]': 'ValveBiped.Bip01_R_Finger32',
        'NPC R Finger40 [RF40]': 'ValveBiped.Bip01_R_Finger4',
        'NPC R Finger41 [RF41]': 'ValveBiped.Bip01_R_Finger41',
        'NPC R Finger42 [RF42]': 'ValveBiped.Bip01_R_Finger42',
        #Helpers
        'NPC L UpperarmTwist1 [LUt1]': 'ValveBiped.hlp_l_uppertwist1',
        'NPC L UpperarmTwist2 [LUt2]': 'ValveBiped.hlp_l_uppertwist2',
        'NPC L ForearmTwist1 [LLt1]': 'ValveBiped.hlp_l_ulnatwist1',
        'NPC L ForearmTwist2 [LLt2]': 'ValveBiped.hlp_l_ulnatwist2',
        
        'NPC R UpperarmTwist1 [RUt1]': 'ValveBiped.hlp_r_uppertwist1',
        'NPC R UpperarmTwist2 [RUt2]': 'ValveBiped.hlp_r_uppertwist2',
        'NPC R ForearmTwist1 [RLt1]': 'ValveBiped.hlp_r_ulnatwist1',
        'NPC R ForearmTwist2 [RLt2]': 'ValveBiped.hlp_r_ulnatwist2',
    }
    
    for b in bpy.context.object.data.bones:
        if b.name in dict.keys():
            b.name = dict[b.name]

rename_bones()