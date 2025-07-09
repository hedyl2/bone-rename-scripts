import bpy

def rename_bones():
    
    dict = {
        # Torso
        'b__Pelvis__': 'ValveBiped.Bip01_Pelvis',
        'b__Spine0__': 'ValveBiped.Bip01_Spine',
        'b__Spine1__': 'ValveBiped.Bip01_Spine2',
        'b__Spine2__': 'ValveBiped.Bip01_Spine4',
        'b__Neck__': 'ValveBiped.Bip01_Neck1',
        'b__Head__': 'ValveBiped.Bip01_Head1',
        # Left Arm
        'b__L_Clavicle__': 'ValveBiped.Bip01_L_Clavicle',
        'b__L_UpperArm__': 'ValveBiped.Bip01_L_UpperArm',
        'b__L_Forearm__': 'ValveBiped.Bip01_L_Forearm',
        'b__L_ForearmTwist__': 'ValveBiped.Bip01_L_Ulna',
        'b__L_Hand__': 'ValveBiped.Bip01_L_Hand',
        # Right Arm
        'b__R_Clavicle__': 'ValveBiped.Bip01_R_Clavicle',
        'b__R_UpperArm__': 'ValveBiped.Bip01_R_UpperArm',
        'b__R_Forearm__': 'ValveBiped.Bip01_R_Forearm',
        'b__R_ForearmTwist__': 'ValveBiped.Bip01_R_Ulna',
        'b__R_Hand__': 'ValveBiped.Bip01_R_Hand',
        # Left Leg
        'b__L_Thigh__': 'ValveBiped.Bip01_L_Thigh',
        'b__L_Calf__': 'ValveBiped.Bip01_L_Calf',
        'b__L_Foot__': 'ValveBiped.Bip01_L_Foot',
        'b__L_Toe__': 'ValveBiped.Bip01_L_Toe0',
        # Right Leg
        'b__R_Thigh__': 'ValveBiped.Bip01_R_Thigh',
        'b__R_Calf__': 'ValveBiped.Bip01_R_Calf',
        'b__R_Foot__': 'ValveBiped.Bip01_R_Foot',
        'b__R_Toe__': 'ValveBiped.Bip01_R_Toe0',
        # Left Fingers
        'b__L_Thumb0__': 'ValveBiped.Bip01_L_Finger0',
        'b__L_Thumb1__': 'ValveBiped.Bip01_L_Finger01',
        'b__L_Thumb2__': 'ValveBiped.Bip01_L_Finger02',
        'b__L_Index0__': 'ValveBiped.Bip01_L_Finger1',
        'b__L_Index1__': 'ValveBiped.Bip01_L_Finger11',
        'b__L_Index2__': 'ValveBiped.Bip01_L_Finger12',
        'b__L_Mid0__': 'ValveBiped.Bip01_L_Finger2',
        'b__L_Mid1__': 'ValveBiped.Bip01_L_Finger21',
        'b__L_Mid2__': 'ValveBiped.Bip01_L_Finger22',
        'b__L_Ring0__': 'ValveBiped.Bip01_L_Finger3',
        'b__L_Ring1__': 'ValveBiped.Bip01_L_Finger31',
        'b__L_Ring2__': 'ValveBiped.Bip01_L_Finger32',
        'b__L_Pinky2__': 'ValveBiped.Bip01_L_Finger4',
        'b__L_Pinky1__': 'ValveBiped.Bip01_L_Finger41',
        'b__L_Pinky0__': 'ValveBiped.Bip01_L_Finger42',
        # Right Fingers
        'b__R_Thumb0__': 'ValveBiped.Bip01_R_Finger0',
        'b__R_Thumb1__': 'ValveBiped.Bip01_R_Finger01',
        'b__R_Thumb2__': 'ValveBiped.Bip01_R_Finger02',
        'b__R_Index0__': 'ValveBiped.Bip01_R_Finger1',
        'b__R_Index1__': 'ValveBiped.Bip01_R_Finger11',
        'b__R_Index2__': 'ValveBiped.Bip01_R_Finger12',
        'b__R_Mid0__': 'ValveBiped.Bip01_R_Finger2',
        'b__R_Mid1__': 'ValveBiped.Bip01_R_Finger21',
        'b__R_Mid2__': 'ValveBiped.Bip01_R_Finger22',
        'b__R_Ring0__': 'ValveBiped.Bip01_R_Finger3',
        'b__R_Ring1__': 'ValveBiped.Bip01_R_Finger31',
        'b__R_Ring2__': 'ValveBiped.Bip01_R_Finger32',
        'b__R_Pinky2__': 'ValveBiped.Bip01_R_Finger4',
        'b__R_Pinky1__': 'ValveBiped.Bip01_R_Finger41',
        'b__R_Pinky0__': 'ValveBiped.Bip01_R_Finger42'

    }
    
    for b in bpy.context.object.data.bones:
        if b.name in dict.keys():
            b.name = dict[b.name]

rename_bones()