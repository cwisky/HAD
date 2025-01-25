import bpy
from math import radians
from mathutils import Quaternion

def calculate_distance(obj1, obj2):
    """Calculate the Euclidean distance between two objects."""
    return (obj1.location - obj2.location).length

def get_armature_rotation_quaternion(armature):
    """Get the rotation of the Armature as a quaternion."""
    if armature and armature.rotation_mode == 'QUATERNION':
        return armature.rotation_quaternion
    else:
        # Convert rotation to quaternion if it's not in quaternion mode
        return armature.rotation_euler.to_quaternion()

def render_animation_with_custom_filename(angle_deg):
    # Define the objects
    armature = bpy.data.objects.get("Armature")
    camera = bpy.data.objects.get("Camera")

    if not armature or not camera:
        print("Make sure an Armature and a Camera are present in the scene!")
        return

    # Calculate rotation (quaternion) and distance
    rotation = get_armature_rotation_quaternion(armature)
    qw, qx, qy, qz = rotation.w, rotation.x, rotation.y, rotation.z
    distance = calculate_distance(armature, camera)

    # Generate filename based on angle and rotation data
    file_name = f"animation_angle_{angle_deg}_qw_{qw:.3f}_qx_{qx:.3f}_qy_{qy:.3f}_qz_{qz:.3f}_dist_{distance:.3f}.mp4"
    output_path = bpy.path.abspath(f"C:/test/mp4/{file_name}")

    # Set rendering settings
    bpy.context.scene.render.filepath = output_path
    bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
    bpy.context.scene.render.ffmpeg.format = 'MPEG4'
    bpy.context.scene.render.ffmpeg.codec = 'H264'
    bpy.context.scene.render.ffmpeg.constant_rate_factor = 'HIGH'
    bpy.context.scene.render.ffmpeg.ffmpeg_preset = 'GOOD'

    # Render the animation
    print(f"Rendering video for angle {angle_deg} degrees...")
    bpy.ops.render.render(animation=True)
    print(f"Animation rendered and saved as {output_path}")

def rotate_and_render_armature():
    armature = bpy.data.objects.get("Armature")
    if not armature:
        print("Armature object not found!")
        return

    # Ensure the rotation mode is set to 'QUATERNION'
    armature.rotation_mode = 'QUATERNION'

    # Initial rotation quaternion
    initial_rotation = armature.rotation_quaternion.copy()

    for step in range(0, 91):  # 30 steps to cover 90 degrees
        # Calculate the current angle in degrees
        #angle_deg = step * (90 / 30)  # Divide 90 degrees into 30 steps
        angle_deg = step

        # Create a quaternion for the current absolute rotation
        rotation_quaternion = Quaternion((0, 0, 1), radians(angle_deg))

        # Apply the rotation relative to the initial rotation
        armature.rotation_quaternion = rotation_quaternion @ initial_rotation

        # Force Blender to update the scene
        bpy.context.view_layer.update()

        # Render the current state
        render_animation_with_custom_filename(angle_deg)

    print("All animations rendered successfully.")

# Run the function
rotate_and_render_armature()
