import bpy

def rename_bones():
    
    dict = {
        # Torso
        'NPC Pelvis [Pelv]': 'NPC Pelvis',
        'NPC Spine [Spn0]': 'NPC Spine',
        'NPC Spine1 [Spn1]': 'NPC Spine1',
        'NPC Spine2 [Spn2]': 'NPC Spine2',
        'NPC Neck [Neck]': 'NPC Neck',
        'NPC Head [Head]': 'NPC Head',
        # Left Arm
        'NPC L Clavicle [LClv]': 'NPC Clavicle.L',
        'NPC L UpperArm [LUar]': 'NPC UpperArm.L',
        'NPC L Forearm [LLar]': 'NPC Forearm.L',
        'NPC L Hand [LHnd]': 'NPC Hand.L',
        # Right Arm
        'NPC R Clavicle [RClv]': 'NPC Clavicle.R',
        'NPC R UpperArm [RUar]': 'NPC UpperArm.R',
        'NPC R Forearm [RLar]': 'NPC Forearm.R',
        'NPC R Hand [RHnd]': 'NPC Hand.R',
        # Left Leg
        'NPC L Thigh [LThg]': 'NPC Thigh.L',
        'NPC L Calf [LClf]': 'NPC Calf.L',
        'NPC L Foot [Lft ]': 'NPC Foot.L',
        'NPC L Toe0 [LToe]': 'NPC Toe0.L',
        # Right Leg
        'NPC R Thigh [RThg]': 'NPC Thigh.R',
        'NPC R Calf [RClf]': 'NPC Calf.R',
        'NPC R Foot [Rft ]': 'NPC Foot.R',
        'NPC R Toe0 [RToe]': 'NPC Toe0.R',
        # Left Fingers
        'NPC L Finger00 [LF00]': 'NPC Finger00.L',
        'NPC L Finger01 [LF01]': 'NPC Finger01.L',
        'NPC L Finger02 [LF02]': 'NPC Finger02.L',
        'NPC L Finger10 [LF10]': 'NPC Finger10.L',
        'NPC L Finger11 [LF11]': 'NPC Finger11.L',
        'NPC L Finger12 [LF12]': 'NPC Finger12.L',
        'NPC L Finger20 [LF20]': 'NPC Finger20.L',
        'NPC L Finger21 [LF21]': 'NPC Finger21.L',
        'NPC L Finger22 [LF22]': 'NPC Finger22.L',
        'NPC L Finger30 [LF30]': 'NPC Finger30.L',
        'NPC L Finger31 [LF31]': 'NPC Finger31.L',
        'NPC L Finger32 [LF32]': 'NPC Finger32.L',
        'NPC L Finger40 [LF40]': 'NPC Finger40.L',
        'NPC L Finger41 [LF41]': 'NPC Finger41.L',
        'NPC L Finger42 [LF42]': 'NPC Finger42.L',
        # Right Fingers
        'NPC R Finger00 [RF00]': 'NPC Finger00.R',
        'NPC R Finger01 [RF01]': 'NPC Finger01.R',
        'NPC R Finger02 [RF02]': 'NPC Finger02.R',
        'NPC R Finger10 [RF10]': 'NPC Finger10.R',
        'NPC R Finger11 [RF11]': 'NPC Finger11.R',
        'NPC R Finger12 [RF12]': 'NPC Finger12.R',
        'NPC R Finger20 [RF20]': 'NPC Finger20.R',
        'NPC R Finger21 [RF21]': 'NPC Finger21.R',
        'NPC R Finger22 [RF22]': 'NPC Finger22.R',
        'NPC R Finger30 [RF30]': 'NPC Finger30.R',
        'NPC R Finger31 [RF31]': 'NPC Finger31.R',
        'NPC R Finger32 [RF32]': 'NPC Finger32.R',
        'NPC R Finger40 [RF40]': 'NPC Finger40.R',
        'NPC R Finger41 [RF41]': 'NPC Finger41.R',
        'NPC R Finger42 [RF42]': 'NPC Finger42.R',
        #Helpers
        'NPC L UpperarmTwist1 [LUt1]': 'NPC UpperarmTwist1.L',
        'NPC L UpperarmTwist2 [LUt2]': 'NPC UpperarmTwist2.L',
        'NPC L ForearmTwist1 [LLt1]': 'NPC ForearmTwist1.L',
        'NPC L ForearmTwist2 [LLt2]': 'NPC ForearmTwist2.L',
        
        'NPC R UpperarmTwist1 [RUt1]': 'NPC UpperarmTwist1.R',
        'NPC R UpperarmTwist2 [RUt2]': 'NPC UpperarmTwist2.R',
        'NPC R ForearmTwist1 [RLt1]': 'NPC ForearmTwist1.R',
        'NPC R ForearmTwist2 [RLt2]': 'NPC ForearmTwist2.R',
    }
    
    for b in bpy.context.object.data.bones:
        if b.name in dict.keys():
            b.name = dict[b.name]

rename_bones()