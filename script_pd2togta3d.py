import bpy

def rename_bones():
    
    dict = {
        # Torso
        'Hips': ' Pelvis',
        'Spine': ' Spine',
        'Spine1': ' Spine1',
        'Spine2': 'MERGEME_Spine1',
        'Neck': 'Neck',
        'Head': 'Head',
        # Left Leg
        'LeftUpLeg': ' L Thigh',
        'LeftLeg': ' L Calf',
        'LeftFoot': ' L Foot',
        'LeftToeBase': ' L Toe0',
        # Right Leg
        'RightUpLeg': ' R Thigh',
        'RightLeg': ' R Calf',
        'RightFoot': ' R Foot',
        'RightToeBase': ' R Toe0',
        # Left Arm
        'LeftShoulder': ' Bip01 L Clavicle',
        'LeftArm': ' L UpperArm',
        'LeftForeArm': ' L ForeArm',
        'LeftForeArmRoll': 'MERGEME_L ForeArm',
        'LeftHand': ' L Hand',
        # Right Arm
        'RightShoulder': 'Bip01 R Clavicle',
        'RightArm': ' R UpperArm',
        'RightForeArm': ' R ForeArm',
        'RightForeArmRoll': 'MERGEME_R ForeArm',
        'RightHand': ' R Hand',
        # Left Fingers

        # Right Fingers

        'RightHandIndex1': ' R Finger',
        'RightHandIndex2': 'R Finger01'


    }
    
    for b in bpy.context.object.data.bones:
        if b.name in dict.keys():
            b.name = dict[b.name]

rename_bones()