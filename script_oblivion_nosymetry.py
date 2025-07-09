import bpy

def rename_bones():
    
    dict = {
        # Left Arm
        'Bip01 Clavicle.L': 'Bip01 L Clavicle',
        'Bip01 UpperArm.L': 'Bip01 L UpperArm',
        'Bip01 Forearm.L': 'Bip01 L Forearm',
        'Bip01 Hand.L': 'Bip01 L Hand',
        # Right Arm
        'Bip01 Clavicle.R': 'Bip01 R Clavicle',
        'Bip01 UpperArm.R': 'Bip01 R UpperArm',
        'Bip01 Forearm.R': 'Bip01 R Forearm',
        'Bip01 Hand.R': 'Bip01 R Hand',
        # Left Leg
        'Bip01 Thigh.L': 'Bip01 L Thigh',
        'Bip01 Calf.L': 'Bip01 L Calf',
        'Bip01 Foot.L': 'Bip01 L Foot',
        'Bip01 Toe0.L': 'Bip01 L Toe0',
        # Right Leg
        'Bip01 Thigh.R': 'Bip01 R Thigh',
        'Bip01 Calf.R': 'Bip01 R Calf',
        'Bip01 Foot.R': 'Bip01 R Foot',
        'Bip01 Toe0.R': 'Bip01 R Toe0',
        # Left Fingers
        'Bip01 Finger00.L': 'Bip01 L Finger00',
        'Bip01 Finger01.L': 'Bip01 L Finger01',
        'Bip01 Finger02.L': 'Bip01 L Finger02',
        'Bip01 Finger10.L': 'Bip01 L Finger10',
        'Bip01 Finger11.L': 'Bip01 L Finger11',
        'Bip01 Finger12.L': 'Bip01 L Finger12',
        'Bip01 Finger20.L': 'Bip01 L Finger20',
        'Bip01 Finger21.L': 'Bip01 L Finger21',
        'Bip01 Finger22.L': 'Bip01 L Finger22',
        'Bip01 Finger30.L': 'Bip01 L Finger30',
        'Bip01 Finger31.L': 'Bip01 L Finger31',
        'Bip01 Finger32.L': 'Bip01 L Finger32',
        'Bip01 Finger40.L': 'Bip01 L Finger40',
        'Bip01 Finger41.L': 'Bip01 L Finger41',
        'Bip01 Finger42.L': 'Bip01 L Finger42',
        # Right Fingers
        'Bip01 Finger00.R': 'Bip01 R Finger00',
        'Bip01 Finger01.R': 'Bip01 R Finger01',
        'Bip01 Finger02.R': 'Bip01 R Finger02',
        'Bip01 Finger10.R': 'Bip01 R Finger10',
        'Bip01 Finger11.R': 'Bip01 R Finger11',
        'Bip01 Finger12.R': 'Bip01 R Finger12',
        'Bip01 Finger20.R': 'Bip01 R Finger20',
        'Bip01 Finger21.R': 'Bip01 R Finger21',
        'Bip01 Finger22.R': 'Bip01 R Finger22',
        'Bip01 Finger30.R': 'Bip01 R Finger30',
        'Bip01 Finger31.R': 'Bip01 R Finger31',
        'Bip01 Finger32.R': 'Bip01 R Finger32',
        'Bip01 Finger40.R': 'Bip01 R Finger40',
        'Bip01 Finger41.R': 'Bip01 R Finger41',
        'Bip01 Finger42.R': 'Bip01 R Finger42',
        #Helpers
        'Bip01 ForearmTwist.R': 'Bip01 R ForearmTwist',
        'Bip01 ForearmTwist.L': 'Bip01 L ForearmTwist',
        'Bip01 UpperArmTwist.R': 'Bip01 R UpperArmTwist',
        'Bip01 UpperArmTwist.L': 'Bip01 L UpperArmTwist'
    }
    
    for b in bpy.context.object.data.bones:
        if b.name in dict.keys():
            b.name = dict[b.name]

rename_bones()